
import pandas as pd
import numpy as np
import json
import os
import sys
from datetime import datetime
from datetime import timezone
from parser import Parser
from linkml_runtime.dumpers import yaml_dumper, json_dumper, tsv_dumper
from ak_schema import *

class Repertoire(Parser):
    
    def __init__(self, verbose, airr_map):
        Parser.__init__(self, verbose, airr_map)

    # Hide the impementation of AKC data model from the other classes. 
    # repertoire_dict: Keyed on the AIRR field name, contains three attributes:
    #     value: the value of the AIRR field
    #     akc_field: the field name for the field in the AKC data model
    #     akc_class: the AKC class/object the field belongs to in the AKC data model
    def generateAKCRepertoire(self, repertoire_dict, akc_class_list):
        
        # Create a dictionary that contains the AKC class objects, keyed on
        # AKC class name. We iterate over the list of class names provided.
        akc_class_dict = dict()
        for akc_class in akc_class_list:
            # Our classes are in the global scope, so we can instantiate
            # a class using the globals function with the class name as key.
            akc_class_dict[akc_class] = globals()[akc_class]('')

        # For each class, we traverse each field to see if it belongs in
        # the class, if so we set the field in the class to be the
        # appropriate value.
        for class_key, class_value in akc_class_dict.items():
            print('Info: Processing class %s'%(class_key))
            # Iterate over the fields in the repertoire
            for key, value in repertoire_dict.items():
                # If the field has an akc_class and it is the current
                # class that we are processing, then set the field (value['akc_field'])
                # in the class (akc_class_dict[class_key]) to be the correct
                # value (value['value'])
                if 'akc_class' in value and value['akc_class'] == class_key:
                    akc_class_dict[class_key][value['akc_field']] = value['value']
        #print(yaml_dumper.dumps(akc_class_dict))
        print(json_dumper.dumps(akc_class_dict))

        return True

    # Given a flattented repertoire, add it to the investigation dict as required.
    # If the repertoire doesn't belong to the investigation, it is ignored. This
    # method is designed to build a set of AKC classes that describe an investigation
    # from the de-normalized AIRR data model.
    #
    # repertoire_dict: Keyed on the AIRR field name, contains three attributes:
    #     value: the value of the AIRR field
    #     akc_field: the field name for the field in the AKC data model
    #     akc_class: the AKC class/object the field belongs to in the AKC data model
    # study_dict: keyed on AIRR data model study identifier. Each investigation dictionary
    #     is keyed on AKC class name, containing an array of instances of each class.
    # 
    # Example:
    #     investigation_dict['PRJNA300878'] = {
    #         'Investigation':{'PRJNA300878':[]},'Participant':[],'Specimen':[]}
    def generateAKCInvestigation(self, repertoire_dict, investigation_dict, akc_class_list):
        
        # Check to make sure we have an AIRR Study ID.
        airr_study_field = 'study_id'
        if not airr_study_field in repertoire_dict:
            print('ERROR: Could not find AIRR study field %s in Repertoire'%(airr_study_field))
            return investigation_dict

        # Check to see if the Investigation with that ID is in the dictionary.
        if repertoire_dict['study_id']['value'] in investigation_dict:
            # If it does, we need to kee track of it
            investigation = investigation_dict[repertoire_dict['study_id']['value']]
        else:
            # If it doesn't exist we need to create a dict for this study.
            investigation = dict()
            # For each class type, create a keyed array of class instances,
            # an empty array for now.
            for akc_class in akc_class_list:
                investigation[akc_class] = dict()

            # Record the investigation for later use.
            investigation_dict[repertoire_dict['study_id']['value']] = investigation

        # Iterate over the AKC classes and build the objects we need
        for akc_class in akc_class_list:
            # Get the link/key fields for the AKC classes.
            # TODO: this should be in the config file.
            if akc_class == 'Investigation':
                airr_link_field = 'study_id'
            elif akc_class == 'Participant':
                airr_link_field = 'subject_id'
            elif akc_class == 'Specimen':
                airr_link_field = 'sample_id'
            else:
                print('ERROR: Could not link class %s, skipping'%(akc_class))
                continue
                
            if not airr_link_field in repertoire_dict:
                print('ERROR: Could not find link field %s, skipping'%(airr_link_field))
                continue

            # Example:
            #     investigation_dict['PRJNA300878'] = {
            #         'Investigation':{'PRJNA300878':[]},'Participant':[],'Specimen':[]}
            airr_link_value = repertoire_dict[airr_link_field]['value']
            akc_dict = investigation[akc_class]
            # Check to see if we have seen this instance before
            # E.g. 
            if airr_link_value in akc_dict:
                akc_object = akc_dict[airr_link_value]
            else:
                akc_object = globals()[akc_class]('')

            # Iterate over the Repertoire and process any fields that are of
            # the current AKC class.
            for key, value in repertoire_dict.items():
                # If the current field is of the class we are parsing,
                # process it.
                if 'akc_class' in value and value['akc_class'] == akc_class:
                    akc_object[value['akc_field']] = value['value']
                    akc_dict[airr_link_value] = akc_object
                    print('Info: processing class %s, airr = %s, akc = %s, value = %s'%(akc_class, key, value['akc_field'],value['value']))


#        # Create a dictionary that contains the AKC class objects, keyed on
#        # AKC class name. We iterate over the list of class names provided.
#        akc_class_dict = dict()
#        for akc_class in akc_class_list:
#        #    # Our classes are in the global scope, so we can instantiate
#        #    # a class using the globals function with the class name as key.
#            akc_class_dict[akc_class] = globals()[akc_class]('')
#
#        # For each class, we traverse each field to see if it belongs in
#        # the class, if so we set the field in the class to be the
#        # appropriate value.
#        for class_key, class_value in akc_class_dict.items():
#            print('Info: Processing class %s'%(class_key))
#            # Iterate over the fields in the repertoire
#            for key, value in repertoire_dict.items():
#                # If the field has an akc_class and it is the current
#                # class that we are processing, then set the field (value['akc_field'])
#                # in the class (akc_class_dict[class_key]) to be the correct
#                # value (value['value'])
#                if 'akc_class' in value and value['akc_class'] == class_key:
#                    akc_class_dict[class_key][value['akc_field']] = value['value']

        return investigation_dict

