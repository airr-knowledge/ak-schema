
import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
from datetime import timezone
from parser import Parser

class Repertoire(Parser):
    
    def __init__(self, verbose, repository_tag, repository_chunk, airr_map, repository):
        Parser.__init__(self, verbose, repository_tag, repository_chunk, airr_map, repository)

    # Hide the impementation of AKC data model from the other classes. 
    def generateAKCRepertoire(self, repertoire_dict):
        
        akc_class_dict = {"participant":{}, "Investigation":{}, "reference":{}, "specimen":{}} 

        class_dict = dict()
        for class_key, class_value in akc_class_dict.items():
            instance_dict = dict()
            for key, value in repertoire_dict.items():
                if value['akc_class'] == class_key:
                    instance_dict[value['akc_field']] = value['value']
            class_dict['%s'%(class_key)] = instance_dict
        print(json.dumps(class_dict, indent=4))
        return True

    # Hide the impementation of the repository from the Repertoire subclasses.
    # The subclasses don't ask much of the repository, just insert a single
    # JSON document at a time. Returns a record_id on success, None on failure
    def repositoryInsertRepertoire( self, json_document ):
    
        # Check to see if the repertoire already exists. We do this by using
        # the rearrangement file field and check to see if the file field
        # already exists in another record or not...
        # First get the file field we use to connect rearrangments and reperotires
        repertoire_file_field = self.getRepertoireFileField()
        # Then get the repository field
        file_repository_field = self.getAIRRMap().getMapping(repertoire_file_field,
                                                        self.getiReceptorTag(),
                                                        self.getRepositoryTag())
        # Also get the field that links repertoires to rearrangements
        link_field = self.getRepertoireLinkIDField()
        # Map it to a repository field
        link_repository_field = self.getAIRRMap().getMapping(link_field,
                                                             self.getiReceptorTag(),
                                                             self.getRepositoryTag())
        # Then get the actual files that belong to this repertoire.
        file_names = json_document[file_repository_field]
        # Check to see if there are files in the file field. If not, then pring a warning
        # as we won't be able to link any rearrangements to this repertoire. We set an empty
        # array as we want to still insert the record with the following warning...
        if file_names is None or file_names == "":
            print("Warning: Repertoire does not have any rearrangement files.")
            print("Warning:     Will not be able to link rearrangements to this repertoire")
            idarray = []
        else:
            # Finally we search for and get a list of the repertoires that have the files.
            idarray = self.repositoryGetRepertoireIDs(file_repository_field, file_names)

        # If idarray is None, there was a problem with the query.
        if idarray is None:
            print("ERROR: Unable to check for repertoire existance for file %s"%(file_names))
            print("ERROR:     Repertoires must have valid rearrangement files.")
            print("ERROR:     Rearrangement files must be unique in the repository.")
            return None

        # The number of repertoires should be 0 other wise it already exists. Fail if
        # the number is not 0.
        num_repertoires = len(idarray)
        # Get some info to help write out messages
        study_tag = self.getAIRRMap().getMapping("study_id",
                                                 self.getiReceptorTag(),
                                                 self.getRepositoryTag())
        study = "NULL" if not study_tag in json_document else json_document[study_tag]
        sample_tag = self.getAIRRMap().getMapping("sample_id", self.getiReceptorTag(),
                                                  self.getRepositoryTag())
        sample = "NULL" if not sample_tag in json_document else json_document[sample_tag]
        # Print an error if record already exists and we are NOT updating the record.
        if not self.repository.updateOnly() and not num_repertoires == 0:
            print("ERROR: Unable to write repertoire, already exists in the repository")
            print("ERROR:     Write failed for study '%s', sample '%s'"%(study, sample))
            print("ERROR:     File field %s contains rearrangement files %s"%
                  (repertoire_file_field, file_names))
            print("ERROR:     Files found in records with record IDs %s"%(str(idarray)))
            return None

        # Get the repertoire, data_processing, and sample_processing IDs for the record
        # being inserted.
        rep_id_field =  self.getAIRRMap().getMapping("repertoire_id",
                                              self.getAIRRTag(),
                                              self.getRepositoryTag(),
                                              self.getAIRRMap().getRepertoireClass())
        if rep_id_field is None:
            print("ERROR: Could not find \"repertoire_id\" field in mapping (%s -> %s)"%
                  (self.getAIRRTag(), self.getRepositoryTag()))
            return None

        data_id_field =  self.getAIRRMap().getMapping("data_processing_id",
                                              self.getAIRRTag(),
                                              self.getRepositoryTag(),
                                              self.getAIRRMap().getRepertoireClass())
        sample_id_field =  self.getAIRRMap().getMapping("sample_processing_id",
                                              self.getAIRRTag(),
                                              self.getRepositoryTag(),
                                              self.getAIRRMap().getRepertoireClass())
        # Get the mappings for the create and update fields. Both our local ones and
        # the ADC related ones. ADC fields are 'adc_publish_date' and 'adc_update_data'
        # If they aren't in the mapping, force the fields to be stored anyway.
        adc_publish_date =  self.getAIRRMap().getMapping("adc_publish_date",
                                              self.getiReceptorTag(),
                                              self.getRepositoryTag(),
                                              self.getAIRRMap().getRepertoireClass())
        if adc_publish_date is None:
            adc_publish_date = "adc_publish_date"

        adc_update_date =  self.getAIRRMap().getMapping("adc_update_date",
                                              self.getiReceptorTag(),
                                              self.getRepositoryTag(),
                                              self.getAIRRMap().getRepertoireClass())
        if adc_update_date is None:
            adc_update_date = "adc_update_date"

        ir_updated_at =  self.getAIRRMap().getMapping("ir_updated_at_repertoire",
                                              self.getiReceptorTag(),
                                              self.getRepositoryTag(),
                                              self.getAIRRMap().getRepertoireClass())
        if ir_updated_at is None:
            ir_updated_at = "ir_updated_at"

        ir_created_at =  self.getAIRRMap().getMapping("ir_created_at_repertoire",
                                              self.getiReceptorTag(),
                                              self.getRepositoryTag(),
                                              self.getAIRRMap().getRepertoireClass())
        if ir_created_at is None:
            ir_created_at = "ir_created_at"

        # Get the repertoire_id that we are trying to insert from the JSON,
        # None if not present.
        if rep_id_field in json_document:
            repertoire_id = json_document[rep_id_field]
            if repertoire_id == "":
                repertoire_id = None
        else: repertoire_id = None

        # Get the data_processing_id that we are trying to insert from the JSON,
        # None if not present.
        if data_id_field in json_document:
            data_processing_id = json_document[data_id_field]
            if data_processing_id == "":
                data_processing_id = None
        else: data_processing_id = None

        # Get the sample_processing_id that we are trying to insert from the JSON,
        # None if not present.
        if sample_id_field in json_document:
            sample_processing_id = json_document[sample_id_field]
            if sample_processing_id == "":
                sample_processing_id = None
        else: sample_processing_id = None

        # Get the number of repertoires that exist in the repository for the
        # repertoire_id we are trying to insert.
        rep_array = self.repositoryGetRepertoires(rep_id_field, repertoire_id)
        num_repertoires = len(rep_array)

        # If we are updating...
        if self.repository.updateOnly():
            # If we are updating we want the record to be unique. repertoire_id is
            # not sufficient so we have to check and see if the repertoire_id,
            # data_processing_id, and sample_processing_id is unique
            # We use the internal "link" field that is guaranteed to be unique in
            # the repository to update the record.
            if num_repertoires == 0:
                print("ERROR: Could not find Reperotire %s to update"%(repertoire_id))
                return None
            elif num_repertoires == 1:
                rep = rep_array[0]
                # If we have the correct repertoire, keep track of its link field,
                # other wise we fail as we have to have an exact match for each field.
                if (rep[sample_id_field]==sample_processing_id and 
                    rep[data_id_field]==data_processing_id and
                    rep[rep_id_field]==repertoire_id):
                    link_repository_value = rep[link_repository_field]
                else:
                    print("ERROR: Can not change repertoire/sample/data processing IDs.")
                    print("ERROR:     repertoire_id = %s,%s"%(repertoire_id,rep[rep_id_field]))
                    print("ERROR:     sample_processing_id = %s,%s"%(sample_processing_id,rep[sample_id_field]))
                    print("ERROR:     data_processing_id = %s,%s"%(data_processing_id,rep[data_id_field]))
                    return None
                    
            elif num_repertoires > 1:
                link_repository_value = None
                for rep in rep_array:
                    # If we found the correct repertoire, keep track of its "link_field"
                    # as that is the unique repository identifier we use to update that field.
                    # If not report an error and return.
                    if (rep[sample_id_field]==sample_processing_id and 
                        rep[data_id_field]==data_processing_id and
                        rep[rep_id_field]==repertoire_id):
                        if link_repository_value == None:
                            link_repository_value = rep[link_repository_field]
                        else:
                            print("ERROR: Found more than one repertoire with:")
                            print("ERROR:     repertoire_id = %s"%(repertoire_id))
                            print("ERROR:     sample_processing_id = %s"%(sample_processing_id))
                            print("ERROR:     data_processing_id = %s"%(data_processing_id))
                            return None

            # Store in our internal field the update time.
            json_document[ir_updated_at] = self.getDateTimeNowUTC()
            json_document[adc_update_date] = self.getDateTimeNowUTC()

            # Update the repertoire with the JSON data. Note that this is a non-destructive
            # and conservative update. That is, it won't remove any information AND it ONLY
            # sets fields that are different. For each field it reads the value, compares it,
            # and the writes the new value if and only if it is different.
            if self.verbose():
                print("Info: Updating Repertoire:")
                print("Info:     %s = %s"% (link_repository_field, link_repository_value))
                print("Info:     %s = %s"% (rep_id_field, repertoire_id))
                print("Info:     %s = %s"% (data_id_field, data_processing_id))
                print("Info:     %s = %s"% (sample_id_field, sample_processing_id))
            record_id = self.repository.updateRepertoire(link_repository_field,
                                                         link_repository_value,
                                                         json_document, ir_updated_at)
            return record_id
        else:

            # If we are inserting, we want the new record to not exist. If we are
            # updating we want the record to be unique. repertoire_id is not sufficient
            # so we have to check and see if the repertoire_id, data_processing_id, and
            # sample_processing_id to confirm uniqueness (update) or missing (insert). 
            if not num_repertoires == 0:
                duplicate = True
                for rep in rep_array:
                    #print("new = -%s- -%s- -%s-"%
                    #      (repertoire_id, data_processing_id, sample_processing_id))
                    #print("current = -%s- -%s- -%s-"%
                    #      (rep[rep_id_field],
                    #       rep[data_id_field],
                    #       rep[sample_id_field]))
                    # Check if the repertoire found has a different data_processing_id, if
                    # so then this is not a conflict for insertion.
                    if (data_id_field in rep and
                            not rep[data_id_field] == data_processing_id and
                            not rep[data_id_field] == "" and
                            not data_processing_id is None and
                            not data_processing_id == ""):
                        #print("DIFFERENT DATA_PROC")
                        duplicate = False
                    # Check if the repertoire found has a different sample_processing_id, if
                    # so then this is not a conflict for insertion.
                    elif (sample_id_field in rep and
                            not rep[sample_id_field] == sample_processing_id and
                            not rep[sample_id_field] == "" and
                            not sample_processing_id is None and
                            not sample_processing_id == ""):
                        #print("DIFFERENT SAMPLE_PROC")
                        duplicate = False
    
                if duplicate:
                    print("ERROR: Unable to confirm uniqieness of repertoire in repository")
                    print("ERROR:     Write failed for study '%s', sample '%s'"%(study, sample))
                    print("ERROR:     Trying to write a record with fields:")
                    print("ERROR:         %s = %s"% (rep_id_field, repertoire_id))
                    print("ERROR:         %s = %s"% (data_id_field, data_processing_id))
                    print("ERROR:         %s = %s"% (sample_id_field, sample_processing_id))
                    print("ERROR:     Unable to differentiate from repository record:")
                    print("ERROR:         %s = %s"% (rep_id_field, rep[rep_id_field]))
                    print("ERROR:         %s = %s"% (data_id_field, rep[data_id_field]))
                    print("ERROR:         %s = %s"% (sample_id_field, rep[sample_id_field]))
                    return None

            # Store in our internal field the creation and update time.
            now_str = self.getDateTimeNowUTC()
            json_document[ir_updated_at] = now_str
            json_document[ir_created_at] = now_str
            json_document[adc_publish_date] = now_str
            json_document[adc_update_date] = now_str

            # Initialize the internal rearrangement count field to 0
            rearrangement_count_field = self.getRearrangementCountField()
            count_field = self.getAIRRMap().getMapping(rearrangement_count_field,
                                                       self.getiReceptorTag(),
                                                       self.getRepositoryTag())
            if count_field is None:
                print("Warning: Could not find %s field in repository, not initialized"
                      %(rearrangement_count_field, repository_tag))
            else:
                json_document[count_field] = 0

            # Try to write the record and return record_id as appropriate.
            record_id = self.repository.insertRepertoire(json_document, link_repository_field,
                                                         ir_updated_at)
            if record_id is None:
                print("ERROR: Unable to write repertoire record to repository")
                return None

            # Update the _id fields if they were empty to force uniqueness. To do this we use
            # the record_id which is guaranteed to be unique in the repository.
            if repertoire_id is None:
                self.repository.updateField(link_repository_field, record_id,
                                            rep_id_field, str(record_id), ir_updated_at)
            if data_processing_id is None:
                self.repository.updateField(link_repository_field, record_id,
                                            data_id_field, str(record_id), ir_updated_at)
            if sample_processing_id is None:
                self.repository.updateField(link_repository_field, record_id,
                                            sample_id_field, str(record_id), ir_updated_at)
            if self.verbose:
                print("Info: Successfully wrote repertoire record <%s, %s, %s>" %
                      (study, sample, file_names))

            # Return the record ID
            return record_id

