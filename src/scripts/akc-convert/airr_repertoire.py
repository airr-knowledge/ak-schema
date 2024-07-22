#!/usr/bin/python3

import pandas as pd
import json
import os
from datetime import datetime
from datetime import timezone
from repertoire import Repertoire
import airr

class AIRRRepertoire(Repertoire):
    
    # Constructor - call the parent class constructor.
    def __init__(self, verbose, repository_tag, repository_chunk, airr_map, repository):
        Repertoire.__init__(self, verbose, repository_tag, repository_chunk, airr_map, repository) 

    def process(self, filename):

        # Check to see if we have a file    
        if not os.path.isfile(filename):
            print("ERROR: input file " + filename + " is not a file")
            return False

        # Get the column tag for the iReceptor mapping
        ireceptor_tag = self.getiReceptorTag()

        # Get the column tag for the iReceptor mapping
        repository_tag = self.getRepositoryTag()

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
        repertoire_id_field = self.getRepertoireLinkIDField()
        repertoire_file_field = self.getRepertoireFileField()

        # The 'Repertoire' contains a dictionary for each repertoire.
        repertoire_list = []
        rep_class = self.getAIRRMap().getRepertoireClass()
        for repertoire in data['Repertoire']:
            repertoire_dict = dict()
            for key, value in repertoire.items():
                try:
                    self.akc_flatten(key, value, repertoire_dict, key, rep_class)
                except TypeError as error:
                    print("ERROR: %s"%(error))
                    return False

            # Ensure that we have a correct file name to link fields. If we can't find it 
            # this is a fatal error as we can not link any data to this set repertoire,
            # so there is no point adding the repertoire...
            repository_file_field = self.getAIRRMap().getMapping(repertoire_file_field,
                                                    ireceptor_tag, repository_tag)
            # If we can't find a mapping for this field in the repository mapping, then
            # we might still be OK if the metadata spreadsheet has the field. If the fails, 
            # then we should exit.
            if repository_file_field is None or len(repository_file_field) == 0:
                print("Warning: No repository mapping for the rearrangement file field (%s)"
                      %(repertoire_file_field))
                repository_file_field = repertoire_file_field
    
            # If we can't find the file field for the rearrangement field in the repository, then
            # abort, as we won't be able to link the repertoire to the rearrangement.
            #if not repository_file_field in repertoire_dict:
            #    print("ERROR: Could not find a repertoire file field in the metadata (%s)"
            #          %(repertoire_file_field))
            #    print("ERROR: Will not be able to link repertoire to rearrangement annotations")
            #    return False

            repertoire_list.append(repertoire_dict)
                
        # Iterate over the list and load records. Note that this code inserts all data
        # that was read in. That is, all of the non MiAIRR fileds that exist
        # are stored in the repository. So if the provided file has lots of extra fields
        # they will exist in the repository.
        # TODO: Ensure that all records are written as the correct type for the repository.
        for r in repertoire_list:
            if self.generateAKCRepertoire(r) is None: 
                return False

        # If we made it here we are DONE!
        return True
