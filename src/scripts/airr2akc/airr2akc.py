# This code is a derivitave of the airr_flatten code found here:
# https://github.com/sfu-ireceptor/sandbox/tree/master/airr-spec-flatten
# and is developed under this license:
# https://github.com/sfu-ireceptor/sandbox/blob/master/LICENSE
import collections
import argparse
import yaml
import sys
# This requires the AIRR python module to be installed.
import airr
from airr.schema import Schema

def processField(field, field_spec, block, required_fields, field_path,
                    airr_class, airr_api_query, airr_api_response,
                    labels, table, verbose, recursive=False):

        # Get the required fields for this schema object
        if verbose:
            print("**** processField: Field = %s\n"%(field))
            print("**** processField: block=%s,path=%s,class=%s,query=%s,respsonse=%s\n"%(block,field_path,airr_class,airr_api_query,airr_api_response))
            print("**** processField: field spec = %s\n"%(field_spec))

        # Create a new dictionary entry for the field.
        field_dict = dict()
        # Set up the basic field mappings for the stanard iReceptor fields.
        field_dict['airr'] = field
        field_dict['airr_spec'] = True
        # If the field is required, set the attribute.
        if field in required_fields:
            field_dict['airr_required'] = True
        else:
            field_dict['airr_required'] = False
        field_dict['ir_class'] = airr_class
        field_dict['ir_subclass'] = block
        field_dict['ir_adc_api_query'] = airr_api_query + field
        field_dict['ir_adc_api_response'] = airr_api_response + field
        field_dict['airr_is_array'] = False
        field_tag = field_dict['ir_adc_api_query']+"_"+airr_class+"_"+block

        if verbose:
            print("**** processField: Field spec for %s = %s\n"%(airr_api_query+field,field_spec))
        # We want to append a field to our table of fields in only those
        # cases where the field is actually a leaf node in the "tree" of the spec.
        # By default, we assume we want to add the field.
        append = True
        # If the field is a $ref to another object, then it is not a field in and
        # of itself that we will refer to in the AIRR config file. We later recurse
        # on the $ref object, to pick up all of the fields within the $ref. The one special
        # case to this is if the $ref is to the AIRR Ontology object, for which we
        # have to do some special processing.
        if '$ref' in field_spec and not field_spec['$ref'] == "#/Ontology":
            append = True
            label = 'airr_type'
            schema_ref = field_spec['$ref']
            schema = schema_ref.split('/')[1]
            field_dict[label] = schema
            if verbose:
                print("**** processField: No append for $ref - %s\n"%(field_tag))
        # If the field is an array of objects (the items for the array contain
        # objects of or multiple fields (allOf)) then we recurse on the $ref objects
        # and we don't want to add this field to our final field table. If it an array
        # of basic types (integer, string) then we do want to add it to the field table.
        if 'type' in field_spec and field_spec['type'] == 'array':
            if '$ref' in field_spec['items']:
                if recursive:
                    append = False
                else:
                    field_dict['airr_is_array'] = True
                    label = 'airr_array_schema'
                    if not label in labels:
                        labels.append(label)
                    # Add the value of the $ref object to the dictionary
                    schema_ref = field_spec['items']['$ref']
                    schema = schema_ref.split('/')[1]
                    field_dict[label] = schema
                    append = True
                if verbose:
                    print("**** processField: No append for arrays of $ref - %s\n"%(field_tag))
            elif 'allOf' in field_spec['items'] or ('type' in field_spec['items'] and field_spec['items']['type'] == 'object'):
                if recursive:
                    append = False
                else:
                    append = True
                if verbose:
                    print("**** processField: No append for arrays of $ref - %s\n"%(field_tag))
            else:
                field_dict['airr_is_array'] = True
        # If the field is an object then we recurse on the object's fields and we don't
        # want to add this field to our field table.
        if 'type' in field_spec and field_spec['type'] == 'object':
            append = False
            if verbose:
                print("**** processField: No append for objects - %s\n"%(field_tag))

        # Finally, if append == True then we are processing a field and we need to add
        # it to the field table.
        if append:    
            # Add the field to the table.
            if verbose:
                print("**** processField: Adding dict for field_tag = %s\n"%(field_tag))
                print("**** processField: Adding dict for ir_adc_api_query = %s\n"%(field_dict['ir_adc_api_query']))
            table[field_tag] = field_dict
        else:
            if verbose:
                print("**** processField: NOT Adding dict for field_tag = %s\n"%(field_tag))

        # Iterate over the fields specs as required to set the fields attributes.
        for k,v in field_spec.items():
            if verbose:
                print("**** processField: Field = %s,%s\n"%(k,v))
            # A field in the AIRR specification either has "normal" field specs
            # such as type, description, and example or it has AIRR specific field
            # specifications in a custom x-airr object. This custom object has things
            # about the MiAIRR standard and the ADC API. We have to handle both.

            # All fields are by default nullable so we set xairr_nullable here.
            field_dict['airr_nullable'] = True
            # Make sure it is in the labels.
            if not 'airr_nullable' in labels:
                labels.append('airr_nullable')
            # Handle the x-airr schema objects
            if k == 'x-airr':
                # Iterated over the x-airr schema objects.
                for xairr_k, xairr_v in v.items():
                    # If it is an ontology object, record the ID and label
                    if xairr_k == 'ontology':
                        label = 'airr_ontology_top_id'
                        if not label in labels:
                            labels.append(label)
                        # Add the value of this field to the column.
                        field_dict[label] = xairr_v['top_node']['id']

                        label = 'airr_ontology_top_label'
                        if not label in labels:
                            labels.append(label)
                        # Add the value of this field to the column.
                        field_dict[label] = xairr_v['top_node']['label']
                    # The miairr tag is a controlled vocabulary of "essential",
                    # "important", or "defined". It controls the setting of two
                    # columns in the mapping, airr_miairr and airr_required.
                    elif xairr_k == 'miairr':
                        # The miairr tag is a controlled vocabulary of "essential",
                        # "important", or "defined". If this field exists and is 
                        # set to one of these, then the airr_miairr label should be
                        # set to True as it is a MiAIRR field. If it isn't one of these
                        # values then it is an error.
                        if xairr_v in ['essential', 'important', 'defined']:
                            label = 'airr_miairr'
                            if not label in labels:
                                labels.append(label)
                            # Add the value of this field to the column.
                            field_dict[label] = True
                        else:
                            print("Warning: Invalid x_airr:miairr field %s"%(xairr_v))
                    # AIRR nullable is by default true, so we set overwrite the default
                    # if we get a value here.
                    elif xairr_k == 'nullable':
                        if xairr_v == False:
                            field_dict['airr_nullable'] = False
                    else:
                        # If it is a string value, we want to clean it up, in case
                        # there is some extra white space...
                        value = xairr_v
                        if isinstance(value, str):
                            value = value.strip()
                        # Create a new label for this field, as we want to keep track
                        # of this as a column in our table. We prefic all of the AIRR
                        # columns with airr_ to differentiate them.
                        label = 'airr_'+xairr_k
                        # Only add it if it isn't in the labels already.
                        if not label in labels:
                            labels.append(label)
                        # Add the value if this field to the column.
                        field_dict[label] = value
            else:
                # We are processing normal YAML spec fields.
                if k == '$ref':
                    # Handle a $ref field to another object
                    if v == "#/Ontology":
                        # If the $ref is to an Ontology, mark the type as ontology.
                        field_dict["airr_type"] = "ontology"
                        # We want to add on a .value qualifier to the ADC API variable
                        # names as we return the value component of the ontology in
                        # the API.
                        field_dict['ir_adc_api_query'] = field_dict['ir_adc_api_query'] + '.label'
                        field_dict['ir_adc_api_response'] = field_dict['ir_adc_api_response'] + '.label'
                        # For ontology fields, we need to create a second entry for
                        # the id component of the ontology.
                        # Create a new dictionary entry for the id field.
                        #id_dict = dict()
                        # Set up the basic field mappings for the iReceptor fields.
                        #id_dict['airr'] = field + "_id"
                        #id_dict['ir_class'] = airr_class
                        #id_dict['ir_subclass'] = block
                        # Create the .id qualifier for the API names.
                        #id_dict['ir_adc_api_query'] = airr_api_query + field + ".id"
                        #id_dict['ir_adc_api_response'] = airr_api_response + field + ".id"
                        #id_dict['airr_is_array'] = False
                        #id_dict['airr_type'] = "string"
                        #id_field_tag = id_dict['airr']+airr_class+block
                        #id_field_tag = id_dict['ir_adc_api_query']+"_"+airr_class+"_"+block
                        #if verbose:
                        #    print("**** processField: Adding dict for field_tag = %s\n"%(field_tag))
                        #    print("**** processField: Adding dict for ir_adc_api_query = %s\n"%(id_dict['ir_adc_api_query']))
                        #table[id_field_tag] = id_dict
                    else:
                        # If the $ref is to another object, then handle that object by
                        # recursion. We get the object to use from the name.
                        ref_array = v.split("/")
                        new_schema_name = ref_array[1]
                        # We recurse on the new schema block, making sure that we track
                        # that we are processing a new object and that the API field 
                        # references need to reference the hierarchy correctly. 
                        if recursive:
                            labels, table = extractBlock(new_schema_name, airr_class,
                                             airr_api_query+field_dict['airr']+'.',
                                             airr_api_response+field_dict['airr']+'.',
                                             labels, table, verbose, recursive)
                elif k == 'items':
                    # Handle a list of items, meaning we have an array. In the AIRR
                    # specification we can have an array of $ref objects or an
                    # "allOf" directive of $ref objects or a an actual object,
                    # which means we have to process each element.
                    
                    if "type" in v and v["type"] == "object":
                        properties = v["properties"]
                        if verbose:
                            print("**** processField: PROPERTIES2 = %s\n"%(properties))
                        for prop_k,prop_v in properties.items():
                            if verbose:
                                print("**** processField: field, value = %s,%s\n"%(prop_k,prop_v))
                            # Note the API response has a .0. in it because this
                            # is an array.
                            labels, table = processField(prop_k, prop_v, block, required_fields,
                                                      field,
                                                      airr_class,
                                                      airr_api_query+field+".",
                                                      airr_api_response+field+".0.",
                                                      labels, table, verbose, recursive)
                    for item_key, item_value in v.items():
                        if item_key == '$ref':
                            # The item is a $ref, get the sub-object and process it.
                            ref_array = item_value.split("/")
                            new_schema_name = ref_array[1]
                            # Note the API response has a .0. in it because this
                            # is an array.
                            if recursive:
                                labels, table = extractBlock(new_schema_name, airr_class,
                                            airr_api_query+field_dict['airr']+'.',
                                            airr_api_response+field_dict['airr']+'.0.',
                                            labels, table, verbose, recursive)
                        elif item_key == 'allOf':
                            # The item is an allOf so process each element.
                            for ref_dict in item_value:
                                # The item is a $ref, get the sub-object and process it.
                                if '$ref' in ref_dict:
                                    ref_array = ref_dict['$ref'].split("/")
                                    new_schema_name = ref_array[1]
                                    # Note the API response has a .0. in it because
                                    # this is an array.
                                    if recursive:
                                        labels, table = extractBlock(new_schema_name,
                                               airr_class,
                                               airr_api_query+field_dict['airr']+'.',
                                               airr_api_response+field_dict['airr']+'.0.',
                                               labels, table, verbose, recursive)
                        elif item_key == 'type':
                            # This is the special case of handling a "type" for an "array". 
                            # The only arrays that have a type are array fields. If this
                            # is the case, we want to set the type of the array field.
                            # First add it to the labels if we don't already have it.
                            label = 'airr_type'
                            if not label in labels:
                                labels.append(label)
                            # Strip off any whitespace if it is a string...
                            value = item_value 
                            if isinstance(v, str):
                                value = v.strip()
                            field_dict[label] = value
                elif k == 'example':
                    # Processing an example - some special cases...
                    # First add it to the labels if we don't already have it.
                    label = 'airr_'+k
                    if not label in labels:
                        labels.append(label)
                    if isinstance(v,dict):
                        # If it is a dict() then we have an ontology term, process
                        # the ID and value for the ontology.
                        field_dict[label] = str(v['id']) + ', ' + v['label']
                    elif not isinstance(v, str):
                        # If it isn't a string, store it
                        field_dict[label] = v
                    else:
                        # If it is a string, then we want to strip it in case it has
                        # odd white space...
                        field_dict[label] = v.strip()
                elif k == 'enum':
                    # First add it to the labels if we don't already have it.
                    label = 'airr_'+k
                    if not label in labels:
                        labels.append(label)
                    # Handle the enum case, where we concatenante the enum fields so
                    # we can track them.
                    value = ''
                    enum_len = len(v)
                    count = 0
                    # Iterate over the enum values and add them to a string.
                    for enum_val in v:
                        if count > 0: 
                            # We need to handle none as this is now a possible
                            # enum value.
                            if enum_val is None:
                                enum_val = 'null'
                            value = value + ',' + str(enum_val)
                        else:
                            value = str(enum_val)
                        count = count + 1
                    field_dict[label] = value
                elif k == 'properties':
                    if verbose:
                        print("**** processField: PROPERTIES = %s,%s\n"%(k,v))
                    for prop_k,prop_v in v.items():
                        if verbose:
                            print("**** processField: field, value = %s,%s\n"%(prop_k,prop_v))
                        labels, table = processField(prop_k, prop_v, block, required_fields,
                                                  field,
                                                  airr_class,
                                                  airr_api_query+field+".",
                                                  airr_api_response+field+".",
                                                  labels, table, verbose, recursive)
                else:
                    if verbose:
                        print("**** processField: key, value = %s,%s\n"%(k,v))
                    # If we get here, we are processing "normal" fields...
                    # First add it to the labels if we don't already have it.
                    label = 'airr_'+k
                    if not label in labels:
                        labels.append(label)
                    # Strip off any whitespace if it is a string...
                    value = v
                    if isinstance(v, str):
                        value = v.strip()
                    field_dict[label] = value

        # We are done, return the labels and the table.
        return labels, table

# Recursive function to extract fields from a AIRR YAML specification into a
# flat table. The function processes all $ref objects recursively to build up
# a table of entries with all fields from all sub-objects in the YAML definition.
#
# Parameters:
# - block: The schema block to extract.
# - airr_class: The airr class field. For iReceptor this stays constant through the
#   hierarchy, and is either "repertoire" or "rearrangement"
# - airr_api_query: The hierarchical tag for the AIRR API query. This is essentially
#   the query field that the API requires (e.g. study.study_id) and is built as we 
#   traverse the heirarchy of the Repertoire object.
# - airr_api_response: The hierarchical tag for the AIRR API response. This tells us
#   the hierarchy of the object that this field needs to go in. It is similar to
#   airr_api_query except for those objects that are arrays they are denoted with a
#   .0. string (e.g. sample.0.sample_id denotes that sample_id is part of the sample
#   array response.
# - labels: An array of labels that have been found thus far in the query. When
#   a new label is found it should be added to the labels array.
# - table: An array of dictionaries, each row in the table is a field in the spec, and
#   each dictionary a key value pair where the labels are the keys and the values
#   are the field values for those labels. 
#
# Returns:
# - labels: A new set of labels based on the labels provided plus any
# added by the current object.
# - table: An array of dictionaries, based on the table provided but with
# new rows added as per the fields that were found in the current object.

def extractBlock(block, airr_class, airr_api_query, airr_api_response, labels, table, verbose, recursive=False):

    if verbose:
        print("#### extractBlock %s\n"%(block))
    # Use the AIRR library to get an AIRR Schema block for the current block.
    try:
        schema = Schema(block)
    except Exception as e:
        print(e)
        # Return an empty set of labels and an empty dictionary.
        sys.exit(1)

    if verbose:
        print("#### got a schema\n")

    # Get the required fields for this schema object
    required_fields = schema.required

    # For each field in the schema, process it
    for field in schema.properties:
        if verbose:
            print("#### extractBlock: processing property field %s\n"%(field))
        field_spec = schema.properties[field]
        if verbose:
            print("#### extractBlock: field spec %s\n"%(field_spec))
        labels, table = processField(field, field_spec, block, required_fields,"",
                                     airr_class, airr_api_query, airr_api_response,
                                     labels, table, verbose, recursive)

    # We are done, return the labels and the table.
    return labels, table

def getArguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=""
    )

    # The block to process
    parser.add_argument("airr_block")
    # Flag as to whether to process the block recursively
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Process internally referenced objects recursively.")
    # Flag as to whether we generate enums or the basic slots
    parser.add_argument(
        "-e",
        "--enums",
        action="store_true",
        help="Generate LinkML enums rather than slots.")
    # Verbosity flag for debugging
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run the program in verbose mode. This option will generate debug output and may cause a problem with using the config file as a TSV file.")


    # Parse the command line arguements.
    options = parser.parse_args()
    return options

def convertCamelCase(word):
    # Change _ to camel case as per LinkML naming. _ _ replaced with _
    new_word = ''.join('_' if x == '' else x.capitalize() for x in word.split('_'))
    return new_word

if __name__ == "__main__":
    # Get the command line arguments.
    options = getArguments()

    # Create an empty table. This gets populated by the traversal of the YAML block
    # that is processed.
    table = collections.OrderedDict()
    # Create an initial set of lables for the mapping file. These are mappings
    # that don't exist in the YAML file but are needed in the mapping file.
    labels = ['airr', 'airr_spec', 'airr_required', 'ir_class', 'ir_subclass',
              'ir_adc_api_query', 'ir_adc_api_response', 'airr_is_array']
    initial_labels = ['airr', 'ir_class', 'ir_subclass',
                      'ir_adc_api_query', 'ir_adc_api_response', 'airr_is_array']
    # Recursively process the block provided. This will recursively process any
    # $ref entries in the YAML and build correct entries for each field.
    labels, table = extractBlock(options.airr_block, options.airr_block,
                                 '', '', labels, table,
                                 options.verbose, options.recursive)

    # We need to do some special processing for our ontologies. The _id field of 
    # the ontology does not have an entry in the spec, so we need to copy a bunch
    # of values from the _value field to the _id field.
    for field, field_dict in table.items():
        #if field_dict['airr_type'] == 'ontology':
        if False:
            # Get the field name and generate the ontology id field name
            field = field_dict['airr']
            id_field = field + "_id"
            label_base_tag = field_dict['ir_adc_api_query']
            id_base_tag = label_base_tag.replace("label", "id")
            id_field_tag = id_base_tag+"_"+field_dict['ir_class']+"_"+field_dict['ir_subclass']
            if options.verbose:
                print("$$$$ Ontology term %s, %s, %s"%(field, id_field, id_field_tag))
                #print(table)
            # We want this field to be type string not ontology.
            field_dict['airr_type'] = 'string'
            # If the id field is in the table, update the id fields column values
            if id_field_tag in table:
                if options.verbose:
                    print("$$$$ Ontology ID field %s"%(id_field))
                # Get the dictionary for the id_field
                id_dict = table[id_field_tag]
                # For each column in the value field, copy it to the id field. Note
                # we do this for all of the generated fields from the spec, not the
                # special fields that are generated.
                for column in field_dict:
                    # Initial labels contains the special fields, we don't want
                    # to overwrite these.
                    if not column in initial_labels:
                        id_dict[column] = field_dict[column]
                        # We want to add some info to the ID description/name/title fields.
                        if column == "airr_description" or column == "airr_name" or column == "airr_title":
                            id_dict[column] = id_dict[column] + " (Ontology ID)"
                # We want the type of the id field to be string.
                id_dict['airr_type'] = 'string'
                # We want the airr_spec field to be TRUE.
                id_dict['airr_spec'] = True
                # Finally, we store the updated dict in the table.
                if options.verbose:
                    print("$$$$ Updating dict for field_tag = %s\n"%(id_field_tag))
                table[id_field_tag] = id_dict

    # Once we have our table built, we need to print it out.
    if options.verbose:
        # Print out the header labels.
        for label in labels:
            print(label,end='\t')
        print("")

    # Now print out the definition of the object and its slots
    if not options.enums:
        print('id: https://github.com/airr-knowledge/ak-schema')
        print('name: ak-schema')
        print('')
        print('classes:')
        print('  %s:'%(options.airr_block))
        print('    slots:')
        for field, field_dict in table.items():
            if 'airr' in field_dict:
                if not options.enums:
                    print('      - %s'%(field_dict['airr']))

        print('')
        print('slots:')
                
    # Now print out the definition for each slot
    for field, field_dict in table.items():
        # For each row, generate a LinkML specification for the field
        if 'airr' in field_dict:
            if options.enums:
                range_name = convertCamelCase(field_dict['airr'])
                if 'airr_enum' in field_dict and 'airr_format' in field_dict and field_dict['airr_format'] == 'controlled_vocabulary':
                    print('%s:'%(range_name))
                    print('  name: %s'%(range_name))
                    print('  permissible_values:')

                    enum_array = field_dict['airr_enum'].split(',')
                    for enum_str in enum_array:
                        print('    %s:'%(enum_str))
                if 'airr_format' in field_dict and field_dict['airr_format'] == 'ontology':
                    print('%s:'%(range_name))
                    print('  name: %s'%(range_name))
                    print('  permissible_values:')
                    if 'airr_ontology_top_id' in field_dict:
                        print('    %s:'%(field_dict['airr_ontology_top_label']))
                        print('      text: %s'%(field_dict['airr_ontology_top_label']))
                        print('      meaning: %s'%(field_dict['airr_ontology_top_id']))
                    elif 'airr_example' in field_dict:
                        ontology_example_array = field_dict['airr_example'].split(',')
                        print('    %s:'%(ontology_example_array[1]))
                        print('      text: %s'%(ontology_example_array[1]))
                        print('      meaning: %s'%(ontology_example_array[0]))

            else:
                if options.verbose:
                    print(field_dict)
                print('  %s:'%(field_dict['airr']))
                print('    name: %s'%(field_dict['airr']))
                if 'airr_description' in field_dict:
                    print('    description: %s'%(field_dict['airr_description']))

                # Handle the range, this is a bit complex depending on the field.
                if 'airr_format' in field_dict and field_dict['airr_format'] == 'ontology':
                    print('    range: %s'%(convertCamelCase(field_dict['airr'])))
                elif 'airr_format' in field_dict and field_dict['airr_format'] == 'controlled_vocabulary':
                    range_name = convertCamelCase(field_dict['airr'])
                    print('    range: %s'%(range_name))
                elif 'airr_is_array' in field_dict and field_dict['airr_is_array'] == True:
                    if 'airr_array_schema' in field_dict:
                        print('    range: %s'%(field_dict['airr_array_schema']))
                    print('    multivalued: true')
                elif 'airr_type' in field_dict:
                    print('    range: %s'%(field_dict['airr_type']))

                # Print out some x-airr attributes if required.
                if 'airr_required' in field_dict:
                    print('    required: %s'%(field_dict['airr_required']))
                if 'airr_nullable' in field_dict:
                    print('    annotations:')
                    print('      nullable: %s'%(field_dict['airr_nullable']))
                if 'airr_identifier' in field_dict:
                    print('    identifier: %s'%(field_dict['airr_identifier']))
                print('')

        
        #for label in labels:
        #    # If the label is in the row, print the info, otherwise print an
        #    # empty tab column. The end of our print isn't a new line, it is a
        #    # tab character, so we stay on the same row.
        #    if label in field_dict:
        #        print(field_dict[label], end='\t')
        #    else:
        #        print("", end='\t')

    # We are done, return success
    sys.exit(0)

