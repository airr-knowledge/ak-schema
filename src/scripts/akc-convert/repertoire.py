
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

class CRepertoire(Parser):
    
    def __init__(self, verbose, airr_map):
        Parser.__init__(self, verbose, airr_map)

        # Map that tells how to build the name of a class instance based
        # on the classes and fields that it is composed of.
        # TODO: This should be in a config file and not hardcoded here
        self.class_name_map = {
            "Investigation" : { "classes" : ["Investigation"], "fields" : ["study_id"] },
            "Reference" : { "classes" : ["Reference"], "fields" : ["study_id"] },
            "StudyArm" : { "classes" : ["StudyArm"], "fields" : ["study_group_description"] },
            "Participant" : { "classes" : ["Participant"], "fields" : ["subject_id"] },
            "Specimen" : { "classes" : ["Specimen"], "fields" : ["subject_id", "sample_id"] },
            "LifeEvent" : { "classes" : ["LifeEvent"], "fields" : ["subject_id", "sample_id"] },
            "ImmuneExposure" : { "classes" : ["ImmuneExposure"], "fields" : ["subject_id", "disease_diagnosis"] },
            "AIRRSequencingAssay" : { "classes" : ["AIRRSequencingAssay"], "fields" : ["subject_id", "sample_id","sample_processing_id"] },
#            "NucleicAcidProcessing" : { "classes" : ["NucleicAcidProcessing"], "fields" : ["subject_id", "sample_id","sample_processing_id"] },
            "LibraryPreparationProcessing" : { "classes" : ["LibraryPreparationProcessing"], "fields" : ["subject_id", "sample_id","sample_processing_id"] },
            "CellIsolationProcessing" : { "classes" : ["CellIsolationProcessing"], "fields" : ["subject_id", "sample_id","sample_processing_id"] }
        }
        # Classes that perform a special link function between other classes
        # TODO: This should be in a config file and not harcoded here.
        self.link_classes = ['LifeEvent', 'StudyEvent']

        # Mapping of which ADC fields should be stored in a specific class to help
        # link AKC objects
        self.class_adc_map = {
                "Investigation" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id'],
                "Reference" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id'],
                "StudyArm" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id', 'subject_id', 'study_group_description'],
                "Participant" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id','subject_id', 'sample_id', 'study_group_description'],
                "LifeEvent" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id', 'subject_id', 'sample_id'],
                "ImmuneExposure" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id', 'subject_id', 'sample_id'],
                "Specimen" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id', 'subject_id', 'sample_id'],
                "CellIsolationProcessing" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id', 'subject_id', 'sample_id'],
#                "NucleicAcidProcessing" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id', 'subject_id', 'sample_id'],
                "LibraryPreparationProcessing" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id', 'subject_id', 'sample_id'],
                "AIRRSequencingAssay" : ['repertoire_id', 'sample_processing_id', 'data_processing_id', 'study_id', 'subject_id', 'sample_id'],
                "Assay" : [],
                "TCellReceptorEpitopeBindingAssay" : []
                }

        # A mapping of AKC class to the slot it should be stored in in
        # AIRRKnowledgeCommons
        self.akc_class_to_slot = {
                'Investigation':'investigations',
                'Reference':'references',
                'StudyArm':'study_arms',
                'StudyEvents':'study_events',
                'Participant':'participants',
                'LifeEvent':'life_events',
                'ImmuneExposure':'immune_exposures',
                'Assessment':'assessments',
                'Specimen':'specimens',
                'SpecimenCollection':'specimen_collections',
                'SpecimenProcessing':'specimen_processings',
                'CellIsolationProcessing':'specimen_processings',
#                'NucleicAcidProcessing':'specimen_processings',
                'LibraryPreparationProcessing':'specimen_processings',
                'Assay':'assays',
                'AIRRSequencingAssay':'assays',
                'TCellReceptorEpitopeBindingAssay':'assays',
                'Dataset':'datasets',
                'Conclusion':'conclusions',
                'Chain':'chains',
                'TCellReceptor':'tcell_receptors',
                'Epitope':'epitopes'
                }
        # A mapping of AKC class to the slot it should be stored in in
        # AIRRKnowledgeCommons
        self.akc_slot_list = [
                'investigations',
                'references',
                'study_arms',
                'study_events',
                'participants',
                'life_events',
                'immune_exposures',
                'assessments',
                'specimens',
                'specimen_collections',
                'specimen_processings',
                'assays',
                'datasets',
                'conclusions',
                'chains',
                'tcell_receptors',
                'epitopes'
                ]

    def classToSlot(self, class_name):
        if class_name in self.akc_class_to_slot:
            return self.akc_class_to_slot[class_name]
        else:
            return None

    def classToSlotList(self):
        return self.akc_class_to_slot

    def slotList(self):
        return self.akc_slot_list

    def getAIRRUniqueLink(self, repertoire_dict, link_class, akc_class):
        # Get the link name for a class instance. Default to None
        airr_link_value = None
        # Link classes are special as they play an intermediate
        # role that link two other classes. As such, there instance
        # names need to have both the source and destination classes
        # in their names. 
        # print('getAIRRUniqueLink - akc_class = %s, link_class = %s'%(akc_class, link_class))
        if akc_class in self.link_classes:
            airr_link_value = akc_class + '_' + link_class
        else:
            airr_link_value = akc_class 

        # If the class is in the class map, process it, else generate a warning.
        if akc_class in self.class_name_map:
            # Get the fields that this class needs to make it unique
            class_name_fields = self.class_name_map[akc_class]['fields']
            # Iterate over the fields and add them to the instance name
            for field in class_name_fields:
                # print('getAIRRUniqueLink - adding field %s = %s'%(field, repertoire_dict[field]['value']))
                # If the field is in the repertoire, we add the field value to the link tag.
                if field in repertoire_dict:
                    field_value = repertoire_dict[field]['value']
                    # Check to see if we have an ontology dictionary. If we do
                    # then we use the ontology ID in the link value.
                    if isinstance(field_value, dict): 
                        if 'id' in field_value:
                            # Check for an empty ontology and don't use it if empty
                            if not field_value['id'] is None:
                                # If all is good, use the link value.
                                field_value = field_value['id']
                                airr_link_value = airr_link_value + '_' + field_value
                        else:
                            # Warn that we are trying to use a dictionary field that
                            # isn't an ontology, this should not happen.
                            print('Warning: mapped field %s (%s) is not an ontology dict'%
                                    (field, field_value))
                    else:
                        airr_link_value = airr_link_value + '_' + field_value
                else:
                    print('Warning: mapped field %s not in AIRR repertoire'%(field))
        else:
            print('Warning: Could not link class %s, skipping'%(akc_class))

        # print('getAIRRUniqueLink - %s'%(airr_link_value))
        return airr_link_value

    def getAKCUniqueLink(self, akc_class_instance, akc_class, link_class):
        # Get the link name for a class instance. Default to None
        airr_link_value = None
        # Link classes are special as they play an intermediate
        # role that link two other classes. As such, there instance
        # names need to have both the source and destination classes
        # in their names. 
        #print('getAKCUniqueLink - akc_class = %s, link_class = %s'%(akc_class, link_class))
        if akc_class in self.link_classes:
            airr_link_value = akc_class + '_' + link_class
        else:
            airr_link_value = akc_class 

        # If the class is in the class map, process it, else generate a warning.
        if akc_class in self.class_name_map:
            # Get the fields that this class needs to make it unique
            class_name_fields = self.class_name_map[akc_class]['fields']
            # Iterate over the fields and add them to the instance name
            for field in class_name_fields:
                #print('getAKCUniqueLink - adding field %s = %s'%(field, akc_class_instance['adc_' + field]))
                if 'adc_' + field in akc_class_instance:
                    airr_link_value = airr_link_value + '_' + akc_class_instance['adc_' + field]
                else:
                    print('Warning: mapped field %s not in AKC class instance.'%(field))
        else:
            print('Warning: Could not link class %s, skipping'%(akc_class))

        #print('getAKCUniqueLink - %s'%(airr_link_value))
        return airr_link_value

    def addADCData(self, akc_object, akc_class, repertoire_dict):

        #print('addADCData: akc_class = %s'%(akc_class))
        if akc_class in self.class_adc_map:
            fields = self.class_adc_map[akc_class]
            #print('addADCData: fields = %s'%(fields))
            for field in fields:
                if field in repertoire_dict:
                    akc_object['adc_' + field] = repertoire_dict[field]['value']
                    #print('addADCData: adding %s = %s'%('adc_' + field, repertoire_dict[field]['value']))
                else:
                    print('Warning: Could not find field %s in repertoire'%(field))
        else:
            print('Warning: Could not find class %s in ADC class map'%(akc_class))

        return akc_object

    def removeADCData(self, akc_object, akc_class):

        #print('removeADCData: akc_class = %s'%(akc_class))
        if akc_class in self.class_adc_map:
            fields = self.class_adc_map[akc_class]
            for field in fields:
                field_name = 'adc_' + field
                if field_name in akc_object:
                    #print('removeADCData: removing %s = %s'%(field_name, akc_object[field_name]))
                    del akc_object[field_name]
                else:
                    print('Warning: Could not find field %s in repertoire'%(field))
                if 'adc_link_tag' in akc_object:
                    del akc_object['adc_link_tag']
        else:
            print('Warning: Could not find class %s in ADC class map'%(akc_class))

        return akc_object

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
        
        # Keep track of instances where we need to generate explicit "link"
        # classes for some of the more complex objects in the AKC data model.
        # TODO: This should be in a config file, not hardcoded here.
        akc_link_classes = {
                'ImmuneExposure': {'link_class' : 'LifeEvent', 'link_target':'Particpant'},
                'Specimen': {'link_class' : 'LifeEvent', 'link_target':'Particpant'},
                'Participant': {'link_class' : 'LifeEvent', 'link_target':'Particpant'}
                }
        # A mapping for AIRR classes that are used in AKC link classes (e.g. LifeEvent).
        # In these cases we need to know the equivalent AKC class to use in the
        # definition of the AKC instance
        # TODO: This should be in a config file, not hardcoded here.
        class_map = {
            'Subject':'Participant',
            'SampleProcessing':'Specimen',
            'Diagnosis':'ImmuneExposure',
        }

        # TODO: This should be in a config file, not hardcoded here.
        airr_study_field = 'study_id'
        # Check to make sure we have an AIRR Study ID.
        if not airr_study_field in repertoire_dict:
            print('ERROR: Could not find AIRR study field %s in Repertoire'%(airr_study_field))
            return investigation_dict

        # Check to see if the Investigation with that ID is in the dictionary.
        akc_base_class = 'AIRRKnowledgeCommons'
        if akc_base_class in investigation_dict:
            # If it does, we need to keep track of it
            investigation = investigation_dict[akc_base_class]
        else:
            # If it doesn't exist we need to create a dict for this study.
            investigation = globals()[akc_base_class]()

            # Record the investigation for later use.
            investigation_dict[akc_base_class] = investigation

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
        akc_ref_fields = self.getAIRRMap().getIRAKCRows(fields_of_interest)

        # Iterate over the AKC classes and build the objects we need
        for akc_class in akc_class_list:

            if not akc_class in globals():
                print('Warning: Class %s is not a valid AKC schema class, skipping'%(akc_class))
                continue

            # Get the dictionary for this class
            akc_dict = investigation[self.akc_class_to_slot[akc_class]]

            # Iterate over the Repertoire and process any fields that are of
            # the current AKC class.
            for key, value in repertoire_dict.items():

                # If the current field is of the class we are parsing,
                # process it.
                if 'akc_class' in value and value['akc_class'] == akc_class:
                    # Get the value that identifies an object from this repertoire
                    # of this class type and for the given key and value
                    class_type = ''
                    if value['airr_subclass'] in class_map:
                        class_type = class_map[value['airr_subclass']]
                    airr_link_value = self.getAIRRUniqueLink(repertoire_dict, class_type, akc_class)
                
                    # Check to see if we have seen instance labeled with airr_link_value
                    # before. If not, create a new object with the link value as the label.
                    if airr_link_value in akc_dict:
                        #if self.verbose():
                        #    print('Info: Found instance %s'%(airr_link_value))
                        akc_object = akc_dict[airr_link_value]
                    else:
                        if self.verbose():
                            print('Info: Create instance %s, field = %s, value = %s, class = %s, type = %s, airr class = %s'%(airr_link_value, value['akc_field'],value['value'], akc_class, value['akc_type'],value['airr_subclass']))
                        # The python globals object consists of a list of global entities. This
                        # will include the classes that are part of the AKC data model. So the
                        # line below instantiates an instance of the class with the name provided in akc_class.
                        if akc_class == 'Reference':
                            uri = repertoire_dict['pub_ids']['value'].replace(' ','')
                            akc_object = globals()[akc_class](source_uri=uri)
                        else:
                            akc_object = globals()[akc_class](akc_id=str(uuid.uuid4()))
                        # Generate a unique ID for this object, add the link tag and related
                        # other info we might need to link objects together later.
                        #akc_object['akc_id'] = str(uuid.uuid4())
                        akc_object['adc_link_tag'] = airr_link_value
                        akc_object = self.addADCData(akc_object, akc_class, repertoire_dict)
                        # Some classes (akc_link_classes) require the creation of other classes
                        # when they are created. This is because they are not in the AIRR data
                        # model directly. In this case they will not have any fields associated
                        # with them and therefore will not be generated. A common example is a
                        # AIRR Diagnosis, which doesn't have any time information. As such, a 
                        # LifeEvent won't be created, but this is needed to link the AKC
                        # ImmuneExposure to a Participant.
                        #
                        # We therefore need to create these classes explicitly from te akc_link_classes
                        # dictionary.
                        #
                        # First we check to see if the current class is such a class.
                        if akc_class in akc_link_classes:
                            # If so get the info required to create the class.
                            link_class_info = akc_link_classes[akc_class]
                            link_class = link_class_info['link_class']
                            # Generate the unique link ID for the class instance
                            class_link_value = self.getAIRRUniqueLink(repertoire_dict, akc_class, link_class)
                            # Get the dictionary of objects of the type of class we are creating. This is often
                            # a LifeEvent as it is these objects that often fall into this category.
                            class_link_dict = investigation[self.akc_class_to_slot[link_class]]
                            # Check to see if the instance already exists. If so we don't need to do anything.
                            # If it doesn't exist, we just create an empty one.
                            if not class_link_value in class_link_dict:
                                if self.verbose():
                                    print('Info: Create instance %s (link Class), link class = %s, target_class = %s'%(class_link_value, link_class, link_class_info['link_target']))
                                # Create the class instance required.
                                akc_link_object = globals()[link_class](akc_id=str(uuid.uuid4()))
                                # Generate a unique ID for this object, add the link tag and related
                                # other info we might need to link objects together later.
                                akc_link_object['akc_id'] = str(uuid.uuid4())
                                akc_link_object['adc_link_tag'] = class_link_value
                                akc_link_object = self.addADCData(akc_link_object, link_class, repertoire_dict)
                                # Store the new object in the class dictionary
                                class_link_dict[class_link_value] = akc_link_object
                                # Update the class dictionary in the investigation.
                                investigation[self.akc_class_to_slot[link_class]] = class_link_dict

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
                        # Keep track of the ADC repertoire that contributed to this
                        # AKC object. We use a CURIE with prefix ADC_REPERTOIRE.
                        # We build an array of source_uris in the AKC object that
                        # links back to the source of this data. This could be a 
                        # list of CURIEs from multiple repositories is the
                        # investigation exists in the ADC, IEDB, and VDJBase
                        repertoire_id = repertoire_dict['repertoire_id']['value']
                        repertoire_curie = 'ADC_REPERTOIRE:' + repertoire_id
                        # If we have the field and the repertoire doesn't already
                        # exist in the list, append the CURIE.
                        if 'source_uris' in akc_object:
                            if not repertoire_curie in akc_object['source_uris']:
                                akc_object['source_uris'].append(repertoire_curie)
                        else:
                            # If not, then we create a new list with the CURIE.
                            akc_object['source_uris'] = [repertoire_curie]
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
                                    print('Info:     Creating new array field %s.%s, value = %s'%(airr_link_value, value['akc_field'], value['value']))
                                if value['akc_is_array']:
                                    akc_object[value['akc_field']] = value['value']
                                else:
                                    print('Warning: Got array when not expecting array for field %s'%(value['akc_field']))
                        else:
                            # If the field exists (it isn't None) and the value is different
                            # print out a warning.
                            if current_value != None:
                                if current_value != value['value']:
                                    print('Warning: Value for "%s.%s" field exists and is not the same (%s vs %s)'%(airr_link_value, value['akc_field'], akc_object[value['akc_field']], value['value']))
                                else:
                                    # In this case the field already exists and we have
                                    # confirmed that the field hasn't changed as it should.
                                    if self.verbose():
                                        print('Info:     Field %s.%s matches (%s)'%(airr_link_value, value['akc_field'], current_value))
                            else:
                                # If there is no value, add the value to the object.
                                if self.verbose():
                                    print('Info:     Creating new field %s.%s, value = %s'%(airr_link_value, value['akc_field'], value['value']))
                                akc_object[value['akc_field']] = value['value']

                    # If the current field is a "link field" (the akc_form column is of type Class)
                    # we need to check to see if the referenced Class object has been created yet.
                    # This is necessary since some object might not have any fields so these instances
                    # would not be created.
                    if value['akc_form'] == "Class": 
                        # Get the link value that identifies this object.
                        class_type = value['akc_type']
                        class_link_value = self.getAIRRUniqueLink(repertoire_dict, akc_class, value['akc_type'])
                        # Get the dictionary that holds the objecst of this class.
                        akc_class_dict = investigation[self.akc_class_to_slot[value['akc_type']]]
                        # Check to see if we have seen instance labeled with class_link_value
                        # before. If not, create a new object with the link value as the label.
                        if class_link_value in akc_class_dict:
                            akc_class_object = akc_class_dict[class_link_value]
                        else:
                            if self.verbose():
                                print('Info: Create instance %s (empty Class), field = %s, value = %s, type = %s'%(class_link_value, value['akc_field'],value['value'], value['akc_type']))
                            # Create the object, set its ID, add its link tag
                            
                            akc_class_object = globals()[akc_class](akc_id=str(uuid.uuid4()))
                            #akc_class_object['akc_id'] = str(uuid.uuid4())
                            akc_class_object['adc_link_tag'] = class_link_value
                            # Add approrpiate extra ADC related data for this type of object.
                            akc_class_object = self.addADCData(akc_class_object, akc_class, repertoire_dict)
                            # Add the object to the dictionary.
                            akc_class_dict[class_link_value] = akc_class_object

                        
                    # Add the object the dictionary
                    akc_dict[airr_link_value] = akc_object

            # Once processing done for this investigation, reassign the investigation dictionary
            investigation[self.akc_class_to_slot[akc_class]] = akc_dict

        # Return the investigation dictionary we have built.
        return investigation_dict

