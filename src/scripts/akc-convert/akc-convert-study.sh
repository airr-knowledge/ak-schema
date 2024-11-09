#!/bin/bash

# Check if the input TSV file is provided as an argument
if [ $# -ne 3 ]; then
    echo "Usage: $0 REPOSITORY STUDY_ID OUTPUT_DIR"
    exit 1
fi

# Get the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Get the parameters
REPOSITORY=$1
STUDY_ID=$2
OUTPUT_DIR=$3

# Check if the output directory is a directory
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Error: '$OUTPUT_DIR' is not a directory."
    exit 1
fi

# Query the repository for the study ID provided and save the repertoire file.
curl --silent -H 'content-type: application/json' -d "{\"filters\":{\"op\":\"=\", \"content\": {\"field\":\"study.study_id\", \"value\":\"$STUDY_ID\"}}}" https://$REPOSITORY/airr/v1/repertoire > $OUTPUT_DIR/$REPOSITORY-$STUDY_ID-ADC.json
# If the query failed, print a message and exit.
if [ $? -ne 0 ]; then
    echo "Error: Query for $STUDY_ID in repository $REPOSITORY failed"
    exit 1
fi

# Check the count of the number of repertoires, and if none were found, exit.
COUNT=`cat $OUTPUT_DIR/$REPOSITORY-$STUDY_ID-ADC.json | jq '.Repertoire | length'`
if [ $COUNT -eq 0 ]; then
    echo "Error: Query for $STUDY_ID in repository $REPOSITORY returned no repertoires"
    exit 1
fi

# Convert the data to the AKC schema
python dataloader.py --repertoire -f $OUTPUT_DIR/$REPOSITORY-$STUDY_ID-ADC.json --mapfile ./config/AIRR-iReceptorMapping.txt -o $OUTPUT_DIR/$REPOSITORY-$STUDY_ID-AKC.json
# If conversion failed, report an error and exit.
if [ $? -ne 0 ]; then
    echo "Error: Conversion of ADC query response failed"
    exit 1
fi

echo "Info: Conversion complete, AKC format data in $OUTPUT_DIR/$REPOSITORY-$STUDY_ID-AKC.json"
