#!/bin/bash

# Check if the correct number of arguments is provided
# This processes all of the JSON file in input_directory
# and generates a single combined file. Lists at the top
# level of the objects are merged across the files to 
# create a single long list. There is an expected top level
# object called AIRRKnowledgeCommons that contains the lists.
# E.g. All AKC "investigations" across all of the AKC files
# will be merged into a single "investigations" list.
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_directory> <output_file>"
  exit 1
fi

# Read arguments
JSON_DIR="$1"
OUTPUT_FILE="$2"

# Check if the input directory exists
if [ ! -d "$JSON_DIR" ]; then
  echo "Error: Directory $JSON_DIR does not exist."
  exit 1
fi

# Check if the directory exists
if [ ! -d "$JSON_DIR" ]; then
  echo "Directory $JSON_DIR does not exist."
  exit 1
fi

# Use jq to dynamically merge all top-level lists from AIRRKnowledgeCommons
# Thanks to ChatGPT for the jq magic...
jq -s '
  reduce .[] as $item ({};
    if $item.AIRRKnowledgeCommons then
      reduce ($item.AIRRKnowledgeCommons | keys_unsorted)[] as $key (.;
        if $item.AIRRKnowledgeCommons[$key] | type == "object" then
          .[$key] += $item.AIRRKnowledgeCommons[$key]
        elif $item.AIRRKnowledgeCommons[$key] | type == "array" then
          .[$key] += ($item.AIRRKnowledgeCommons[$key] | map(.))
        else
          .
        end
      )
    else
      .
    end
  )' "$JSON_DIR"/*.json > "$OUTPUT_FILE"

# Check if the operation succeeded
if [ $? -eq 0 ]; then
  echo "Combined lists written to $OUTPUT_FILE"
else
  echo "An error occurred while combining the files."
fi

