# Parent Parser class of data file type specific AIRR data parsers
# Extracted common code patterns shared across various parsers.

from os.path import join
from datetime import datetime
from datetime import timezone
import re
import os
import pandas as pd
import numpy as np
from ak_schema import *



class Parser:

    # Class constructor
    def __init__(self, verbose, airr_map):

        # Keep track of the verbosity level
        self.verbose_level = verbose

        # The tag in the map file to use for iReceptor specific fields
        self.ireceptor_tag = "ir_id" 

        # The tag in the map file to use for AIRR specific fields
        self.airr_tag = "airr" 

        # The tag in the map file to use for AKC specific fields
        self.akc_tag = "akc_field" 

        # A helper variable that parser's can use if they need to create a scratch
        # folder for storing temporary data in it. The folder name is guaranteed to
        # be unique to the process being run, as it uses the process id in the folder
        # name.
        self.scratchFolder = ""

        # Save the AIRR Mapping object
        self.airr_map = airr_map

        # Keep track of the fields that we use to link the two types of files
        # that we parse, repertoire and rearrangement files. When we parse
        # rearrangement files, we assume that all of the rearrangements in each
        # file belong to a single repertoire, although it is possible to have more
        # than one file contain rearrangements of the same repertoire.
        #
        # As a result, when we load a file of rearrangements we need to associate
        # each file with a repertoire. There are two ways of doing this.
        # 
        # Firstly, each row in the Repertoire collection has a ID field
        # (identified by a specific iReceptor field) and it is this field 
        # that must be unique across all of the repertoires in the repository. As
        # a result, it is possible to specify a ID to which all of the
        # rearrangements, clones, cells, or expression in a specific file should be associated.
        #
        # Secondly, it is possible to use the reperotire file name of the file 
        # being loaded to identify the repertoire to which the rearrangements,
        # clones, cells, and gene expression belong. The file name for rearrangements,
        # clones, cells, and gene expression is stored in a field (again, identified
        # by a specific iReceptor field).
        #
        # Below, we keep track of these important fields. This is
        # maintained by the Parser class because these are the fields that link
        # the two types of parsed files. repertoire_link_id field is the ID of
        # record in the repertoire collection. Rearrangements are associated with
        # this ID through the field identified by the rearrangement_linkid_field.
        # The repertoire_file_field is the field in the repertoire where file
        # names for rearrangement, clone, cell, and gene expression files are stored. This
        # is the main lookup mechanism when a rearrangement, clone, cell, or gene expression
        # file is loaded against a repertoire.
        #
        # Finally ir_*_count it the internal field that the repository
        # uses to cache the count of all the data that belong to a specific
        # repertoire record.
        self.repertoire_linkid_field = "ir_annotation_set_metadata_id"
        self.repertoire_file_field = "ir_rearrangement_file_name"
        self.rearrangement_count_field = "ir_sequence_count"
        self.clone_count_field = "ir_clone_count"
        self.cell_count_field = "ir_cell_count"
        self.expression_count_field = "ir_expression_count"

        # We need to keep track of the field (identified by an iReceptor 
        # field name) in the annotation collection that points to the
        # Repertoire ID field in the repertoire collection. This should be
        # set by the subclass (Rearrangement, Clone, Cell, or Expression).
        self.annotation_linkid_field = ""

    # Sanity check for validity for the parser...
    def checkValidity(self):
        if not self.airr_map.hasColumn(self.ireceptor_tag):
            print("ERROR: Could not find required iReceptor column in AIRR Mapping")
            return False
        if not self.airr_map.hasColumn(self.airr_tag):
            print("ERROR: Could not find required AIRR column in AIRR Mapping")
            return False
        if not self.airr_map.hasColumn(self.akc_tag):
            print("ERROR: Could not find required AKC column in AIRR Mapping")
            return False
        return True

    # Utility methods to return internal field names of importance
    def getRepertoireLinkIDField(self):
        return self.repertoire_linkid_field

    def getRepertoireFileField(self):
        return self.repertoire_file_field

    def getRearrangementCountField(self):
        return self.rearrangement_count_field

    def getCloneCountField(self):
        return self.clone_count_field

    def getCellCountField(self):
        return self.cell_count_field

    def getExpressionCountField(self):
        return self.expression_count_field

    def getAnnotationLinkIDField(self):
        return self.annotation_linkid_field

    # Utility method to return the tag used by the mapping for the AKC.
    def getAKCTag(self):
        return self.akc_tag
    # Utility method to return the tag used by the mapping for the iReceptor fields.
    def getiReceptorTag(self):
        return self.ireceptor_tag
    # Utility method to return the tag used by the mapping for the AIRR fields.
    def getAIRRTag(self):
        return self.airr_tag

    # Utility method to return the verbose boolean flag - all parsers need this.
    def verbose(self):
        return self.verbose_level

    # Utility method to get the AIRR Map class associated with this object.
    def getAIRRMap(self):
       return self.airr_map

    # Utility function to map a key of a specific value to the correct field for
    # the AKC. Possible to limit the mapping to a class in the mapping.
    def fieldToAKC(self, field, map_class=None):

        # Check to see if the field is in the AIRR mapping, if not warn.
        airr_field = self.getAIRRMap().getMapping(field, self.airr_tag,
                                                  self.airr_tag, map_class)
        if airr_field is None:
            print("Warning: Could not find %s in AIRR mapping"%(field))

        # Check to see if the field can be mapped to a field in the AKC, if not warn.
        akc_field = self.getAIRRMap().getMapping(field, self.airr_tag,
                                                 self.akc_tag, map_class)
        if akc_field is None:
            akc_field = field
            print("Warning: Could not find AKC mapping for %s, storing as is"%(field))

        # Return the mapping.
        return akc_field

    @staticmethod
    def len_null_to_0(value):
        if pd.isnull(value) or value is None or not isinstance(value,(str)):
            return 0
        else:
            return len(value)

    @staticmethod
    def len_null_to_null(value):
        if pd.isnull(value) or value is None or not isinstance(value,(str)):
            return np.nan
        else:
            return len(value)

    @staticmethod
    def null_integer_to_0(value):
        if pd.isnull(value) or value is None:
            return 0
        else:
            return value

    @staticmethod
    def to_string(value):
        # Some string values are lists of strings, so we return the list.
        # For now we don't check the contents of the list for string type.
        if isinstance(value, (list)):
            return value
        # Null values are OK
        elif pd.isnull(value):
            return np.nan
        # If its a string, return it
        elif isinstance(value, (str)):
            return value
        # Convert to string, if it generates an error that is OK as errors
        # are expected as failure mode for this method.
        else:
            return str(value)

        # If we get here something bad happened
        raise TypeError("Can't convert value %s (%s) to string"%(str(value), type(value)))

    @staticmethod
    def to_number(value):
        # Some string values are lists of strings, so we return the list.
        # For now we don't check the contents of the list for string type.
        if isinstance(value, (list)):
            raise TypeError("Can't convert value %s (%s) to number"
                            %(str(value), type(value)))
        # Null values are OK
        elif pd.isnull(value):
            return np.nan
        # If its a float or an integer, return it
        elif isinstance(value, (float, int)):
            return float(value)
        # If its a string, try and convert it, handling the error
        elif isinstance(value, (str)):
            # If it is an empty string, treat that has a Null
            if value == "":
                return np.nan
            # Try and convert the string and if it fails, handle the error.
            try:
                return float(value)
            except Exception as err:
                raise TypeError("Can't convert value %s (%s) to string"
                                 %(str(value), type(value)))
        # If we get here something bad happened
        raise TypeError("Can't convert value %s (%s) to string"
                        %(str(value), type(value)))

    @staticmethod
    def to_integer(value):
        # Some string values are lists of strings, so we return an error. We
        # don't check for lists of integers.
        if isinstance(value, (list)):
            raise TypeError("Can't convert value %s (%s) to integer"
                            %(str(value), type(value)))
        # Null values are OK
        elif pd.isnull(value):
            return np.nan
        # If its a integer, return it
        elif isinstance(value, int):
            return value
        # If its a float, try and convert it.
        elif isinstance(value, float):
            if int(value) == value:
                return int(value)
            else:
                raise TypeError("Can't convert value %f (%s) to integer"
                                %(value, type(value)))
        # If its a string, try and convert it, handling the error
        elif isinstance(value, (str)):
            # If it is an empty string, treat that has a Null
            if value == "":
                return np.nan
            # Try and convert the string and if it fails, handle the error.
            try:
                return int(value)
            except Exception as err:
                raise TypeError("Can't convert value %s (%s) to integer"
                                 %(str(value), type(value)))
        # If we get here something bad happened
        raise TypeError("Can't convert value %s (%s) to integer"%(str(value), type(value)))

    @staticmethod
    def to_boolean(value):
        # Null values are OK
        if pd.isnull(value):
            return np.nan
        elif isinstance(value, (bool)):
            return value
        elif isinstance(value, (str)):
            if value in ["T","t","True","TRUE","true","1"]:
            	return True
            elif value in ["F","f","False","FALSE","false","0"]:
                return False
            else:
                raise TypeError("Can't convert string value %s to boolean"%(value))
        elif isinstance(value, (int)):
            if value in [1]:
            	return True
            elif value in [0]:
                return False
            else:
                raise TypeError("Can't convert integer value %d to boolean"%(value))
        # If we get here we failed...
        raise TypeError("Can't convert value %s (%s) to boolean"%(str(value), type(value)))

    @staticmethod
    def str_to_bool(string_value):
        # Null values are OK, as are string variations of various types...
        if pd.isnull(string_value):
            return None
        elif not isinstance(string_value, (str)):
            raise TypeError("Can't convert non-string value " + str(string_value))
        elif string_value in ["T","t","True","TRUE","true","1"]:
            return True
        elif string_value in ["F","f","False","FALSE","false","0"]:
            return False
        # If we get here we failed...
        raise TypeError("Can't convert string " + string_value + " to boolean")

    @staticmethod
    def int_to_bool(int_value):
        # Null values are OK as are 1/0, nothing else...
        if pd.isnull(int_value):
            return None
        elif not isinstance(int_value, (int)):
            raise TypeError("Can't convert non-integer value " + str(int_value))
        elif int_value == 1:
            return True
        elif int_value == 0:
            return False
        # If we get here we failed...
        raise TypeError("Can't convert integer " + str(int_value) + " to boolean")
 
    @staticmethod
    def float_to_str(float_value):
        # Pandas null, return null
        if pd.isnull(float_value):
            return None
        # We expect a float!!!
        elif not isinstance(float_value, (float)):
            raise TypeError("Can't convert non-float value " + str(float_value))
        # Convert away
        else:
            return str(float_value)

    @staticmethod
    def str_to_float(str_value):
        # Pandas null, None, or empty string map to a null value.
        if pd.isnull(str_value) or str_value is None or str_value == "":
            return None
        # If it ain't string, we have a problem...
        elif not isinstance(str_value, (str)):
            raise TypeError("Can't convert non-float value " + str(str_value))
        # Convert away...
        else:
            return float(str_value)

    @staticmethod
    def str_to_int(str_value):
        # Pandas null, None, or empty string map to a null value.
        if pd.isnull(str_value) or str_value is None or str_value == "":
            return None
        # If it ain't string, we have a problem...
        elif not isinstance(str_value, (str)):
            raise TypeError("str_to_int: Can't convert non-string value " + str(str_value))
        # Convert away...
        else:
            float_value = float(str_value)
            if float(int(str_value)) != float_value:
                raise TypeError("str_to_int: Can't convert a non integer float to an integer, " +
                                str_value)
            return int(str_value)

    @staticmethod
    def float_to_int(float_value):
        # Pandas null or None map to a null value.
        if float_value is None or pd.isnull(float_value):
            return None
        # If it ain't float, we have a problem...
        elif not isinstance(float_value, (float)):
            # OK, this is really weird... In and ideal world this function would
            # always take a float, so we wouldn't need the test below. This method
            # would typically get used on a Pandas data frame column, which are 
            # supposed to be all the same type (correct me if I am wrong). For
            # some mysterious reason, when this is called from 
            # Rearrangement.mapToRepositoryType where the type of the first
            # element of a column is a float, somehow other values in the 
            # data frame have different types (an empty string rather than None).
            # This takes care of this case - not sure why this happens!
            if isinstance(float_value, (str)) and float_value == "":
                return None
            raise TypeError("Can't convert non-float value '%s' (%s)"
                            %(str(float_value), type(float_value)))
        # Convert away...
        else:
            if float(int(float_value)) != float_value:
                raise TypeError("Can't convert a non integer float to an integer, " +
                                str(float_value))
            return int(float_value)


    # Utility function to map a key of a specific value to the correct type for
    # the AKC. 
    def valueToAKC(self, field, field_column, value, map_class=None):
        # Define the columns to use for the mappings
        airr_type_tag = "airr_type"
        airr_nullable_tag = "airr_nullable"
        airr_array_tag = "airr_is_array"
        akc_type_tag = "akc_type"

        # Get the types of the fields, both the AIRR type and the AKC type
        airr_field_type = self.getAIRRMap().getMapping(field, field_column,
                                                airr_type_tag, map_class)
        akc_field_type = self.getAIRRMap().getMapping(field, field_column,
                                                akc_type_tag, map_class)
        field_nullable = self.getAIRRMap().getMapping(field, field_column,
                                                airr_nullable_tag, map_class)
        is_array = self.getAIRRMap().getMapping(field, field_column,
                                                airr_array_tag, map_class)

        # Check for a null value on a nullable field, if it happens this is an error
        # so raise an exception. Note if we could not find a mapping for the
        # field in the nullable mapping column then this is not an error. No nullable
        # mapping means we don't know if it is nullable or not, so we assume it is.
        if value is None and not field_nullable is None and not field_nullable:
            raise TypeError("Null value for AIRR non nullable field " + field)

        # Do a default the conversion for the value
        akc_value = value

        #print("Info: Converting field %s %s"%(field, value))
        #print("Info:    field type %s %s"%(airr_field_type, akc_field_type))
        #print("Info:    nullable %s"%(str(field_nullable)))
        #print("Info:    is_array %s"%(str(is_array)))

        # Handle arrays first... We want to do this as the field_type of an
        # array is a string, which can mess us up.
        if is_array:
            # Handle arrays, a null value is OK...
            if value is None:
                akc_value = None
            elif isinstance(value, list):
                # Currently, the spec only supports arrays of strings. If any of the
                # elements are not string, raise a type error.
                for item in value:
                    self.valueToRepository(field, field_column, item, map_class)
                # Otherwise, return the array of strings...
                akc_value = value
            elif isinstance(value, str):
                # Assume a comma separated list of strings, create the array and return it.
                akc_value = value.split(',')
                if isinstance(akc_value, list):
                    akc_value = [x.strip() for x in akc_value]
                else:
                    raise TypeError("Unable to convert a ',' separated string to an array (" +
                                     value + ")")
            else:
                if self.verbose():
                    print("Info: Unable to convert field %s = %s (%s, %s, %s), not converted"%
                          (field, value, airr_field_type, akc_field_type, type(value)))
        elif akc_field_type == "string":
            # We don't want null strings, we want empty strings.
            if value is None:
                akc_value = None 
            else:
                akc_value = str(value)
        elif akc_field_type == "boolean":
            # Even though python does not allow boolean values to be null
            # (e.g. bool(None) == False), JSON and data repositories often do,
            # so in this case we don't want to return False for a None value. 
            # We want to return None...
            if value is None:
                akc_value = None
            elif isinstance(value,(str)):
                akc_value = Parser.str_to_bool(value)
            elif isinstance(value,(int)):
                akc_value = Parser.int_to_bool(value)
            else:
                akc_value = bool(value)
        elif akc_field_type == "integer":
            # We allow integers to be null, as we don't know what to replace them
            # with.
            if value is None:
                akc_value = None
            else:
                # This is a complex case... We are converting a boolean AIRR field to
                # an integer representation of that boolean value. The problem is that
                # on loading the boolean AIRR field may be represented as an integer (0/1),
                # a string (T/True/TRUE/true), or a boolean (True/False). We want to handle 
                # all of these cases.
                if airr_field_type == "boolean":
                    if isinstance(value, (int)):
                        if value == 1: akc_value = 1
                        elif value == 0: akc_value = 0
                        else:
                            raise TypeError("Invalid boolean value " + str(value) +
                                            " for field " + field)
                    elif isinstance(value, (str)):
                        if value in ["T","t","True","TRUE","true"]:
                            akc_value = 1
                        elif value in ["F","f","False","FALSE","false"]:
                            akc_value = 0
                        else:
                            raise TypeError("Invalid boolean value " + value +
                                            " for field " + field)
                    elif isinstance(value, (bool)):
                        if value == True: akc_value = 1
                        elif value == False: akc_value = 0
                        else:
                            raise TypeError("Invalid boolean value " + str(value) +
                                            " for field " + field)
                    else:
                        raise TypeError("Invalid boolean value " + str(value) +
                                            " for field " + field)

                else:
                    # This is the base case - we convert an integer to an integer...
                    akc_value = int(value)
        elif akc_field_type == "number":
            # We allow floats to be null, as we don't know what to replace them
            # with.
            if value is None:
                akc_value = None
            else:
                akc_value = float(value)
        else:
            if self.verbose():
                print("Info: Unable to convert field %s = %s (%s, %s, %s), not converted"%
                      (field, value, airr_field_type, akc_field_type, type(value)))
         
        #print("Info: Converting field %s (%s -> %s)"%(field, value, akc_value))
        return akc_value

    # Utility function to check to see if a given value is a valid type for a specific
    # AIRR field.  If doing strict AIRR checks, if the field is not an AIRR field then
    # it returns FALSE. If not doing strict AIRR checks, then it doesn't do any checks
    # against the the field if it isn't an AIRR field (it returns TRUE).
    def validAIRRFieldType(self, key, value, strict):
        field_type = self.getAIRRMap().getMapping(key, self.getAIRRTag(),
                               "airr_type", self.getAIRRMap().getRepertoireClass())
        field_nullable = self.getAIRRMap().getMapping(key, self.getAIRRTag(),
                               "airr_nullable", self.getAIRRMap().getRepertoireClass())
        is_array = self.getAIRRMap().getMapping(key, self.getAIRRTag(),
                               "airr_is_array", self.getAIRRMap().getRepertoireClass())
        # If we are not doing strict typing, then if the key is not an AIRR
        # key (field_type == None) then we return True. This allows us to
        # check AIRR keys only and skip non-AIRR keys. If strict checking is
        # on, then if we find a non-AIRR key, we return False, as this is
        # checking AIRR typing explicitly, not typing in general.
        if field_type is None:
            if strict: return False
            else: return True

        # If the value is null and the field is nullable or there is no nullable
        # entry in the AIRR mapping (meaning NULL is OK) then return True.
        if (not isinstance(value, (list))and
            pd.isnull(value) and
            (field_nullable == None or field_nullable)):
            return True

        # If we get here, we have an AIRR field, so no matter what we
        # return False if the type doesn't match.
        valid_type = False
        if isinstance(value, (str)) and field_type == "string":
            valid_type = True
        elif isinstance(value, (bool,np.bool_)) and field_type == "boolean":
            valid_type = True
        elif isinstance(value, (int,np.integer)) and field_type == "integer":
            valid_type = True
        elif isinstance(value, (float,int,np.floating,np.integer)) and field_type == "number":
            # We need to accept integers and floats as numbers.
            valid_type = True
        elif isinstance(value, (list)) and is_array:
            # List is a special case, we only have arrays of strings.
            # Iterate and check each value
            valid_type = True
            for element in value:
                if not self.validAIRRFieldType(key, element, strict):
                    valid_type = False

        if self.verbose():
            if not isinstance(value, (list)) and pd.isnull(value):
                print("Info: Field %s type ERROR, null value, field is non-nullable"%
                      (key))
            elif not valid_type:
                print("Info: Field %s type ERROR, expected %s, got %s"%
                      (key, field_type, str(type(value))))
        return valid_type

    # Set the AKC related attributes for the field dictionary given the 
    # airr_field value.
    def setAKCAttr(self, field_dict, airr_field, akc_field, airr_class):
        field_dict['akc_field'] = akc_field
        field_dict['akc_class'] = self.getAIRRMap().getMapping(airr_field, 'airr',
                                                               'akc_class', airr_class)
        field_dict['akc_form'] = self.getAIRRMap().getMapping(airr_field, 'airr',
                                                              'akc_form', airr_class)
        field_dict['akc_type'] = self.getAIRRMap().getMapping(airr_field, "airr",
                                                              "akc_type", airr_class)
        field_dict['akc_is_array'] = self.getAIRRMap().getMapping(airr_field, "airr",
                                                              "akc_is_array", airr_class)
        field_dict['akc_convert'] = self.getAIRRMap().getMapping(airr_field, "airr",
                                                              "akc_convert", airr_class)
        return field_dict

    # This method is a recursive function that takes a key and value in a JSON
    # object and recursively flattens the values adding each element to the dictionary
    # as it finds a "leaf node". Note a leaf node in general is a key value pair where
    # the value is not a compoud object (not a dict or a list). If it is not a leaf node
    # then the function recurses on all of the elements in the dict or list. Note that
    # a leaf node is a bit complex and specialized based on both the AIRR spec and how
    # they are represented in the AKC.
    #
    # Each leaf node for a field is represented in the repertoire dictionary as follows:
    # {
    #   "study_id":
    #   {
    #     "value":"enrollment",
    #     "airr_subclass":"Subject",
    #     "akc_class":"Participant",
    #     "akc_field":"age_event"
    #     "akc_form":"Class"
    #     "akc_type":"LifeEvent"
    #   }
    # }
    def akc_flatten(self, key, value, dictionary, key_path, airr_class, append=False):
        column = self.getAIRRTag()
        # If it is an integer, float, or bool we just use the key value pair.
        if isinstance(value, (int, float, bool)):
            if self.validAIRRFieldType(key, value, False):
                # Map the field and if it exists as an akc_field, process it.
                akc_field = self.getAIRRMap().getMapping(key, "airr", "akc_field", airr_class)
                field_dict = dict()
                field_dict['value'] = value
                field_dict['airr_subclass'] = self.getAIRRMap().getMapping(key,
                                                  "airr", "ir_subclass", airr_class)
                if not akc_field is None and value != '':
                    # For each field we create a dictionary that has the value,
                    # the AKC class/object, and the AKC field name.
                    field_dict = self.setAKCAttr(field_dict, key, akc_field, airr_class)

                # Store the field dictionary keyed on the key.
                dictionary[key] = field_dict
            else:
                raise TypeError("AIRR type error for " + key)
        # If it is a string we just use the key value pair.
        elif isinstance(value, str):
            if self.validAIRRFieldType(key, value, False):
                # Map the field and if it exists as an akc_field, process it.
                akc_field = self.getAIRRMap().getMapping(key, "airr", "akc_field", airr_class)

                # Check to see if the key is in the dictionary.
                if key in dictionary:
                    field_dict = dictionary[key]
                    # If we are appending, we want to add to the list already there.
                    # If not, then we have an error situation that warrants a warning.
                    # This is an error because we should never have multiple definitions
                    # of a field in a single repertoire except in append mode (array).
                    if append:
                        field_dict['value'].append(value)
                        print('Info: Appending array field %s = %s'%(key, field_dict['value']))
                    else:
                        print('Warning: Field %s already in dictionary, ignoring %s'%(key, value))
                else:
                    field_dict = dict()
                    # If we are appending, the field is an array so create a list
                    # with one element, otherwise just assign the value.
                    if append:
                        field_dict['value'] = [value]
                        print('Info: New array field %s = %s'%(key, field_dict['value']))
                    else:
                        field_dict['value'] = value

                # Track the AIRR subclass of the field.
                field_dict['airr_subclass'] = self.getAIRRMap().getMapping(key,
                                                  "airr", "ir_subclass", airr_class)

                # If the AKC field is valid, set up the AKC attribute information.
                if not akc_field is None and value != '':
                    # For each field we create a dictionary that has the value,
                    # the AKC class/object, and the AKC field name.
                    field_dict = self.setAKCAttr(field_dict, key, akc_field, airr_class)

                # Store the field dictionary keyed on the key.
                dictionary[key] = field_dict
            else:
                raise TypeError("AIRR type error for " + key)
        elif isinstance(value, dict):
            # We need to handle the AIRR ontology terms. Ontologies have two fields in
            # their dictionary, a value and an id.
            if 'label' in value and 'id' in value:
                # In an ontology, the dictionary contains two fields, a value and an id.
                # We store this in the AKC as is for now.
                value_key = key
                id_key = key+"_id"

                # Check types of both the value and the id, convert the data type, and
                # add to the dictionary.
                if (self.validAIRRFieldType(value_key, value['label'], False) and
                            self.validAIRRFieldType(id_key, value['id'], False)):
                    # Map the field and if it exists as an akc_field, process it.
                    akc_field = self.getAIRRMap().getMapping(key, "airr", "akc_field", airr_class)
                    field_dict = dict()
                    field_dict['value'] = value
                    field_dict['airr_subclass'] = self.getAIRRMap().getMapping(key,
                                                      "airr", "ir_subclass", airr_class)
                    if not akc_field is None and value != '':
                        # For each field we create a dictionary that has the value,
                        # the AKC class/object, and the AKC field name.
                        field_dict = self.setAKCAttr(field_dict, key, akc_field, airr_class)

                    # Store the field dictionary keyed on the key.
                    dictionary[key] = field_dict
                else:
                    raise TypeError(key)
            else:
                # If we aren't processing an ontology term, we recursively flatten
                for sub_key, sub_value in value.items():
                    self.akc_flatten(sub_key, sub_value, dictionary,
                                     key_path + "." + sub_key, airr_class)
        elif isinstance(value, list):
            # There are currently three possible list situations in the spec.
            # - keywords_study, data_processing_files: An array of strings
            #   that should be concatenated
            # - diagnosis: We only support one per repertoire. Warn and continue with 1st
            # - pcr_target: We only support one per repertoire. Warn and continue with 1st
            # - data_processing: We only support one per repertoire. Warn and continue
            #   with 1st data processing

            # We flatten this explicitly as a special case. We want to store the list
            # of strings.
            if key == "keywords_study" or key == "data_processing_files" or key == "germline_alleles":
                # TODO: Need to implement type checking on this field...

                if self.validAIRRFieldType(key, value, False):
                    # Map the field and if it exists as an akc_field, process it.
                    akc_field = self.getAIRRMap().getMapping(key, "airr", "akc_field", airr_class)
                    field_dict = dict()
                    field_dict['value'] = value
                    field_dict['airr_subclass'] = self.getAIRRMap().getMapping(key,
                                                      "airr", "ir_subclass", airr_class)
                    if not akc_field is None and value != '':
                        # For each field we create a dictionary that has the value,
                        # the AKC class/object, and the AKC field name.
                        field_dict = self.setAKCAttr(field_dict, key, akc_field, airr_class)

                    # Store the field dictionary keyed on the key.
                    dictionary[key] = field_dict
                else:
                    raise TypeError(key)
            elif key == "data_processing":
                # If we are handling a data processing element list, we have a hint as
                # to which element is the most important, as we can use the
                # "primary_annotation" field to determine which one to use.
                # Warn if we found more than one, as we only store one per repertoire. If
                # you have more than one and want to store the rearrangements separately
                # then you need to split this up into two repertoires.
                if len(value) > 1:
                    print("Warning: Found more than one %s element (found %d)."%
                          (key, len(value)))
                # Look for the primary annotation
                got_primary = False
                for element in value:
                    if 'primary_annotation' in element and element['primary_annotation']:
                        # If we found it, flatten it and the break out of the loop
                        for sub_key, sub_value in element.items():
                            self.akc_flatten(sub_key, sub_value, dictionary,
                                             key_path + "." + sub_key, airr_class)
                        got_primary = True
                        if self.verbose():
                            print("Info: Found a primary annotation, using it.")
                        break
                # If we didn't find the primary, then use the first one as a best guess.
                if not got_primary:
                    print("Warning: Could not find a primary annotation, using the first one.")
                    for sub_key, sub_value in value[0].items():
                            self.akc_flatten(sub_key, sub_value, dictionary,
                                             key_path + "." + sub_key, airr_class)
            elif key == "pcr_target":
                # For pcr_target, we have a class with a set of leaf nodes. We want to
                # create an array for each leaf node that contains the constituent parts.
                # So an array of pcr_targets with pcr_target_locus of TRA and TRB 
                # becomes pcr_target_locus ['TRA','TRB']
                if self.verbose():
                    print("Info: Found a PCRTarget array.")
                for element in value:
                    for sub_key, sub_value in element.items():
                        self.akc_flatten(sub_key, sub_value, dictionary,
                                         key_path + "." + sub_key, airr_class, True)

            else:
                # Process the array of objects as indivdual objects.
                if len(value) > 1:
                    if self.verbose():
                        print("Info: Processing multi element array key %s."%(key))
                # We should only have arrays of objects here. Special case AIRR
                # arrays are handled above. So we should only have an array of 
                # dictionaries here.
                if isinstance(value[0], dict):
                    for element in value:
                        for sub_key, sub_value in element.items():
                            self.akc_flatten(sub_key, sub_value, dictionary, key_path + "." + sub_key, airr_class)
                else:
                    print("Warning: Skipping non-AIRR multi element array %s."%(key))

        return dictionary


    #####################################################################################
    # Hide the internal use of temporary folders from the subclasses
    #####################################################################################

    # Utility methods to deal with data and scratch folders that all Parsers need.
    def getDataFolder(self, fileWithPath):
        # Data folder is based on the path to the file.
        data_dir = os.path.dirname(fileWithPath)
        # If there is no path, then the data directory is the current directory.
        if (not os.path.isdir(data_dir)):
            data_dir = "."
        return data_dir

    # We create a specific temporary 'scratch' folder for each sequence archive
    def setScratchFolder(self, fileWithPath, fileName):
        folderName = fileName[:fileName.index('.')]
        self.scratchFolder = self.getDataFolder(fileWithPath) + "/tmp_" + str(os.getpid()) + "_" + folderName + "/"

    # Get the folder
    def getScratchFolder(self):
        return self.scratchFolder

    # Get the folder with the filename appended.
    def getScratchPath(self, fileName):
        return join(self.getScratchFolder(), fileName)


    #####################################################################################
    # Hide the internal implementation of performing timing functions.
    #####################################################################################

    @staticmethod
    def getDateTimeNowUTC():
        # Use AIRR Standard/YAML data-time ISO standard.
        return datetime.now(timezone.utc).isoformat()

