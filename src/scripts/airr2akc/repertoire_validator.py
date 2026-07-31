import json
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.loaders import json_loader
from linkml_runtime.dumpers import json_dumper
import sys
import logging
import argparse

#modifying path to access ak_schema.py file
sys.path.insert(0, "/work")
from src.ak_schema.datamodel.ak_schema import RepertoireDataFile


# Configure logging to display warnings clearly
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

sv = SchemaView("project/linkml/ak_schema.yaml")
EXCLUDED_KEYS = set()

EXCLUDED_SCHEMA_PATHS = set()
# ==================================================================================
# Find Classes that are available in the schema and only keep those in the repertoire file
# ==================================================================================

# Get all valid schema class names for quick lookup
ALL_SCHEMA_CLASSES = set(sv.all_classes().keys())

def get_allowed_slots_for_class(class_name: str) -> set:
    """Returns all valid slot names for a given class if it exists in the schema."""
    if class_name not in ALL_SCHEMA_CLASSES:
        print(f"class_name: {class_name} not in SCHEMA")
        return set()
    try:
        cls = sv.induced_class(class_name)
        return {s.name for s in cls.attributes.values()} | set(cls.slots)
    except Exception:
        return set()


def clean_airr_dict(data, class_name="RepertoireDataFile", path="root"):
    """
    Recursively removes any JSON key that is not a valid slot for the given LinkML class.
    """
    # Handle lists
    if isinstance(data, list):
        return [clean_airr_dict(item, class_name) for item in data]

    # Return primitives as-is/ Should be a dict
    if not isinstance(data, dict):
        return data

    allowed_slots = get_allowed_slots_for_class(class_name)

    cleaned = {}
    for key, value in data.items():
        # If the class is recognized in schema and key isn't allowed, skip it
        if allowed_slots and key not in allowed_slots:
            EXCLUDED_KEYS.add(key)
            EXCLUDED_SCHEMA_PATHS.add(f"{class_name}.{key}")
            continue

        # Look up child range class name
        child_class_name = key
        if allowed_slots and key in allowed_slots:
            try:
                slot_def = sv.induced_slot(key, class_name)
                # Only use range if it points to a recognized class (not a string/int primitive)
                if slot_def and slot_def.range in ALL_SCHEMA_CLASSES:
                    child_class_name = slot_def.range
            except Exception:
                pass

        # Recurse into dicts or lists
        if isinstance(value, (dict, list)):
            cleaned[key] = clean_airr_dict(value, child_class_name)
        else:
            cleaned[key] = value

    return cleaned


# ==================================================================================
# Read Repertoire File Clean it
# ==================================================================================
parser = argparse.ArgumentParser()
parser.add_argument( "filename", nargs="?", default="examples/repertoires/repertoires.airr.json", help="AIRR JSON file")
args = parser.parse_args()
filename = args.filename

print(filename)
with open(filename) as f:
    d = json.load(f)

#Change these fields to match class names in schema

d["info"] = d.pop("Info")
d["repertoires"] = d.pop("Repertoire")

cleaned_data = clean_airr_dict(d, class_name="RepertoireDataFile")

# --- Print Unique Summary Report ---
print("\n" + "="*50)
print(" EXCLUSION SUMMARY (Deduplicated)")
print("="*50)

print(f"\nUnique Unmapped Keys Excluded ({len(EXCLUDED_KEYS)}):")
for k in sorted(EXCLUDED_KEYS):
    print(f" - {k}")

print(f"\nUnique Class Paths Excluded ({len(EXCLUDED_SCHEMA_PATHS)}):")
for p in sorted(EXCLUDED_SCHEMA_PATHS):
    print(f" - {p}")

print("\n" + "="*50)

# ==================================================================================
# Use Json loader for validation
# ==================================================================================

obj = json_loader.load(
    cleaned_data,
    target_class=RepertoireDataFile,
)

print("Successfully loaded RepertoireDataFile!")
print(f"Total Repertoires: {len(obj.repertoires)}")

# print(obj)
# print(type(obj))
# print(type(obj.repertoires))
# print(len(obj.repertoires[0]))
print(obj.repertoires[0])


# Write back out
json_dumper.dump(obj, "repertoires_out.airr.json" )

print("Successfully wrote repertoires_out.airr.json")

# # # Test if the files are same
# # with open("repertoires.airr.json") as f:
# #     original = json.load(f)

# # with open("repertoires_out.airr.json") as f:
# #     generated = json.load(f)

# # if original == generated:
# #     print("JSON files are structurally identical")
# # else:
# #     print("JSON files differ")