#!/usr/bin/python3

import os
import sys
import airr
import uuid
import numpy as np
from repertoire import CRepertoire
from linkml_runtime.dumpers import yaml_dumper, json_dumper, tsv_dumper
from ak_schema import *


class AIRRRepertoire(CRepertoire):
    
    # Constructor - call the parent class constructor.
    def __init__(self, verbose, airr_map):
        CRepertoire.__init__(self, verbose, airr_map) 

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
        class_class_map = {
                "Participant" : {
                    "Investigation" : { "classes" : ["Investigation"], "fields" : ["adc_study_id"] }
                    }
                }
        class_map = {
                "Investigation" : {
                    "participants" : {"lookup" : "forward", "class" : "Participant", "field" : "adc_study_id", "source" : "Investigation"},
                    "documents" : {"lookup" : "forward", "class" : "Reference", "field" : "adc_study_id", "source" : "Investigation"},
                    "assays" : {"lookup" : "forward", "class" : "AIRRSequencingAssay", "field" : "adc_study_id", "source" : "Investigation"},
                    "conclusions" : {"lookup" : "forward", "class" : "Conclusion", "field" : "adc_study_id", "source" : "Investigation"},
                    "simulations" : {"lookup" : "forward", "class" : "Simulation", "field" : "adc_study_id", "source" : "Investigation"}
                    },
                "Reference" : {
                    "investigations" : {"lookup" : "forward", "class" : "Investigation", "field" : "adc_study_id", "source" : "Investigation"},
                    },
                "StudyArm" : {
                    "investigation" : {"lookup" : "forward", "class" : "Investigation", "field" : "adc_study_id", "source" : "Investigation"},
                    },
                "Participant" : {
                    "age_event" : {"lookup" : "reverse", "class" : "LifeEvent", "field" : "adc_link_tag", "source" : "Investigation"},
                    "study_arm" : {"lookup" : "reverse", "class" : "StudyArm", "field" : "adc_study_group_description", "source" : "Investigation"},
                    },
                "LifeEvent" : {
                    "participant" : {"lookup" : "reverse", "class" : "Participant", "field" : "adc_subject_id", "source" : "Investigation"},
                    },
                "ImmuneExposure" : {
                    "life_event" : {"lookup" : "reverse", "class" : "LifeEvent", "field" : "adc_subject_id"},
                    },
                "Specimen" : {
                    "life_event" : {"lookup" : "reverse", "class" : "LifeEvent", "field" : "adc_repertoire_id", "source" : "Investigation"},
                    },
                "CellIsolationProcessing" : {
                    "specimen" : {"lookup" : "reverse", "class" : "LifeEvent", "field" : "adc_repertoire_id", "source" : "Specimen"},
                    },
#                "NucleicAcidProcessing" : {
#                    "specimen" : {"lookup" : "reverse", "class" : "LifeEvent", "field" : "adc_repertoire_id", "source" : "Specimen"},
#                    },
                "LibraryPreparationProcessing" : {
                    "specimen" : {"lookup" : "reverse", "class" : "LifeEvent", "field" : "adc_repertoire_id", "source" : "Specimen"},
                    },
                "AIRRSequencingAssay" : {
                    "specimen" : {"lookup" : "reverse", "class" : "LifeEvent", "field" : "adc_repertoire_id", "source" : "Specimen"},
                    }
                }
        # For every field that refers to another class, process the field.
        # For example, the particpants field in the Investigation class is an
        # array of IDs that point to the participants in the Investigation. We
        # need to build this array of IDs.
        for index, row in akc_class_fields.iterrows():
            if self.verbose():
                print('#### Processing class row: class = %s, field = %s, form = %s, type = %s, array = %s'%(
                        row['akc_class'], row['akc_field'], row['akc_form'], row['akc_type'], row['akc_is_array']))
            # Source class is the class of object where the ID comes from (e.g. Participant).
            akc_source_class = row['akc_type']
            akc_source_slot = self.classToSlot(akc_source_class)
            # Change class is the class of object that the ID reference is added to (e.g. Investigation).
            akc_change_class = row['akc_class']
            akc_change_slot = self.classToSlot(akc_change_class)
            # Get the field we are changing
            akc_change_field = row['akc_field']
            if self.verbose():
                print("AKC Change Class = %s, Change Field = %s, Source Class = %s"%(akc_change_class, akc_change_field, akc_source_class))
            # For each investigation in the top level investigation dictionary, process the investigation.
            for adc_study_id, akc_investigation in investigation_dict.items():
                if self.verbose():
                    print('Processing investigation: %s'%(adc_study_id))
                # If our investigation has the change class and the source class, process it.
                if akc_change_slot in akc_investigation and akc_source_slot in akc_investigation:
                    if self.verbose():
                        print('    Change class %s in investigation: %s'%(akc_change_class, adc_study_id))
                        print('    Looping over source class %s'%(akc_source_class))
                    # Get the dictionary for the class we are changing.
                    akc_change_class_dict = akc_investigation[self.classToSlot(akc_change_class)]
                    # Get the dictionary for the class the link is coming from.
                    akc_source_class_dict = akc_investigation[self.classToSlot(akc_source_class)]
                    
                    # Loop over the source instances from which the links are being produced.
                    for source_akc_key, source_class_instance in akc_source_class_dict.items():
                        if self.verbose():
                            print("        Processing source class instance = %s"%(source_akc_key))
                        # For each instance of the class of object is being changed, check to see
                        # if it has any fields that point to the source class.
                        for change_akc_key, change_class_instance in akc_change_class_dict.items():
                            # If the change class and the field being processed is not in our
                            # class map, we don't know how to link it so we skip it.
                            if akc_change_class in class_map and akc_change_field in class_map[akc_change_class]:
                                #if self.verbose():
                                #    print("        Change AKC key = %s, Source AKC key = %s"%(change_akc_key, source_akc_key))
                                # Get the field information on how we convert this field in this class.
                                field_info = class_map[akc_change_class][akc_change_field]
                                # A forward lookup means we use the change class to generate the class instance name
                                # we use to check if we have a match between the source and change classes
                                if field_info['lookup'] == 'forward':
                                    # self.getAKCUniqueLink generates the correct class names for us. This is where the
                                    # linking magic occurs. Don't stare at it to closely or you will fall into a trance.
                                    change_link_tag = self.getAKCUniqueLink(change_class_instance, akc_change_class, akc_source_class)
                                    #if self.verbose():
                                    #    print("        Change link tag = %s, Checking %s (Forward lookup)"%(change_link_tag, change_akc_key))
                                    # If the tags/keys match, then we need to update the links.
                                    if change_link_tag == change_akc_key:
                                        if self.verbose():
                                            print("        Found %s in change dictionary"%(change_link_tag))
                                        # If it is an array, then we append the id of the instance being linked, 
                                        # If it isn't an array then we just set the variable.
                                        if row['akc_is_array'] == True:
                                            if row['akc_type'] == 'Reference':
                                                change_class_instance[row['akc_field']].append(source_class_instance['source_uri'])
                                            else:
                                                change_class_instance[row['akc_field']].append(source_class_instance['akc_id'])
                                        else:
                                            change_class_instance[row['akc_field']] = source_class_instance['akc_id']
                                        if self.verbose():
                                            if row['akc_type'] == 'Reference':
                                                print('            %s.%s in %s = %s (from %s,%s)'%(akc_change_class, row['akc_field'], change_akc_key, source_class_instance['source_uri'],akc_source_class, source_akc_key))
                                            else:
                                                print('            %s.%s in %s = %s (from %s,%s)'%(akc_change_class, row['akc_field'], change_akc_key, source_class_instance['akc_id'],akc_source_class, source_akc_key))
                                elif field_info['lookup'] == 'reverse':
                                    # Reverse look up means we use the change class information but the source class algorithm to
                                    # generate the tag.
                                    lookup_link_tag = self.getAKCUniqueLink(change_class_instance, akc_source_class, akc_change_class)
                                    #if self.verbose():
                                    #    print("        Change link tag = %s, Checking %s (Reverse lookup)"%(lookup_link_tag, source_akc_key))
                                    # If the match, set the link variable, append if array, just set if not an array.
                                    if lookup_link_tag == source_akc_key:
                                        if self.verbose():
                                            print("        Found %s in source dictionary"%(lookup_link_tag))
                                        if row['akc_is_array'] == True:
                                            change_class_instance[row['akc_field']].append(source_class_instance['akc_id'])
                                        else:
                                            change_class_instance[row['akc_field']] = source_class_instance['akc_id']
                                        if self.verbose():
                                            print('            %s.%s in %s = %s (from %s,%s)'%(akc_change_class, row['akc_field'], change_akc_key, source_class_instance['akc_id'],akc_source_class, source_akc_key))
                                else:
                                    print("ERROR: No lookup direction for %s.%s"%(akc_change_class, row['akc_field']))

        # Clean up the adc_ keys in our objects.
        # We only want to do this if we are not in verbose mode.
        # Verbose implies debug, and if we are debugging we want to
        # keep these fields.
        if not self.verbose():
            # Iterate over the base AIRRKnowledgeCommons object
            # This object consists of arrays for each class of object in the
            # AKC
            for akc_tag, akc_object in investigation_dict.items():
                # Get the list of slots in the AIRRKnowledgeCommons objects
                # and iterate over them
                class_to_slot_list = self.classToSlotList()
                for akc_class, akc_slot in class_to_slot_list.items():
                    # For each slot in AIRRKnowledgeCommons, iterate over all
                    # instances of that type of AKC class. First get the alot
                    akc_class_slot = akc_object[akc_slot]
                    # For each instance of the type contained in the slot
                    for akc_instance, akc_instance_dict in akc_class_slot.items():
                        # Generate a temporary object of the type being processed
                        if akc_class == 'Reference':
                            tmp_object = globals()[akc_class](source_uri='')
                        else:
                            #print(akc_class)
                            tmp_object = globals()[akc_class](akc_id=str(uuid.uuid4()))
                        # If the type is the same process it. This avoids needlessly
                        # trying to process different assays from the assays slot
                        # when they are not of the correct subclass. 
                        if type(akc_instance_dict) == type(tmp_object):
                            self.removeADCData(akc_instance_dict, akc_class)
                            
        for akc_tag, akc_object in investigation_dict.items():
            # Get the list of slots in the AIRRKnowledgeCommons objects
            # and iterate over them
            slot_list = self.slotList()
            for akc_slot in slot_list:
                # Get the class list for this slot
                akc_class_slot = akc_object[akc_slot]
                # Create a new empty dictionary, we are essentially going to copy
                # the instance dictionaries with a new key that is the unique UUID
                new_slot_dict = dict()
                # For every instance, add it to the dictionary using the UUID as
                # the key.
                for akc_instance, akc_instance_dict in akc_class_slot.items():
                    if hasattr(akc_instance_dict, 'source_uri'):
                        new_slot_dict[akc_instance_dict['source_uri']] = akc_instance_dict
                    else:
                        new_slot_dict[akc_instance_dict['akc_id']] = akc_instance_dict

                # Replace the old dictionary with the new dictionary
                akc_object[akc_slot] = new_slot_dict

        # We are done, dump out the JSON to the output file.
        print(json_dumper.dumps(investigation_dict), file=out_file)

        # If we made it here we are DONE!
        return True
