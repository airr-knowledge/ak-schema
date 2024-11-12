# This code is developed under this license:
# https://github.com/sfu-ireceptor/sandbox/blob/master/LICENSE

import argparse
import yaml
import sys

def get_arguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="")

    # The block to process
    # parser.add_argument("-a", "--airr_schema_yaml", type=str, default="/Users/lscheffer/PycharmProjects/ak-schema/src/scripts/airr2akc/airr-schema-openapi3.yaml")
    parser.add_argument("-a", "--airr_schema_yaml", type=str, default="/Users/lscheffer/PycharmProjects/ak-schema/src/scripts/airr2akc/airr-schema.yaml")
    parser.add_argument("-o", "--output_file", type=str, default="../../ak_schema/schema/ak_airr.yaml")
    # parser.add_argument("-k", "--keywords_to_parse", type=str, nargs="+")

    return parser.parse_args()


def convert_camel_case(word):
    # Change _ to camel case as per LinkML naming. _ _ replaced with _
    new_word = ''.join('_' if x == '' else x.capitalize() for x in word.split('_'))
    return new_word


def get_slot_range(slot_name, slot_yaml, prefix):
    # if this is an array, get the type of the 'items' in the array
    if "type" in slot_yaml and slot_yaml["type"] == "array":
        slot_range = get_slot_range(slot_name, slot_yaml["items"], prefix)
    elif "enum" in slot_yaml:
        slot_range = f"{prefix}{convert_camel_case(slot_name)}"
    elif "$ref" in slot_yaml:
        if slot_yaml["$ref"] == "#/Ontology":
            slot_range = f"{prefix}{convert_camel_case(slot_name)}"
        else:
            slot_range = f"{prefix}{slot_yaml["$ref"].lstrip("#/")}"
    elif "type" in slot_yaml and slot_yaml["type"] in ("string", "float", "integer", "boolean", "number"):
        slot_range = slot_yaml["type"]
    # elif "x-airr" in slot_yaml and "format" in slot_yaml["x-airr"]:
    #     slot_range = slot_yaml["x-airr"]["format"]  #
    elif "type" in slot_yaml and slot_yaml["type"] == "object":
        # todo only occurs once in RepertoireGroup
        slot_range = slot_yaml["type"]
        print(f"Cannot determine range for slot '{slot_name}', omitting range...", file=sys.stderr)
        slot_range = None
    else:
        raise NotImplementedError(slot_yaml)

    if slot_range == "number":
        slot_range = "float" # todo is this ok

    return slot_range

def get_slot_annotation(slot_yaml):
    annotations = dict()

    if "nullable" in slot_yaml:
        annotations["nullable"] = slot_yaml["nullable"]

    if "x-airr" in slot_yaml:
        if "nullable" in slot_yaml["x-airr"]:
            assert "nullable" not in annotations or annotations["nullable"] == slot_yaml["x-airr"]["nullable"], \
                f"Found contradicting values for nullable in: {slot_yaml}"
            annotations["nullable"] = slot_yaml["x-airr"]["nullable"]

    return annotations

def is_deprecated(slot_yaml):
    return "x-airr" in slot_yaml and "deprecated" in slot_yaml["x-airr"] and slot_yaml["x-airr"]["deprecated"] == True

def is_array(slot_yaml):
    return "type" in slot_yaml and slot_yaml["type"] == "array"

def get_slot(slot_name, slot_yaml, required_slots, prefix):
    if is_deprecated(slot_yaml):
        return dict()

    slot = {slot_name: {
                "name": slot_name,
                # todo: deal with 'description' across different classes
                # "description": slot_yaml["description"].strip() if "description" in slot_yaml else "",
                }}

    slot_range = get_slot_range(slot_name, slot_yaml, prefix)
    if slot_range is not None:
        slot[slot_name]["range"] = slot_range

    if is_array(slot_yaml):
        slot[slot_name]["multivalued"] = True

    # todo: deal with 'required' field across different classes
    # is_required = slot_name in required_slots
    # slot[slot_name]["required"] = is_required

    # todo: deal with 'identifier' field across different classes
    # if "x-airr" in slot_yaml and  "identifier" in slot_yaml["x-airr"]:
    #         slot[slot_name]["identifier"] = slot_yaml["x-airr"]["identifier"]

    # todo: deal with 'annotations' (nullable) across different classes
    # annotations = get_slot_annotation(slot_yaml)
    # if len(annotations) > 0:
    #     slot[slot_name]["annotations"] = annotations

    return slot


def get_all_slots(keyword_yaml, prefix) -> dict:
    all_slots = dict()

    required_slots = keyword_yaml["required"] if "required" in keyword_yaml else []

    for slot_name, slot_yaml in keyword_yaml["properties"].items():
        all_slots.update(get_slot(slot_name, slot_yaml, required_slots, prefix))

    return all_slots

def get_ontology_enum(name, slot_yaml, prefix):
    if "ontology" in slot_yaml["x-airr"]:
        source_nodes = [slot_yaml["x-airr"]["ontology"]["top_node"]["id"]]

        return {"name": f"{prefix}{name}",
                "reachable_from":
                    {"source_nodes": source_nodes,
                     "include_self": True,
                     "relationship_types": ["rdfs:subClassOf"]}} # todo ontology 'Species' has no source node
    else:
        # todo bug report: 'Property' ontology does not follow the same format
        print(f"Ontology '{name}' does not follow the correct formatting.\n"
              f"  Expected to find the field: x-airr/ontology/top_node/id\n"
              f"  Instead found these fields: {slot_yaml}", file=sys.stderr)
        return {"name": f"{prefix}{name}"}

def get_closed_vocabulary_enum(name, slot_yaml, prefix):
    return {"name": f"{prefix}{name}",
            "permissible_values": {"null" if enum_val is None else enum_val: None for enum_val in
                                   slot_yaml["enum"]}}  # todo how to deal with 'null'?

def get_enum(name, slot_yaml, prefix):
    if "type" in slot_yaml and slot_yaml["type"] == "array":
        return get_enum(name, slot_yaml["items"], prefix)

    if "$ref" in slot_yaml and slot_yaml["$ref"] == "#/Ontology":
        return get_ontology_enum(name, slot_yaml, prefix)

    elif "enum" in slot_yaml:
        return get_closed_vocabulary_enum(name, slot_yaml, prefix)


def get_all_enums(keyword_yaml, prefix):
    all_enums = dict()

    for slot_name, slot_yaml in keyword_yaml["properties"].items():
        if not is_deprecated(slot_yaml):
            name = convert_camel_case(slot_name)
            new_enum = get_enum(name, slot_yaml, prefix)

            if new_enum is not None:
                all_enums[f"{prefix}{name}"] = new_enum

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

def get_yaml_output_for_keyword(airr_yaml, keyword, prefix):
    keyword_yaml = airr_yaml[keyword]
    output_slots = get_all_slots(keyword_yaml, prefix)

    yaml_output_dict = {"classes": {f"{prefix}{keyword}": {"slots": list(output_slots.keys())}},
                        "slots": output_slots,
                        "enums": get_all_enums(keyword_yaml, prefix)}

    return yaml_output_dict

def new_keys_not_in_existing(existing_keys, new_keys):
    return all([key not in existing_keys for key in new_keys])

# def check_can_safely_add(existing_keys, new_keys, item_name):
#     assert new_keys_not_in_existing(existing_keys, new_keys), \
#         (f"Error when adding new {item_name}, some of these already exist. \n"
#          f"Existing: {existing_keys}\n"
#          f"New: {new_keys}\n"
#          f"Erroneous: {set(existing_keys).intersection(new_keys)}")

def check_can_safely_add(existing_yaml, new_yaml):
    for key in new_yaml:
        if key in existing_yaml:
            if new_yaml[key] != existing_yaml[key]:
                print(f"Issue when attempting to add slot '{key}'. Same slot was already found with different content:\n"
                      f"  Existing: {new_yaml[key]}\n  New:      {existing_yaml[key]}", file=sys.stderr)
            # assert new_yaml[key] == existing_yaml[key]


def safe_update_yaml(output_yaml, keyword_yaml):
    if "classes" in keyword_yaml:
        check_can_safely_add(output_yaml["classes"], keyword_yaml["classes"])
        output_yaml["classes"].update(keyword_yaml["classes"])

    if "slots" in keyword_yaml:
        check_can_safely_add(output_yaml["slots"], keyword_yaml["slots"])
        output_yaml["slots"].update(keyword_yaml["slots"])

    if "enums" in keyword_yaml:
        check_can_safely_add(output_yaml["enums"], keyword_yaml["enums"])
        output_yaml["enums"].update(keyword_yaml["enums"])


def get_airr_yaml(file_location):
    with open(parsed_args.airr_schema_yaml) as file:
        airr_yaml = yaml.safe_load(file)
    return airr_yaml

def get_simple_keywords_to_process(airr_yaml):
    return [key for key, value in airr_yaml.items() if "type" in value.keys()]

def get_composition_keywords_to_process(airr_yaml):
    return [key for key, value in airr_yaml.items() if list(value.keys()) == ["allOf"]]


class LinkMLDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        # Custom LinkMLDumper ensures lists are always indented (this is non-default behavior specific to LinkML format)
        return super(LinkMLDumper, self).increase_indent(flow, False)

    def write_line_break(self, data=None):
        super().write_line_break(data)

        if len(self.indents) == 1:
            super().write_line_break()


def write_yaml_output(yaml_output_dict, yaml_outfile):
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
                  Dumper=LinkMLDumper, explicit_start=True)


def main(parsed_args):
    # skip_keywords = ["Info", "Ontology", "CURIEMap", "InformationProvider", "Attributes", "FileObject", "DataSet",
    #                  "Manifest", "DataFile", "InfoObject"]
    # skip_keywords += ["SampleProcessing", "RepertoireGroup"]  # todo special case
    airr_yaml = get_airr_yaml(parsed_args.airr_schema_yaml)
    airr_version = airr_yaml["Info"]["version"]
    class_prefix = f"AirrV{str(airr_version).replace('.', '_')}_"


    skip_keywords = ["Info", "Ontology", "CURIEMap", "InformationProvider", "Attributes", "FileObject", "DataSet",
                                      "Manifest", "DataFile", "InfoObject"]

    output_yaml = {"id": "https://github.com/airr-knowledge/ak-schema",
                   "name": "ak-schema",
                   #"airr_version": airr_version,
                   "classes": dict(),
                   "slots": dict(),
                   "enums": dict()}

    # keywords_to_process = airr_yaml.keys()
    # keywords_to_process = parsed_args.keywords_to_parse
    keywords_to_process = get_simple_keywords_to_process(airr_yaml)

    # Simple keywords: add classes, slots and enums
    for keyword in keywords_to_process:
        if keyword not in skip_keywords:
            keyword_yaml = get_yaml_output_for_keyword(airr_yaml, keyword, class_prefix)
            safe_update_yaml(output_yaml, keyword_yaml)

            skip_keywords.append(keyword)

    # composition keywords (consisting of 'allOf'): only add classes
    # although new slots and enums could be defined here, this is not handled, as
    # 'SampleProcessing' is currently the only composition keyword
    for keyword in get_composition_keywords_to_process(airr_yaml):
        if keyword not in skip_keywords:
            keyword_yaml = airr_yaml[keyword]
            for class_yaml in keyword_yaml["allOf"]:
                all_slots = []

                if "$ref" in class_yaml:
                    super_class_name = class_yaml["$ref"].lstrip("/#")
                    all_slots.extend(output_yaml["classes"][f"{class_prefix}{super_class_name}"]["slots"])
                else:
                    all_slots.extend(list(class_yaml["properties"].keys()))

            safe_update_yaml(output_yaml, {"classes": {f"{class_prefix}{keyword}": {"slots": all_slots}}})

    write_yaml_output(output_yaml, parsed_args.output_file)


if __name__ == "__main__":
    parsed_args = get_arguments()

    main(parsed_args)



