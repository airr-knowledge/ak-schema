import argparse
import yaml
import sys
import logging
import glob
from datetime import datetime


def get_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="Script to convert AIRR openapi3 schema to LinkML")

    parser.add_argument("-a", "--airr_schema_yaml", type=str, help="Input openapi3 YAML file",
                        default="../../airr_schema/airr-standards-v1.5/specs/airr-schema-openapi3.yaml")
    parser.add_argument("-o", "--output_file", type=str, help="Output file to write the LinkML to",
                        default="../../ak_schema/schema/ak_airr.yaml")
    parser.add_argument("-f", "--ak_schema_folder", type=str, help="AK schema folder, for checking conflicts with existing schema",
                        default="../../ak_schema/schema/")
    parser.add_argument("-l", "--log_file", type=str, help="Log file to write any error occurring while generating LinkML",
                        default="airr2akc.log")

    parser.add_argument("-s", "--superclass",  type=str, help="Superclass name (will be referenced for each class under 'is_a')", default="AIRRObject")

    parser.add_argument("-v", "--include_version_prefix", action="store_true",
                        help="When this flag is specified, the AIRR version is included as a class prefix")
    parser.add_argument("-c", "--include_class_prefix", action="store_true",
                        help="When this flag is specified, the class name is included as a slot prefix")

    return parser.parse_args()


def snake_to_camel_case(word):
    new_word = ''.join('_' if x == '' else x.capitalize() for x in word.split('_'))
    return new_word

def camel_to_snake_case(word):
    return "".join([char if char.islower() else "_" + char.lower() for char in word]).lstrip("_")

def get_slot_range(slot_name, slot_yaml, version_prefix):
    # if this is an array, get the type of the 'items' in the array
    if "type" in slot_yaml and slot_yaml["type"] == "array":
        slot_range = get_slot_range(slot_name, slot_yaml["items"], version_prefix)
    elif "enum" in slot_yaml:
        slot_range = f"{version_prefix}{snake_to_camel_case(slot_name)}Enum"
    elif "$ref" in slot_yaml:
        if slot_yaml["$ref"] == "#/Ontology":
            slot_range = f"{version_prefix}{snake_to_camel_case(slot_name)}Ontology"
        else:
            slot_range = f"{version_prefix}{slot_yaml['$ref'].lstrip('#/')}"
    elif "type" in slot_yaml and slot_yaml["type"] in ("string", "float", "integer", "boolean", "number"):
        if slot_yaml["type"] == "string" and "format" in slot_yaml and slot_yaml["format"] in ("date", "date-time"):
            slot_range = "datetime"
        else:
            slot_range = slot_yaml["type"]
    # elif "x-airr" in slot_yaml and "format" in slot_yaml["x-airr"]:
    #     slot_range = slot_yaml["x-airr"]["format"]  #
    elif "type" in slot_yaml and slot_yaml["type"] == "object":
        logging.error(f"**\n"
                      f"** Error: Cannot determine range for slot '{slot_name}', omitting range...\n"
                      f"**")
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

def is_multivalued(slot_yaml):
    return is_array(slot_yaml) or "additionalProperties" in slot_yaml

def get_slot(orig_slot_name, slot_yaml, required_slots, cls_keyword, version_prefix):
    if is_deprecated(slot_yaml):
        return dict()

    # Used for Tree/nodes only
    if "additionalProperties" in slot_yaml and type(slot_yaml["additionalProperties"]) == dict:
        slot_yaml = {**slot_yaml["additionalProperties"], **slot_yaml}

    cls_prefix = cls_keyword + "_" if parsed_args.include_class_prefix else ""
    pr_slot_name = f"{version_prefix}{cls_prefix}{orig_slot_name}"

    slot = {pr_slot_name: {
                "name": pr_slot_name,
                "description": slot_yaml["description"].strip() if "description" in slot_yaml else "",
                }}

    if orig_slot_name.endswith("_type"):
        slot[pr_slot_name]["slot_uri"] = "rdf:type"

    slot_range = get_slot_range(orig_slot_name, slot_yaml, version_prefix)
    if slot_range is not None:
        slot[pr_slot_name]["range"] = slot_range

    if is_multivalued(slot_yaml):
        slot[pr_slot_name]["multivalued"] = True

    # is_required = orig_slot_name in required_slots
    # slot[pr_slot_name]["required"] = is_required

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

def get_ontology_enum(base_name, slot_yaml, keyword, version_prefix):
    ontology_name = f"{version_prefix}{base_name}Ontology"

    if "ontology" in slot_yaml["x-airr"]:
        source_node = slot_yaml["x-airr"]["ontology"]["top_node"]["id"]

        if source_node is not None:
            return {"name": ontology_name,
                    "reachable_from":
                        {"source_nodes": [source_node],
                         "include_self": True,
                         "relationship_types": ["rdfs:subClassOf"]}}
        else:
            logging.error(f"**\n"
                          f"** Error: Source node for ontology '{base_name}' (in '{keyword}') was not defined, omitting 'reachable_from'...\n"
                          f"**   Expected to find some value in the field: x-airr/ontology/top_node/id\n"
                          f"**   Instead found these fields: {slot_yaml}\n"
                          f"**")
    else:
        logging.error(f"**\n"
                      f"** Error: Ontology '{base_name}' (in '{keyword}') does not follow the correct formatting, omitting 'reachable_from'...\n"
                      f"**   Expected to find the field: x-airr/ontology/top_node/id\n"
                      f"**   Instead found these fields: {slot_yaml}\n"
                      f"**")

    return {"name": ontology_name}

def get_closed_vocabulary_enum(base_name, slot_yaml, keyword, version_prefix):
    return {"name": f"{version_prefix}{base_name}Enum",
            "permissible_values": {enum_val: None for enum_val in slot_yaml["enum"] if enum_val is not None}}

def get_enum(base_name, slot_yaml, keyword, version_prefix):
    if "type" in slot_yaml and slot_yaml["type"] == "array":
        return get_enum(base_name, slot_yaml["items"], keyword, version_prefix)

    if "$ref" in slot_yaml and slot_yaml["$ref"] == "#/Ontology":
        return get_ontology_enum(base_name, slot_yaml, keyword, version_prefix)

    elif "enum" in slot_yaml:
        return get_closed_vocabulary_enum(base_name, slot_yaml, keyword, version_prefix)


def get_all_enums(keyword_yaml, keyword, version_prefix):
    all_enums = dict()

    for slot_name, slot_yaml in keyword_yaml["properties"].items():
        if not is_deprecated(slot_yaml):
            base_name = snake_to_camel_case(slot_name)
            if base_name == "Property":
                pass
            new_enum = get_enum(base_name, slot_yaml, keyword, version_prefix)

            if new_enum is not None:
                all_enums[new_enum["name"]] = new_enum

    return all_enums


def get_yaml_output_for_keyword(airr_yaml, keyword, version_prefix, linkml_superclass):
    # keyword_yaml = airr_yaml[keyword]
    output_slots = get_all_slots(airr_yaml, keyword, version_prefix)

    yaml_output_dict = {"classes": {f"{version_prefix}{keyword}": {"is_a": linkml_superclass, "slots": list(output_slots.keys())}},
                        "slots": output_slots,
                        "enums": get_all_enums(airr_yaml[keyword], keyword, version_prefix)}

    return yaml_output_dict

def get_yaml_output_for_composition_keyword(airr_yaml, output_yaml, keyword, version_prefix, linkml_superclass):
    composition_yaml = {"classes": {f"{version_prefix}{keyword}": {"is_a": linkml_superclass, "slots": []}},
                        "slots": {},
                        "enums": {}}

    for class_yaml in airr_yaml[keyword]["allOf"]:
        if "$ref" in class_yaml:
            super_class_name = class_yaml["$ref"].lstrip("/#")
            composition_yaml["classes"][f"{version_prefix}{keyword}"]["slots"].extend(
                output_yaml["classes"][f"{version_prefix}{super_class_name}"]["slots"])
        else:
            new_slots = get_all_slots({keyword: class_yaml}, keyword, version_prefix)
            new_enums = get_all_enums(class_yaml, keyword, version_prefix)
            composition_yaml["slots"].update(new_slots)
            composition_yaml["enums"].update(new_enums)

            composition_yaml["classes"][f"{version_prefix}{keyword}"]["slots"].extend(list(new_slots.keys()))

    return composition_yaml


def new_keys_not_in_existing(existing_keys, new_keys):
    return all([key not in existing_keys for key in new_keys])

def get_differing_fields(yaml_pt1, yaml_pt2):
    return ([key for key in yaml_pt1 if key not in yaml_pt2] +
            [key for key in yaml_pt2 if key not in yaml_pt1] +
            [key for key in yaml_pt1 if key in yaml_pt2 and yaml_pt1[key] != yaml_pt2[key]])

def get_intersecting_yaml(yaml_pt1, yaml_pt2):
    final = {}

    for key in yaml_pt1:
        if key in yaml_pt2:
            if yaml_pt1[key] == yaml_pt2[key]:
                final[key] = yaml_pt1[key]
            elif type(yaml_pt1[key]) == dict and type(yaml_pt2[key]) == dict:
                sub_params = get_intersecting_yaml(yaml_pt1[key], yaml_pt2[key])
                if len(sub_params) > 0:
                    final[key] = sub_params

    return final

def safe_update_yaml_component(output_yaml_part, new_yaml_part, type_name):
    conflicts = []

    ignore_fields = ["description", "required", "annotations"]

    for key in new_yaml_part:
        if key in output_yaml_part:
            if new_yaml_part[key] != output_yaml_part[key]:
                conflict_fields = get_differing_fields(new_yaml_part[key], output_yaml_part[key])
                intersecting_yaml = get_intersecting_yaml(new_yaml_part[key], output_yaml_part[key])

                if "permissible_values" in conflict_fields:
                    if get_differing_fields(new_yaml_part[key]["permissible_values"], output_yaml_part[key]["permissible_values"]) == ['null']:
                        intersecting_yaml["permissible_values"]["null"] = None
                        conflict_fields.remove("permissible_values")
                        logging.warning(f"Warning: Keeping value 'null' in permissible_values for {type_name} '{key}' (only sometimes present in input)")

                if not all([field in ignore_fields for field in conflict_fields]):
                    conflicts.append(key)
                    logging.error(f"**\n"
                                    f"** Error: Conflicting {type_name} '{key}'. Same {type_name} was already found with different content (only 'final' is kept):\n"
                                    f"**   Existing: {new_yaml_part[key]}\n"
                                    f"**   New:      {output_yaml_part[key]}\n"
                                    f"**   Final:    {intersecting_yaml}\n"
                                    f"**")
                elif len(conflict_fields) > 0:
                    logging.warning(f"Warning: Removing fields {conflict_fields} from {type_name} '{key}' due to conflicting values.")

                output_yaml_part[key] = intersecting_yaml
        else:
            output_yaml_part[key] = new_yaml_part[key]

    return conflicts


def safe_update_yaml(output_yaml, keyword_yaml, conflicts):
    if "classes" in keyword_yaml:
        class_conflicts = safe_update_yaml_component(output_yaml["classes"], keyword_yaml["classes"], type_name="class")
        conflicts["class_conflicts"] += class_conflicts

    if "slots" in keyword_yaml:
        slot_conflicts = safe_update_yaml_component(output_yaml["slots"], keyword_yaml["slots"], type_name="slot")
        conflicts["slot_conflicts"] += slot_conflicts

    if "enums" in keyword_yaml:
        enum_conflicts = safe_update_yaml_component(output_yaml["enums"], keyword_yaml["enums"], type_name="enum")
        conflicts["enum_conflicts"] += enum_conflicts

def get_airr_yaml(file_location):
    with open(parsed_args.airr_schema_yaml) as file:
        airr_yaml = yaml.safe_load(file)
    return airr_yaml

def get_simple_keywords_to_process(airr_yaml, skip_keywords):
    return [key for key, value in airr_yaml.items() if "type" in value.keys() and key not in skip_keywords]

def get_composition_keywords_to_process(airr_yaml, skip_keywords):
    return [key for key, value in airr_yaml.items() if list(value.keys()) == ["allOf"] and key not in skip_keywords]


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


def log_error_summary(conflicts):
    flush_log()
    logging.info("\nSummary of errors during AIRR LinkML generation:")

    logging.info(f"  {ErrorCounter.count} errors occurred while constructing LinkML")
    for conflict_type in ("class", "slot", "enum"):
        conflicts_of_type = list(set(conflicts[f"{conflict_type}_conflicts"]))
        if len(conflicts_of_type) == 0:
            logging.info(f"  0 {conflict_type} conflicts (overlapping {conflict_type} names with different values)")
        else:
            logging.info(f"  {len(conflicts_of_type)} {conflict_type} conflicts (overlapping {conflict_type} names with different values): {', '.join(conflicts_of_type)}")

    logging.info("")
    flush_log()

def check_conflicts_with_akc_file(output_yaml, ak_data, file_path):
    overlapping_names = []

    base_keys = ("classes", "slots", "enums")
    for airr_key in base_keys:
        for airr_name in output_yaml[airr_key]:
            for ak_key in ak_data.keys():
                if ak_key in base_keys:
                    if ak_data[ak_key] is not None and airr_name in ak_data[ak_key]:
                        logging.warning(f"Warning: Overlapping namespace between AIRR and AKC LinkML ({file_path}): {airr_name} occurs in AIRR {airr_key} and AKC {ak_key}")
                        overlapping_names.append(airr_name)

    return overlapping_names

def log_confict_with_akc_summary(overlapping_names_per_file):
    flush_log()
    logging.info(f"\nSummary of conflicts between AIRR LinkML and exising AKC LinkML:")
    if len(overlapping_names_per_file) == 0:
        logging.info("  No overlapping names found")

    for file_path, overlapping_names in overlapping_names_per_file.items():
        if len(overlapping_names) > 0:
            logging.info(
                f"  Found {len(overlapping_names)} overlapping names between AIRR LinkML and {file_path}: {', '.join(overlapping_names)}")
    flush_log()

def check_conflicts_with_akc(output_yaml):
    overlapping_names_per_file = {}

    for file_path in glob.glob(f"{parsed_args.ak_schema_folder}/*.yaml"):
        if file_path not in glob.glob(f"{parsed_args.ak_schema_folder}/ak_airr*.yaml"):

            with open(file_path, "r") as file:
                ak_data = yaml.safe_load(file)
                overlapping_names = check_conflicts_with_akc_file(output_yaml, ak_data, file_path)
                if len(overlapping_names) > 0:
                    overlapping_names_per_file[file_path] = overlapping_names

    return overlapping_names_per_file

class ErrorCounter(logging.Filter):
    count = 0
    def filter(self, record):
        if record.levelno == logging.ERROR:
            self.__class__.count += 1
        return True

def configure_logger(log_file):
    # stderr and stdout are both written to the log file
    # when no issues arise, stderr is empty (but a log summary is written to stdout/log file)
    # errors are counted to include in error summary
    logger = logging.getLogger()
    logger.addFilter(ErrorCounter())
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(logging.Formatter('%(message)s'))

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.addFilter(lambda record: record.levelno < logging.WARNING)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.WARNING)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)

def flush_log():
    for handler in logging.getLogger().handlers:
        handler.flush()

def process_simple_keywords():
    pass

def main(parsed_args):
    airr_yaml = get_airr_yaml(parsed_args.airr_schema_yaml)
    airr_version = airr_yaml["Info"]["version"]
    version_prefix = f"V{str(airr_version).replace('.', 'p')}" if parsed_args.include_version_prefix else ""

    logging.info(f"Generating LinkML for AIRR version {airr_version} at {datetime.now()}\n" +
                 "\n".join([f"  {key}: {value}" for key, value in vars(parsed_args).items()]) + "\n")
    flush_log()


    skip_keywords = ["Info", "Ontology", "CURIEMap", "InformationProvider", "Attributes", "FileObject", "DataSet",
                                      "Manifest", "DataFile", "InfoObject"]

    output_yaml = {"id": "https://github.com/airr-knowledge/ak-schema",
                   "name": "ak-schema",
                   "classes": dict(),
                   "slots": dict(),
                   "enums": dict()}

    internal_conflicts = {"class_conflicts": [],
                          "slot_conflicts": [],
                          "enum_conflicts": []}

    # Simple keywords: add classes, slots and enums
    for keyword in get_simple_keywords_to_process(airr_yaml, skip_keywords):
        keyword_yaml = get_yaml_output_for_keyword(airr_yaml, keyword, version_prefix, parsed_args.superclass)
        safe_update_yaml(output_yaml, keyword_yaml, internal_conflicts)

    # composition keywords (consisting of 'allOf')
    for keyword in get_composition_keywords_to_process(airr_yaml, skip_keywords):
        composition_yaml = get_yaml_output_for_composition_keyword(airr_yaml, output_yaml, keyword, version_prefix, parsed_args.superclass)
        safe_update_yaml(output_yaml, composition_yaml, internal_conflicts)

    write_yaml_output(output_yaml, parsed_args.output_file)
    akc_conflicts = check_conflicts_with_akc(output_yaml)

    log_error_summary(internal_conflicts)
    log_confict_with_akc_summary(akc_conflicts)

if __name__ == "__main__":
    parsed_args = get_arguments()

    configure_logger(parsed_args.log_file)
    main(parsed_args)




