#!/usr/bin/python3

import os
import airr
import numpy as np
from repertoire import Repertoire
from linkml_runtime.dumpers import yaml_dumper, json_dumper, tsv_dumper


class AIRRRepertoire(Repertoire):
    
    # Constructor - call the parent class constructor.
    def __init__(self, verbose, airr_map):
        Repertoire.__init__(self, verbose, airr_map) 

    def process(self, filename, out_file):

        # Check to see if we have a file    
        if not os.path.isfile(filename):
            print("ERROR: input file " + filename + " is not a file")
            return False

        # Get the column tag for the iReceptor mapping
        ireceptor_tag = self.getiReceptorTag()

        # Get the column tag for the AKC mapping
        akc_tag = self.getAKCTag()

        # Check the validity of the repertoires from an AIRR perspective
        try:
            data = airr.load_repertoire(filename)
        except airr.ValidationError as err:
            print("Warning: AIRR repertoire validation failed for file %s - %s" %
                  (filename, err))
        except Exception as err:
            print("ERROR: AIRR repertoire validation failed for file %s - %s" %
                  (filename, err))
            return False

        # Get the fields to use for finding repertoire IDs, either using those IDs
        # directly or by looking for a repertoire ID based on a rearrangement file
        # name.
        #repertoire_id_field = self.getRepertoireLinkIDField()
        #repertoire_file_field = self.getRepertoireFileField()

        # The 'Repertoire' contains a dictionary for each repertoire.
        repertoire_list = []
        rep_class = self.getAIRRMap().getRepertoireClass()
        # For each repertoire, process it.
        for repertoire in data['Repertoire']:
            # Create a dictionary to contain all the AKC info for this repertoire.
            repertoire_dict = dict()
            # For each field, process it
            for key, value in repertoire.items():
                # Our processing is to flatten the data recursively. This populates
                # the dictionary with an AKC representation of the repertoire data.
                try:
                    self.akc_flatten(key, value, repertoire_dict, key, rep_class)
                except TypeError as error:
                    print("ERROR: %s"%(error))
                    return False

            # Append the dictionary for this repertoire to the list.
            repertoire_list.append(repertoire_dict)
                
        # Extract the AIRR Map akc_class column, drop any NaN values
        # and return a list of the unique classes from the AKC. 
        akc_class_column = self.getAIRRMap().getRepertoireMapColumn('akc_class')
        akc_class_list = akc_class_column.dropna().unique()
        print('Info: Processing AKC classes: %s'%(akc_class_list))

        # Iterate over the repertoire list and process each repertoire. 
        # This will result in a populated dictionary with all of the
        # entities populated, but none of the cross references to other
        # entities resolved
        investigation_dict = dict()
        for repertoire_dict in repertoire_list:
            investigation_dict = self.generateAKCInvestigation(repertoire_dict, investigation_dict, akc_class_list) 

        
        # Now we need to resolve the cross references between objects.

        # Get the column of values from the akc_type column. We only want the
        # Repertoire related fields.
        type_column = self.getAIRRMap().getIRAKCMapColumn('akc_form')
        # Get a boolean column that flags columns of interest. Exclude nulls.
        # We want only those rows where the type_column is "Class" as this
        # indicates that the field is a reference field to another class of object
        fields_of_interest = np.where(type_column == 'Class',True, False)
        # Afer the following akc_class_fields contains N columns (e.g. iReceptor, AIRR)
        # that contain the AKC class fields. Note these are the fields tagged with
        # AKC_Metadata in the ir_class column. This does not iterate over the normal
        # AIRR mapping columns.
        akc_class_fields = self.getAIRRMap().getIRAKCRows(fields_of_interest)
        # A utility mapping dictionary that tells us which ADC field we use to link
        # AKC objects to their reference objects.
        class_map = {
                "Investigation" : {
                    "participants" : {"class" : "Participant", "field" : "adc_study_id"},
                    "documents" : {"class" : "Reference", "field" : "adc_study_id"},
                    "assays" : {"class" : "Assay", "field" : "adc_study_id"},
                    "conclusions" : {"class" : "Conclusion", "field" : "adc_study_id"},
                    "simulations" : {"class" : "Simulation", "field" : "adc_study_id"}
                    },
                "Participant" : {
                    "age_event" : {"class" : "LifeEvent", "field" : "adc_subject_id"},
                    },
                "LifeEvent" : {
                    "participant" : {"class" : "Participant", "field" : "adc_subject_id"},
                    },
                "Specimen" : {
                    "life_event" : {"class" : "LifeEvent", "field" : "adc_sample_id"},
                    }
                }
        # For every field that refers to another class, process the field.
        # For example, the particpants field in the Investigation class is an
        # array of IDs that point to the participants in the Investigation. We
        # need to build this array of IDs.
        for index, row in akc_class_fields.iterrows():
            if self.verbose():
                print('**** Processing class row: class = %s, field = %s, form = %s, type = %s, array = %s'%(
                        row['akc_class'], row['akc_field'], row['akc_form'], row['akc_type'], row['akc_is_array']))
            # Source class is the class of object where the ID comes from (e.g. Participant).
            akc_source_class = row['akc_type']
            # Change class is the class of object that the ID reference is added to (e.g. Investigation).
            akc_change_class = row['akc_class']
            # Get the field we are changing
            akc_change_field = row['akc_field']
            print("AKC Change Class = %s, Change Field = %s, Source Class = %s"%(akc_change_class, akc_change_field, akc_source_class))
            # For each investigation in the top level investigation dictionary, process the investigation.
            for adc_study_id, akc_investigation in investigation_dict.items():
                if self.verbose():
                    print('Processing investigation: %s'%(adc_study_id))
                # If our investigation has the change class and the source class, process it.
                if akc_change_class in akc_investigation and akc_source_class in akc_investigation:
                    if self.verbose():
                        print('Change class %s and source class %s in investigation: %s'%(akc_change_class, akc_source_class, adc_study_id))
                    # Get the dictionary for the class we are changing.
                    akc_change_class_dict = akc_investigation[akc_change_class]
                    # Get the dictionary for the class the link is coming from.
                    akc_source_class_dict = akc_investigation[akc_source_class]
                    
                    # For each instance that might need to be changed, process it.
                    for change_adc_id, change_class_instance in akc_change_class_dict.items():
                        # If we have a mapping for these classes and fields, continue
                        if akc_change_class in class_map and akc_change_field in class_map[akc_change_class]:
                            if self.verbose():
                                print("    Processing change class instance = %s"%(change_adc_id))
                            link_info = class_map[akc_change_class][akc_change_field]
                            link_key = link_info['field']
                            link_value = change_class_instance[link_key]
                            if self.verbose():
                                print("    Got a class map, link field = %s"%(link_key))
                                print("    Got a class map, link value = %s"%(link_value))
                            #if link_key in source_class_instance:
                            # For each potential source of change, process it.
                            for source_adc_id, source_class_instance in akc_source_class_dict.items():
                                if self.verbose():
                                    print("        Processing source class instance = %s"%(source_adc_id))
                                #self.getAIRRUniqueLink(repertoire_dict, row['airr_subclass'],row['akc_class'])
                                # If the link key is in the source class, and the source class link key is
                                # the same as the current link value, then we need to set the field.
                                if link_key in source_class_instance and source_class_instance[link_key] == link_value:

                                    print('        Setting %s field %s in %s to %s (from %s,%s), link value = %s,  multivalue = %s'%(akc_change_class, row['akc_field'],change_adc_id,source_class_instance['akc_id'],akc_source_class, source_adc_id, link_value, row['akc_is_array']))
                                    if row['akc_is_array'] == True:
                                        change_class_instance[row['akc_field']].append(source_class_instance['akc_id'])
                                    else:
                                        change_class_instance[row['akc_field']] = source_class_instance['akc_id']
                        else:
                            print("Warning: No mapping for %s/%s"%(akc_change_class, akc_change_field))
                    
                

        print(json_dumper.dumps(investigation_dict), file=out_file)

        # If we made it here we are DONE!
        return True
