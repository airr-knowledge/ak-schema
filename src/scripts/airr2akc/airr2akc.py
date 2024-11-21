import argparse
import yaml
import sys

def get_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="")

    parser.add_argument("-a", "--airr_schema_yaml", type=str, default="/Users/lscheffer/PycharmProjects/ak-schema/src/scripts/airr2akc/airr-schema-openapi3.yaml")
    parser.add_argument("-o", "--output_file", type=str, default="../../ak_schema/schema/ak_airr.yaml")

    return parser.parse_args()


def snake_to_camel_case(word):
    # Change _ to camel case as per LinkML naming. _ _ replaced with _
    new_word = ''.join('_' if x == '' else x.capitalize() for x in word.split('_'))
    return new_word

def camel_to_snake_case(word):
    return "".join([char if char.islower() else "_" + char.lower() for char in word]).lstrip("_")

def get_slot_range(slot_name, slot_yaml, version_prefix):
    # if this is an array, get the type of the 'items' in the array
    if "type" in slot_yaml and slot_yaml["type"] == "array":
        slot_range = get_slot_range(slot_name, slot_yaml["items"], version_prefix)
    elif "enum" in slot_yaml:
        slot_range = f"{version_prefix}{snake_to_camel_case(slot_name)}"
    elif "$ref" in slot_yaml:
        if slot_yaml["$ref"] == "#/Ontology":
            slot_range = f"{version_prefix}{snake_to_camel_case(slot_name)}"
        else:
            slot_range = f"{version_prefix}{slot_yaml["$ref"].lstrip("#/")}"
    elif "type" in slot_yaml and slot_yaml["type"] in ("string", "float", "integer", "boolean", "number"):
        slot_range = slot_yaml["type"]
    # elif "x-airr" in slot_yaml and "format" in slot_yaml["x-airr"]:
    #     slot_range = slot_yaml["x-airr"]["format"]  #
    elif "type" in slot_yaml and slot_yaml["type"] == "object":
        slot_range = slot_yaml["type"]
        print(f"Cannot determine range for slot '{slot_name}', omitting range...", file=sys.stderr)
        slot_range = None
    else:
        raise NotImplementedError(slot_yaml)

    if slot_range == "number":
        slot_range = "float"

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

def get_slot(orig_slot_name, slot_yaml, required_slots, cls_keyword, version_prefix):
    pr_slot_name = f"{version_prefix}_{camel_to_snake_case(cls_keyword)}__{orig_slot_name}"

    if is_deprecated(slot_yaml):
        return dict()

    slot = {pr_slot_name: {
                "name": pr_slot_name,
                "description": slot_yaml["description"].strip() if "description" in slot_yaml else "",
                }}

    slot_range = get_slot_range(orig_slot_name, slot_yaml, version_prefix)
    if slot_range is not None:
        slot[pr_slot_name]["range"] = slot_range

    if is_array(slot_yaml):
        slot[pr_slot_name]["multivalued"] = True

    is_required = orig_slot_name in required_slots
    slot[pr_slot_name]["required"] = is_required

    annotations = get_slot_annotation(slot_yaml)
    if len(annotations) > 0:
        slot[pr_slot_name]["annotations"] = annotations

    return slot


def get_all_slots(airr_yaml, keyword, version_prefix) -> dict:
    all_slots = dict()

    required_slots = airr_yaml[keyword]["required"] if "required" in airr_yaml[keyword] else []

    for slot_name, slot_yaml in airr_yaml[keyword]["properties"].items():
        all_slots.update(get_slot(slot_name, slot_yaml, required_slots, keyword, version_prefix))

    return all_slots

def get_ontology_enum(name, slot_yaml, version_prefix):
    if "ontology" in slot_yaml["x-airr"]:
        source_node = slot_yaml["x-airr"]["ontology"]["top_node"]["id"]

        if source_node is not None:
            return {"name": f"{version_prefix}{name}",
                    "reachable_from":
                        {"source_nodes": [source_node],
                         "include_self": True,
                         "relationship_types": ["rdfs:subClassOf"]}}
        else:
            print(f"Source node for ontology '{name}' was not defined. \n"
                  f"  Expected to find some value in the field: x-airr/ontology/top_node/id\n"
                  f"  Instead found these fields: {slot_yaml}", file=sys.stderr)
    else:
        print(f"Ontology '{name}' does not follow the correct formatting.\n"
              f"  Expected to find the field: x-airr/ontology/top_node/id\n"
              f"  Instead found these fields: {slot_yaml}", file=sys.stderr)

    return {"name": f"{version_prefix}{name}"}

def get_closed_vocabulary_enum(name, slot_yaml, version_prefix):
    return {"name": f"{version_prefix}{name}",
            "permissible_values": {"null" if enum_val is None else enum_val: None for enum_val in
                                   slot_yaml["enum"]}}

def get_enum(name, slot_yaml, version_prefix):
    if "type" in slot_yaml and slot_yaml["type"] == "array":
        return get_enum(name, slot_yaml["items"], version_prefix)

    if "$ref" in slot_yaml and slot_yaml["$ref"] == "#/Ontology":
        return get_ontology_enum(name, slot_yaml, version_prefix)

    elif "enum" in slot_yaml:
        return get_closed_vocabulary_enum(name, slot_yaml, version_prefix)


def get_all_enums(keyword_yaml, version_prefix):
    all_enums = dict()

    for slot_name, slot_yaml in keyword_yaml["properties"].items():
        if not is_deprecated(slot_yaml):
            name = snake_to_camel_case(slot_name)
            new_enum = get_enum(name, slot_yaml, version_prefix)

            if new_enum is not None:
                all_enums[f"{version_prefix}{name}"] = new_enum

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

def get_yaml_output_for_keyword(airr_yaml, keyword, version_prefix):
    # keyword_yaml = airr_yaml[keyword]
    output_slots = get_all_slots(airr_yaml, keyword, version_prefix)

    yaml_output_dict = {"classes": {f"{version_prefix}{keyword}": {"slots": list(output_slots.keys())}},
                        "slots": output_slots,
                        "enums": get_all_enums(airr_yaml[keyword], version_prefix)}

    return yaml_output_dict

def new_keys_not_in_existing(existing_keys, new_keys):
    return all([key not in existing_keys for key in new_keys])

def check_can_safely_add(existing_yaml, new_yaml, type_name):
    for key in new_yaml:
        if key in existing_yaml:
            if new_yaml[key] != existing_yaml[key]:
                print(f"Issue when attempting to add {type_name} '{key}'. Same slot was already found with different content:\n"
                      f"  Existing: {new_yaml[key]}\n  New:      {existing_yaml[key]}", file=sys.stderr)
            # assert new_yaml[key] == existing_yaml[key]


def safe_update_yaml(output_yaml, keyword_yaml):
    if "classes" in keyword_yaml:
        check_can_safely_add(output_yaml["classes"], keyword_yaml["classes"], type_name="class")
        output_yaml["classes"].update(keyword_yaml["classes"])

    if "slots" in keyword_yaml:
        check_can_safely_add(output_yaml["slots"], keyword_yaml["slots"], type_name="slot")
        output_yaml["slots"].update(keyword_yaml["slots"])

    if "enums" in keyword_yaml:
        check_can_safely_add(output_yaml["enums"], keyword_yaml["enums"], type_name="enum")
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
    airr_yaml = get_airr_yaml(parsed_args.airr_schema_yaml)
    airr_version = airr_yaml["Info"]["version"]
    version_prefix = f"v{str(airr_version).replace('.', 'p')}_"


    skip_keywords = ["Info", "Ontology", "CURIEMap", "InformationProvider", "Attributes", "FileObject", "DataSet",
                                      "Manifest", "DataFile", "InfoObject"]

    output_yaml = {"id": "https://github.com/airr-knowledge/ak-schema",
                   "name": "ak-schema",
                   # "airr_version": airr_version,
                   "classes": dict(),
                   "slots": dict(),
                   "enums": dict()}

    # keywords_to_process = airr_yaml.keys()
    keywords_to_process = get_simple_keywords_to_process(airr_yaml)

    # Simple keywords: add classes, slots and enums
    for keyword in keywords_to_process:
        if keyword not in skip_keywords:
            keyword_yaml = get_yaml_output_for_keyword(airr_yaml, keyword, version_prefix)
            safe_update_yaml(output_yaml, keyword_yaml)

            skip_keywords.append(keyword)

    # composition keywords (consisting of 'allOf'): only add classes
    # although new slots and enums could be defined here, this is not handled, as
    # 'SampleProcessing' is currently the only composition keyword
    for keyword in get_composition_keywords_to_process(airr_yaml):
        if keyword not in skip_keywords:
            keyword_yaml = airr_yaml[keyword]
            # all_slots = []
            composition_yaml = {"classes": {f"{version_prefix}{keyword}": {"slots": []}},
                                "slots": {},
                                "enums": {}}

            for class_yaml in keyword_yaml["allOf"]:
                if "$ref" in class_yaml:
                    super_class_name = class_yaml["$ref"].lstrip("/#")
                    composition_yaml["classes"][f"{version_prefix}{keyword}"]["slots"].extend(output_yaml["classes"][f"{version_prefix}{super_class_name}"]["slots"])
                else:
                    new_slots = get_all_slots({keyword: class_yaml}, keyword, version_prefix)
                    new_enums = get_all_enums(class_yaml, version_prefix)
                    composition_yaml["slots"].update(new_slots)
                    composition_yaml["enums"].update(new_enums)

                    composition_yaml["classes"][f"{version_prefix}{keyword}"]["slots"].extend(list(new_slots.keys()))


            safe_update_yaml(output_yaml, composition_yaml)

    write_yaml_output(output_yaml, parsed_args.output_file)


if __name__ == "__main__":
    parsed_args = get_arguments()

    main(parsed_args)




