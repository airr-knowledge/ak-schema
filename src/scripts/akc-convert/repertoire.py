
import pandas as pd
import numpy as np
import json
import os
import sys
import uuid
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

    def getAIRRUniqueLink(self, repertoire_dict, link_class, akc_class):
        # Get the link/key fields for the AKC classes.
        # TODO: This should be in the config file and not hardcoded here
        link_classes = ['LifeEvent', 'StudyEvent']
        #print('getAIRRUniqueLink - akc_class = %s, link_class = %s'%(akc_class, link_class))
        airr_link_value = None
        if akc_class in link_classes:
            prefix = akc_class + '_' + link_class
        else:
            prefix = akc_class 
        #prefix = akc_class 
        if akc_class == 'Investigation':
            if 'study_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['study_id']['value']
        elif akc_class == 'Reference':
            if 'study_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['study_id']['value']
        elif akc_class == 'Participant':
            if 'subject_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['subject_id']['value']
        elif akc_class == 'Specimen':
            if 'sample_id' in repertoire_dict and 'subject_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['subject_id']['value'] + '_' + repertoire_dict['sample_id']['value']
        elif akc_class == 'LifeEvent' and link_class == 'Participant':
            if 'subject_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['subject_id']['value'] 
        elif akc_class == 'LifeEvent' and link_class == 'ImmuneExposure':
            if 'subject_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['subject_id']['value'] 
        elif akc_class == 'LifeEvent' and link_class == 'Specimen':
            if 'subject_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['subject_id']['value'] + '_' + repertoire_dict['sample_id']['value']
        elif akc_class == 'LifeEvent':
            if 'subject_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['subject_id']['value'] + '_' + repertoire_dict['sample_id']['value']
        elif akc_class == 'ImmuneExposure':
            if 'subject_id' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['subject_id']['value']
        elif akc_class == 'StudyArm':
            if 'study_group_description' in repertoire_dict:
                airr_link_value = prefix + '_' + repertoire_dict['study_group_description']['value']
            
        if airr_link_value == None:
            print('Warning: Could not link class %s, skipping'%(akc_class))
        #print('getAIRRUniqueLink - %s'%(airr_link_value))

        return airr_link_value

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
        # Get the repertoire study, subject, and sample ID fields from the AIRR world
        # TODO: This should be in the config file and not hardcoded here
        if 'repertoire_id' in repertoire_dict:
            repertoire_id = repertoire_dict['repertoire_id']['value']
        else:
            print('ERROR: Could not find repertoire_id field, skipping')
            return investigation_dict

        if 'sample_processing_id' in repertoire_dict:
            sample_processing_id = repertoire_dict['sample_processing_id']['value']
        else:
            print('Warning: Could not find sample_processing_id field')
            sample_processing_id = None

        if 'data_processing_id' in repertoire_dict:
            data_processing_id = repertoire_dict['data_processing_id']['value']
        else:
            print('Warning: Could not find data_processing_id field')
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

        if 'study_group_description' in repertoire_dict:
            study_group_description = repertoire_dict['study_group_description']['value']
        else:
            print('ERROR: Could not find study_group_description field, skipping')
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

            # Get the dictionary for this class
            akc_dict = investigation[akc_class]


            # Iterate over the Repertoire and process any fields that are of
            # the current AKC class.
            for key, value in repertoire_dict.items():

                # If the current field is of the class we are parsing,
                # process it.
                if 'akc_class' in value and value['akc_class'] == akc_class:
                    # Get the value that identifies an object from this repertoire
                    # of this class type and for the given key and value
                    #if value['akc_form'] == "Class": 
                    #    class_type = value['akc_type']
                    #else:
                    #    class_type = ''
                    class_map = {'Subject':'Participant','SampleProcessing':'Specimen','Diagnosis':'ImmuneExposure'}
                    class_type = ''
                    if value['airr_subclass'] in class_map:
                        class_type = class_map[value['airr_subclass']]
                    #if 'akc_type' in value and not value['akc_type'] is None:
                    #    class_type = value['akc_type']
                    #airr_link_value = self.getAIRRUniqueLink(repertoire_dict, value['airr_subclass'], akc_class)
                    airr_link_value = self.getAIRRUniqueLink(repertoire_dict, class_type, akc_class)
                
                    # Check to see if we have seen instance labeled with airr_link_value
                    # before. If not, create a new object with the link value as the label.
                    if airr_link_value in akc_dict:
                        akc_object = akc_dict[airr_link_value]
                    else:
                        print('Info: Create instance %s, field = %s, value = %s, class = %s, type = %s, airr class = %s'%(airr_link_value, value['akc_field'],value['value'], akc_class, value['akc_type'],value['airr_subclass']))
                        akc_object = globals()[akc_class]('')
                        akc_object['akc_id'] = str(uuid.uuid4())

                    # Check to see if the field exists. If so then check the
                    # value. They should be the same. If not generate an error message.
                    # Because we are mapping ADC to AKC, ADC is not normalized. So in
                    # a sense we are normalizing the ADC data. In this case, for example
                    # the study fields (title, publications, etc) should be the same
                    # across all repertoires from the same study. Similarly, all of the 
                    # subject fields (age, subject id, sex, etc) should be the same for
                    # the same subject across all repertoires. This is performing a 
                    # sanity check on the ADC data and generates a warning when data
                    # differs when it presumably should not.
                    if value['akc_field'] in akc_object: 
                        # The field already exists in the object, get the existing value.
                        current_value = akc_object[value['akc_field']]
                        if isinstance(current_value, list):
                            if len(current_value) > 0:
                                # If we have a value check to see if it is different
                                if (current_value.sort() != [value['value']].sort()):
                                    print('Warning: Lists for field "%s" field (%s=%s) exists and are not the same (%s vs %s)'%(value['akc_field'],akc_class,airr_link_value,akc_object[value['akc_field']],value['value']))
                            else:
                                # If no value, create an empty list with the value.
                                if self.verbose():
                                    print('Info: Creating new field %s.%s, value = %s'%(akc_class,value['akc_field'],value['value']))
                                akc_object[value['akc_field']] = [value['value']]
                        else:
                            # If the field exists (it isn't None) and the value is different
                            # print out a warning.
                            if current_value != None:
                                if current_value != value['value']:
                                    print('Warning: Value for "%s" field (%s=%s) exists and is not the same (%s vs %s)'%(value['akc_field'],akc_class,airr_link_value,akc_object[value['akc_field']],value['value']))
                                else:
                                    # In this case the field already exists and we have
                                    # confirmed that the field hasn't changed as it should.
                                    if self.verbose():
                                        print('Info: Field %s matches'%(value['akc_field']))
                            else:
                                # If there is no value, add the value to the object.
                                if self.verbose():
                                    print('Info: Creating new field %s.%s, value = %s'%(akc_class,value['akc_field'],value['value']))
                                akc_object[value['akc_field']] = value['value']

                    if value['akc_form'] == "Class": 
                        class_type = value['akc_type']
                        class_link_value = self.getAIRRUniqueLink(repertoire_dict, akc_class, value['akc_type'])
                        #class_link_value = self.getAIRRUniqueLink(repertoire_dict, class_type, value['akc_type'])
                        #class_link_value = self.getAIRRUniqueLink(repertoire_dict, value['airr_subclass'], value['akc_type'])
                        akc_class_dict = investigation[value['akc_type']]
                        # Check to see if we have seen instance labeled with airr_link_value
                        # before. If not, create a new object with the link value as the label.
                        if class_link_value in akc_class_dict:
                            akc_class_object = akc_dict[airr_link_value]
                        else:
                            if self.verbose():
                                print('Info: Create instance %s(empty Class), field = %s, value = %s, type = %s'%(class_link_value, value['akc_field'],value['value'], value['akc_type']))
                            print('Info: Create instance %s(empty Class), field = %s, value = %s, type = %s'%(class_link_value, value['akc_field'],value['value'], value['akc_type']))
                            akc_class_object = globals()[akc_class]('')
                            akc_class_object['akc_id'] = str(uuid.uuid4())
                            akc_class_object['adc_repertoire_id'] = repertoire_id
                            akc_class_object['adc_sample_processing_id'] = sample_processing_id
                            akc_class_object['adc_data_processing_id'] = data_processing_id
                            akc_class_object['adc_study_id'] = study_id
                            akc_class_object['adc_subject_id'] = subject_id
                            akc_class_object['adc_sample_id'] = sample_id
                            akc_object['adc_study_group_description'] = study_group_description
                            akc_class_object['adc_link_tag'] = class_link_value
                            akc_class_dict[class_link_value] = akc_class_object

                        
                    # Add a bunch of extra fields to track the key ADC fields that 
                    # might be needed later to link AKC objects together.
                    akc_object['adc_repertoire_id'] = repertoire_id
                    akc_object['adc_sample_processing_id'] = sample_processing_id
                    akc_object['adc_data_processing_id'] = data_processing_id
                    akc_object['adc_study_id'] = study_id
                    akc_object['adc_subject_id'] = subject_id
                    akc_object['adc_sample_id'] = sample_id
                    akc_object['adc_study_group_description'] = study_group_description
                    akc_object['adc_link_tag'] = airr_link_value
                    akc_dict[airr_link_value] = akc_object

            # Once processing done for this investigation, reassign the investigation dictionary
            investigation[akc_class] = akc_dict

        # Return the investigation dictionary we have built.
        return investigation_dict

