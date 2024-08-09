
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
    #{
    #  "PRJNA300878": {
    #    "Investigation": {
    #      "PRJNA300878": {
    #        "akc_id": "",
    #        "name": "Individual heritable ...",
    #        "description": "The adaptive ..."
    #        "study_type": {
    #          "id": "NCIT:C16084",
    #          "label": "Observational Study"
    #        },
    #        "archival_id": "PRJNA300878",
    #        "inclusion_criteria": " ",
    #        "release_date": "2019-09-03T17:01:10.226-05:00",
    #        "update_date": "2022-12-16T20:42:08.879Z"
    #      }
    #    },
    #    "Reference": {
    #      "PRJNA300878": {
    #        "source_uri": "",
    #        "sources": "PMID:27005435"
    #      }
    #    },
    #    "Participant": {
    #      "TW01A": {
    #        "akc_id": "",
    #        "species": {
    #          "id": "NCBITAXON:9606",
    #          "label": "Homo sapiens"
    #        },
    #        "biological_sex": "female",
    #        "age": 27,
    #        "age_unit": {
    #          "id": "UO:0000036",
    #          "label": "year"
    #        }
    #      },
    #      "TW01B": {
    #        "akc_id": "",
    #        "species": {
    #          "id": "NCBITAXON:9606",
    #          "label": "Homo sapiens"
    #        },
    #        "biological_sex": "female",
    #        "age": 27,
    #        "age_unit": {
    #          "id": "UO:0000036",
    #          "label": "year"
    #        }
    #      }
    #    },
    #    "Specimen": {
    #      "TW01A_B_naive": {
    #        "akc_id": "",
    #        "tissue": {
    #          "id": "UBERON:0013756",
    #          "label": "venous blood"
    #        }
    #      },
    #      "TW01A_B_memory": {
    #        "akc_id": "",
    #        "tissue": {
    #          "id": "UBERON:0013756",
    #          "label": "venous blood"
    #        }
    #      }
    #    }
    #  }
    #}
    def generateAKCInvestigation(self, repertoire_dict, investigation_dict, akc_class_list):
        
        # Check to make sure we have an AIRR Study ID.
        # TODO: This should be in the config file and not hardcoded here
        airr_study_field = 'study_id'
        if not airr_study_field in repertoire_dict:
            print('ERROR: Could not find AIRR study field %s in Repertoire'%(airr_study_field))
            return investigation_dict
        # Get the repertoirem study, subject, and sample ID fields from the AIRR world
        # TODO: This should be in the config file and not hardcoded here
        if 'repertoire_id' in repertoire_dict:
            repertoire_id = repertoire_dict['repertoire_id']['value']
        else:
            print('ERROR: Could not find repertoire_id field, skipping')
            return investigation_dict

        if 'sample_processing_id' in repertoire_dict:
            sample_processing_id = repertoire_dict['sample_processing_id']['value']
        else:
            print('Warning: Could not find sample_processing_id field, skipping')
            sample_processing_id = None

        if 'data_processing_id' in repertoire_dict:
            data_processing_id = repertoire_dict['data_processing_id']['value']
        else:
            print('Warning: Could not find data_processing_id field, skipping')
            data_processing_id = None

        if 'study_id' in repertoire_dict:
            study_id = repertoire_dict['study_id']['value']
        else:
            print('ERROR: Could not find study_id field, skipping')
            return investigation_dict

        if 'sample_id' in repertoire_dict:
            sample_id = repertoire_dict['sample_id']['value']
        else:
            print('ERROR: Could not find sample_id field, skipping')
            return investigation_dict

        if 'subject_id' in repertoire_dict:
            subject_id = repertoire_dict['subject_id']['value']
        else:
            print('ERROR: Could not find subject_id field, skipping')
            return investigation_dict


        # Check to see if the Investigation with that ID is in the dictionary.
        if study_id in investigation_dict:
            # If it does, we need to keep track of it
            investigation = investigation_dict[study_id]
        else:
            # If it doesn't exist we need to create a dict for this study.
            investigation = dict()
            # For each class type, create a keyed array of class instances,
            # an empty array for now.
            for akc_class in akc_class_list:
                investigation[akc_class] = dict()

            # Record the investigation for later use.
            investigation_dict[study_id] = investigation

        # Iterate over the AKC classes and build the objects we need
        for akc_class in akc_class_list:
            # Get the link/key fields for the AKC classes.
            # TODO: This should be in the config file and not hardcoded here
            if akc_class == 'Investigation':
                airr_link_field = 'study_id'
            elif akc_class == 'Reference':
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
                    print('Info: processing class %s, airr = %s, akc = %s, value = %s'%(akc_class, key, value['akc_field'],value['value']))
                    if akc_class == 'Investigation':
                        akc_object['adc_repertoire_id'] = repertoire_id
                        akc_object['adc_sample_processing_id'] = sample_processing_id
                        akc_object['adc_data_processing_id'] = data_processing_id
                    if akc_class == 'Reference':
                        akc_object['adc_repertoire_id'] = repertoire_id
                        akc_object['adc_sample_processing_id'] = sample_processing_id
                        akc_object['adc_data_processing_id'] = data_processing_id
                        akc_object['adc_study_id'] = study_id
                    if akc_class == 'Participant':
                        akc_object['adc_repertoire_id'] = repertoire_id
                        akc_object['adc_sample_processing_id'] = sample_processing_id
                        akc_object['adc_data_processing_id'] = data_processing_id
                        akc_object['adc_study_id'] = study_id
                        akc_object['adc_subject_id'] = subject_id
                    if akc_class == 'Specimen':
                        akc_object['adc_repertoire_id'] = repertoire_id
                        akc_object['adc_sample_processing_id'] = sample_processing_id
                        akc_object['adc_data_processing_id'] = data_processing_id
                        akc_object['adc_study_id'] = study_id
                        akc_object['adc_subject_id'] = subject_id
                        akc_object['adc_sample_id'] = sample_id
                    akc_dict[airr_link_value] = akc_object

            # Once processing done for this investigation, reassign the investigation dictionary
            investigation[akc_class] = akc_dict

        # Return the investigation dictionary we have built.
        return investigation_dict

