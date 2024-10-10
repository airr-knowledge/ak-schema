#! /opt/ireceptor/data/bin/python
"""
 ireceptor_data_loader.py is a batch loading script for loading
 iReceptor repertoire metadata and sequence rearrangement annotations
 
"""
import os
import argparse
import time
import sys

# AIRR Mapping class.
from airr_map import AIRRMap
# Repertoire loader classes 
from airr_repertoire import AIRRRepertoire

# Get the command line arguments...
def getArguments():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Note: for proper data processing, project --samples metadata should\n" +
        "generally be read first into the database before loading other data types."
    )

    parser.add_argument("--version", action="version", version="%(prog)s 2.0")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run the program in verbose mode. This option will generate a lot of output, but is recommended from a data provenance perspective as it will inform you of how it mapped input data columns into repository columns.")
    parser.add_argument(
        "--skipload",
        action="store_true",
        help="Run the program without actually lodaing data into the repository. This option will allow testing of the entire load process without changing the repository.")
    parser.add_argument(
        "--update",
        action="store_true",
        help="Run the program in update mode rather than insert mode. This only works for repertoires.")

    # Add configuration options 
    config_group = parser.add_argument_group("Configuration file options", "")
    config_group.add_argument(
        "--mapfile",
        dest="mapfile",
        default="ireceptor.cfg",
        help="the iReceptor configuration file. Defaults to 'ireceptor.cfg' in the local directory where the command is run. This file contains the mappings between the AIRR Community field definitions, the annotation tool field definitions, and the fields and their names that are stored in the repository."
    )

    type_group = parser.add_argument_group("data type options", "")
    type_group = type_group.add_mutually_exclusive_group()

    # Processing iReceptor Repertoire metadata
    type_group.add_argument(
        "--ireceptor",
        action="store_const",
        const="iReceptor Repertoire",
        dest="type",
        default="",
        help="The file to be loaded is an iReceptor sample/repertoire metadata file (a 'csv' file with standard iReceptor/AIRR column headers)."
    )

    # Processing AIRR Repertoire metadata
    type_group.add_argument(
        "--repertoire",
        action="store_const",
        const="AIRR Repertoire",
        dest="type",
        default="",
        help="The file to be loaded is an AIRR repertoire metadata file (a 'JSON' file that adheres to the AIRR Repertoire standard)."
    )

    path_group = parser.add_argument_group("file options")
    path_group.add_argument(
        "-f",
        "--filename",
        dest="filename",
        default="",
        help="Name of the file to load."
    )
    path_group.add_argument(
        "-o",
        "--output",
        dest="output_filename",
        default="",
        help="Name of the file to store the output in."
    )

    options = parser.parse_args()

    if options.verbose:
        print('MAPFILE      :', options.mapfile)
        print('DATA_TYPE    :', options.type)
        print('FILE_NAME    :', options.filename)

    return options

if __name__ == "__main__":
    # Get the command line arguments.
    options = getArguments()

    # Create the AIRR mapping object, which has the mapping of fields between
    # the various components. This is essentially a mapping between the AIRR
    # standard fields, the fields in the input file being parsed, and the fields
    # that are stored in the repository.
    airr_map = AIRRMap(options.verbose)
    airr_map.readMapFile(options.mapfile)

    # Start timing the file loading
    t_start = time.perf_counter()

    # Open the output file if provided, otherwise use stdout
    # If we can't open the output file exit.
    out_file = sys.stdout
    if len(options.output_filename) > 0:
        try:
            out_file = open(options.output_filename, "w")
        except:
            print("ERROR: Could not open output file %s"%(options.output_filename))
            sys.exit(4)

    if options.type == "AIRR Repertoire":
        # process AIRR Repertoire metadata
        print("Info: Processing AIRR repertoire metadata file: {}".format(options.filename))
        parser = AIRRRepertoire(options.verbose, airr_map)
    else:
        print("ERROR: unknown data type '{}'".format(options.type))
        sys.exit(4)

    # Check for a valid parser.
    if not parser.checkValidity():
        print("ERROR: Parser not constructed correctly, exiting...")
        sys.exit(4)

    # Parse the file
    parse_ok = parser.process(options.filename, out_file)
    operation = "processed"
    if options.update:
        operation = "updated"
    if parse_ok:
        print("Info: %s file %s %s successfully"%(options.type,options.filename,operation))
    else:
        print("ERROR: %s file %s not %s successfully"%(options.type,options.filename,operation))

    # time end
    t_end = time.perf_counter()
    print("Info: Finished processing in {:.2f} mins".format((t_end - t_start) / 60))

    # Close the output file
    out_file.close()

    # Return success
    if parse_ok:
        sys.exit(0)
    else:
        sys.exit(1)
