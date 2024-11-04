# This code is developed under this license:
# https://github.com/sfu-ireceptor/sandbox/blob/master/LICENSE

import argparse
import yaml

def getArguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="")

    # The block to process
    parser.add_argument("-a", "--airr_schema_yaml", type=str, default="/Users/lscheffer/PycharmProjects/ak-schema/src/scripts/airr2akc/airr-schema-openapi3.yaml")
    parser.add_argument("-o", "--output_folder", type=str, default="../../ak_schema/schema/airr")
    parser.add_argument("-k", "--keywords_to_parse", type=str, nargs="+")

    return parser.parse_args()


def convertCamelCase(word):
    # Change _ to camel case as per LinkML naming. _ _ replaced with _
    new_word = ''.join('_' if x == '' else x.capitalize() for x in word.split('_'))
    return new_word


def getSlotRange(slot_name, slot_yaml):
    # if "x-airr" in slot_yaml and "format" in slot_yaml["x-airr"] and slot_yaml["x-airr"]["format"] not in ("ontology", "controlled_vocabulary"):
    #     pass

    # if this is an array, get the type of the 'items' in the array
    if "type" in slot_yaml and slot_yaml["type"] == "array":
        slot_range = getSlotRange(slot_name, slot_yaml["items"])
    elif "enum" in slot_yaml:
        slot_range = convertCamelCase(slot_name)
    elif "$ref" in slot_yaml:
        if slot_yaml["$ref"] == "#/Ontology":
            slot_range = convertCamelCase(slot_name)
        else:
            slot_range = slot_yaml["$ref"].lstrip("#/")
    elif "type" in slot_yaml and slot_yaml["type"] in ("string", "float", "integer", "boolean", "number"):
        slot_range = slot_yaml["type"]
    # elif "x-airr" in slot_yaml and "format" in slot_yaml["x-airr"]:
    #     slot_range = slot_yaml["x-airr"]["format"]  #
    elif "type" in slot_yaml and slot_yaml["type"] == "object":
        # todo only occurs once in RepertoireGroup
        slot_range = slot_yaml["type"]
    else:
        raise NotImplementedError(slot_yaml)

    if slot_range == "number":
        slot_range = "float"

    return slot_range

def getSlotAnnotation(slot_yaml):
    annotations = dict()

    if "nullable" in slot_yaml:
        annotations["nullable"] = slot_yaml["nullable"]

    if "x-airr" in slot_yaml:
        if "identifier" in slot_yaml["x-airr"]:
            annotations["identifier"] = slot_yaml["x-airr"]["identifier"]
        if "nullable" in slot_yaml["x-airr"]:
            assert "nullable" not in annotations or annotations["nullable"] == slot_yaml["x-airr"]["nullable"], \
                f"Found contradicting values for nullable in: {slot_yaml}"
            annotations["nullable"] = slot_yaml["x-airr"]["nullable"]

    return annotations

def isDeprecated(slot_yaml):
    return "x-airr" in slot_yaml and "deprecated" in slot_yaml["x-airr"] and slot_yaml["x-airr"]["deprecated"] == True

def isArray(slot_yaml):
    return "type" in slot_yaml and slot_yaml["type"] == "array"

def getSlot(slot_name, slot_yaml, required_slots):
    if isDeprecated(slot_yaml):
        return dict()

    slot = {slot_name: {
                "name": slot_name,
                "description": slot_yaml["description"].strip() if "description" in slot_yaml else "",
                "range": getSlotRange(slot_name, slot_yaml)}}

    if isArray(slot_yaml):
        slot[slot_name]["multivalued"] = True

    is_required = slot_name in required_slots
    slot[slot_name]["required"] = is_required

    annotations = getSlotAnnotation(slot_yaml)
    if len(annotations) > 0:
        slot[slot_name]["annotations"] = annotations

    return slot


def getAllSlots(keyword_yaml):
    all_slots = dict()

    required_slots = keyword_yaml["required"] if "required" in keyword_yaml else []

    for slot_name, slot_yaml in keyword_yaml["properties"].items():
        all_slots.update(getSlot(slot_name, slot_yaml, required_slots))

    return all_slots

def getOntologyEnum(name, slot_yaml):
    if "ontology" in slot_yaml["x-airr"]:
        source_nodes = [slot_yaml["x-airr"]["ontology"]["top_node"]["id"]]

        return {"name": name,
                "reachable_from":
                    {"source_nodes": source_nodes,
                     "include_self": True,
                     "relationship_types": ["rdfs:subClassOf"]}} # todo ontology 'Species' has no source node


def getClosedVocabularyEnum(name, slot_yaml):
    return {"name": name,
            "permissible_values": {"null" if enum_val is None else enum_val: None for enum_val in
                                   slot_yaml["enum"]}}  # todo how to deal with 'null'?

def getEnum(name, slot_yaml):
    if "type" in slot_yaml and slot_yaml["type"] == "array":
        return getEnum(name, slot_yaml["items"])

    if "$ref" in slot_yaml and slot_yaml["$ref"] == "#/Ontology":
        return getOntologyEnum(name, slot_yaml)

    elif "enum" in slot_yaml:
        return getClosedVocabularyEnum(name, slot_yaml)



def getAllEnums(keyword_yaml):
    all_enums = dict()

    for slot_name, slot_yaml in keyword_yaml["properties"].items():
        if not isDeprecated(slot_yaml):
            name = convertCamelCase(slot_name)
            new_enum = getEnum(name, slot_yaml)

            if new_enum is not None:
                all_enums[name] = new_enum

    return all_enums


# def getAdditionalKeywords(keyword_yaml):
#     additional_keywords = []
#
#     for slot_yaml in keyword_yaml["properties"].values():
#         if not isDeprecated(slot_yaml):
#             if "$ref" in slot_yaml:
#                 additional_keywords.append(slot_yaml["$ref"].lstrip("#/"))
#             elif "items" in slot_yaml:
#                 if "$ref" in slot_yaml["items"]:
#                     additional_keywords.append(slot_yaml["items"]["$ref"].lstrip("#/"))
#
#     return additional_keywords

def getYamlOutputForKeyword(airr_yaml, keyword):
    yaml_output_dict = {"id": "https://github.com/airr-knowledge/ak-schema",
                        "name": "ak-schema",
                        #"airr_version": airr_yaml["Info"]["version"],
                        "classes": dict(),
                        "slots": dict()}

    keyword_yaml = airr_yaml[keyword]

    output_slots = getAllSlots(keyword_yaml)
    output_enums = getAllEnums(keyword_yaml)

    yaml_output_dict["slots"].update(output_slots)
    yaml_output_dict["classes"] = {keyword: {"slots": list(output_slots.keys())}}

    if len(output_enums) > 0:
        yaml_output_dict["enums"] = output_enums

    return yaml_output_dict

class LinkMLDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        # Custom LinkMLDumper ensures lists are always indented (this is non-default behavior specific to LinkML format)
        return super(LinkMLDumper, self).increase_indent(flow, False)

def writeYamlOutput(yaml_output_dict, yaml_outfile):
    # This line ensures None values (as in {"key1": None, "key2": None}) do not show up as 'null' in YAML output
    # This is specific to LinkML format, not valid standard YAML format
    # it ensures enum values are formatted as follows:
    # permissible_values:
    #   key1:
    #   key2:
    yaml.add_representer(type(None),
                         representer=lambda self, _: self.represent_scalar('tag:yaml.org,2002:null', ''))

    with open(yaml_outfile, "w") as file:
        yaml.dump(yaml_output_dict, file, sort_keys=False, width=float("inf"), default_flow_style=False,
                  Dumper=LinkMLDumper)

def processKeyword(airr_yaml, keyword):
    yaml_output_dict = getYamlOutputForKeyword(airr_yaml, keyword)
    writeYamlOutput(yaml_output_dict, f"{parsed_args.output_folder}/ak_{keyword}.yaml")

def getAirrYaml(file_location):
    with open(parsed_args.airr_schema_yaml) as file:
        airr_yaml = yaml.safe_load(file)
    return airr_yaml

def main(parsed_args):
    airr_yaml = getAirrYaml(parsed_args.airr_schema_yaml)

    skip_keywords = ["Info", "Ontology", "CURIEMap", "InformationProvider", "Attributes", "FileObject", "DataSet",
                     "Manifest", "DataFile", "InfoObject"]
    skip_keywords += ["SampleProcessing"]  # todo special case

    # keywords_to_process = airr_yaml.keys()
    keywords_to_process = parsed_args.keywords_to_parse

    for keyword in keywords_to_process:
        if keyword not in skip_keywords:
            processKeyword(airr_yaml, keyword)

            # keywords_to_parse_recursively.extend(getAdditionalKeywords(airr_yaml[keyword]))
            skip_keywords.append(keyword)


if __name__ == "__main__":
    parsed_args = getArguments()
    main(parsed_args)










# InferenceProcess
#     permissible_values:
#       genomic_sequencing:
#       repertoire_sequencing:
#       'null': # todo: how to deal with 'null'; should quotes be removed?