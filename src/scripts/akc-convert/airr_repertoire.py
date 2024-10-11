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

        
        # Get the column of values from the akc_type column. We only want the
        # Repertoire related fields.
        type_column = self.getAIRRMap().getIRAKCMapColumn('akc_form')
        # Get a boolean column that flags columns of interest. Exclude nulls.
        fields_of_interest = np.where(type_column == 'Class',True, False)
        # Afer the following airr_fields contains N columns (e.g. iReceptor, AIRR)
        # that contain the AIRR Repertoire mappings.
        mymap = {"Participant":"adc_study_id", "LifeEvent":"adc_sample_id"}
        akc_class_fields = self.getAIRRMap().getIRAKCRows(fields_of_interest)
        for index, row in akc_class_fields.iterrows():
            print('class = %s, field = %s, form = %s, type = %s, array = %s'%(
                    row['akc_class'], row['akc_field'], row['akc_form'], row['akc_type'], row['akc_is_array']))
            akc_source_class = row['akc_type']
            akc_change_class = row['akc_class']
            for adc_study_id, akc_investigation in investigation_dict.items():
                akc_change_class_dict = akc_investigation[akc_change_class]
                # If our investigation has the source class, process it.
                if akc_source_class in akc_investigation:
                    akc_source_class_dict = akc_investigation[akc_source_class]
                    for adc_id, class_instance in akc_source_class_dict.items():
                        link_key = mymap[akc_source_class]
                        link_value = class_instance[link_key]
                        print('Setting %s field %s in %s to %s'%(akc_change_class, row['akc_field'],link_value,class_instance['akc_id']))
                        if link_value in akc_change_class_dict:
                            akc_change_class_instance = akc_change_class_dict[link_value]
                            akc_change_class_instance[row['akc_field']] = class_instance['akc_id']
                    
                

        print(json_dumper.dumps(investigation_dict), file=out_file)

        # If we made it here we are DONE!
        return True
