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
# Repository class - hides the DB implementation
#from repository import Repository
# Repertoire loader classes 
#from ir_repertoire import IRRepertoire
from airr_repertoire import AIRRRepertoire
# Rearrangement loader classes
#from imgt import IMGT
#from mixcr import MiXCR
#from airr_tsv import AIRR_TSV
#from adaptive import Adaptive
# Clone loader classes
#from mixcr_clone import MiXCR_Clone
#from airr_clone import AIRR_Clone
# Cell loader classes
#from airr_cell import AIRR_Cell
# Gene Expression loader classes
#from airr_expression import AIRR_Expression

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

    # Override the annotation tool being used. 
    config_group.add_argument(
        "--annotation_tool",
        dest="annotation_tool",
        default="",
        help="The annotation tool to be noted for each rearrangment. This defaults to the tool that is chosen (IgBLAST, MiXCR, V-Quest) but can be overridden by the user if desired. This is most useful for AIRR files which can come from a variety of annotation tools (the default being IgBLAST)."
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

    # Processing IMGT VQuest data, in the form of a zip archive
    type_group.add_argument(
        "--imgt",
        action='store_const',
        const="IMGT V-Quest",
        dest="type",
        help="The file to be loaded is a compressed archive files as provided by the IMGT HighV-QUEST annotation tool."
    )

    # Processing MiXCR data
    type_group.add_argument(
        "--mixcr",
        action='store_const',
        const="MiXCR",
        dest="type",
        help="The file to be loaded is a text (or compressed text) annotation file as produced by the MiXCR annotation tool."
    )

    # Processing MiXCR v3 data
    type_group.add_argument(
        "--mixcr_v3",
        action='store_const',
        const="MiXCR-v3",
        dest="type",
        help="The file to be loaded is a text (or compressed text) annotation file as produced by the MiXCR v3 and above annotation tool."
    )

    # Processing Adaptive data
    type_group.add_argument(
        "--adaptive",
        action='store_const',
        const="Adaptive",
        dest="type",
        help="The file to be loaded is a text (or compressed text) annotation file as produced by the Adaptive ImmuneAccess platform."
    )

    # Processing AIRR TSV annotation data, typically (but not limited to) from IgBLAST
    type_group.add_argument(
        "--airr",
        action='store_const',
        const="AIRR TSV",
        dest="type",
        help="The file to be loaded is a text (or compressed text) annotation file in the AIRR TSV rearrangement format. This format is used to load annotation files produced by IgBLAST (and other tools) that can produce AIRR TSV rearrangement files."
    )

    # Process a general rearrangement mapping
    type_group.add_argument(
        "--10x_contig",
        action='store_const',
        const="10x_contig",
        dest="type",
        help="The file to be loaded is a 10X contig file as produced by the 10X VDJ pipeline. If using a post v4.0 version of the 10X pipeline, we recommend you use the airr_annotations.tsv file and the airr format for data loading."
    )

    # Process a general rearrangement mapping
    type_group.add_argument(
        "--general",
        action='store_const',
        const="ir_general",
        dest="type",
        help="The file to be loaded is a text (or compressed text) annotation file that uses a 'general' mapping that is non specific to an annotation tool. This feature allows for the creation of a generic rearrangement loading capability. This requires that an ir_general mapping be present in the AIRR Mapping configuration file being used by the data loader (see the --mapfile option)"
    )

    # Processing MiXCR Clone data
    type_group.add_argument(
        "--mixcr-clone",
        action='store_const',
        const="MiXCR Clone",
        dest="type",
        help="The file to be loaded is a text (or compressed text) annotation file as produced by the MiXCR clone annotation tool."
    )

    # Processing AIRR Clone data
    type_group.add_argument(
        "--airr-clone",
        action='store_const',
        const="AIRR Clone",
        dest="type",
        help="The file to be loaded is a text (or compressed text) annotation file in the AIRR Clone JSON format."
    )

    # Processing AIRR Cell JSON data
    type_group.add_argument(
        "--airr-cell",
        action='store_const',
        const="AIRR Cell",
        dest="type",
        help="The file to be loaded is a text (or compressed text) AIRR Cell JSON file."
    )

    # Processing AIRR Cell JSON data
    type_group.add_argument(
        "--airr-expression",
        action='store_const',
        const="AIRR Expression",
        dest="type",
        help="The file to be loaded is a text (or compressed text) AIRR Gene Expression JSON file."
    )

    db_group = parser.add_argument_group("database options")
    db_group.add_argument(
        "--host",
        dest="host",
        default="localhost",
        help="MongoDb server hostname. Defaults to 'localhost'."
    )
    db_group.add_argument(
        "--port",
        dest="port",
        default=27017,
        type=int,
        help="MongoDb server port number. Defaults to 27017."
    )
    db_group.add_argument(
        "-u",
        "--user",
        dest="user",
        default=os.environ.get("MONGODB_SERVICE_USER", ""),
        help="MongoDb user name. Defaults to the MONGODB_SERVICE_USER environment variable if set. Defaults to empty string (no user name) otherwise."
    )
    db_group.add_argument(
        "-p",
        "--password",
        dest="password",
        default=os.environ.get("MONGODB_SERVICE_SECRET", ""),
        help="MongoDb service user account password. Defaults to the MONGODB_SERVICE_SECRET environment variable if set. Defaults to empty string (no password) otherwise."
    )
    db_group.add_argument(
        "-d",
        "--database",
        dest="database",
        default=os.environ.get("MONGODB_DB", "ireceptor"),
        help="Target MongoDb database. Defaults to the MONGODB_DB environment variable if set. Defaults to 'ireceptor' otherwise."
    )
    db_group.add_argument(
        "--database_map",
        dest="database_map",
        default="ir_repository",
        help="Mapping to use to map data terms into repository terms. Defaults to ir_repository, which is the mapping for the iReceptor Turnkey repository. This mapping keyword MUST be in the term mapping file as specified by --mapfile"
    )
    db_group.add_argument(
        "--database_chunk",
        dest="database_chunk",
        default=100000,
        type=int,
        help="Number of records to process in a single step when loading rearrangment data into the repository. This is used to reduce the memory footpring of the loading process when very large files are being loaded. Defaults to 100,000"
    )
    db_group.add_argument(
        "--repertoire_collection",
        dest="repertoire_collection",
        default="sample",
        help="The collection to use for storing and searching repertoires (sample metadata). This is the collection that sample metadata is inserted into when the --sample option is specified. Defaults to 'sample', which is the collection in the iReceptor Turnkey repository."
    )
    db_group.add_argument(
        "--rearrangement_collection",
        dest="rearrangement_collection",
        default="sequence",
        help="The collection to use for storing and searching rearrangements (sequence annotations). This is the collection that data is inserted into when the --mixcr, --imgt, and --airr options are used to load files. Defaults to 'sequence', which is the collection in the iReceptor Turnkey repository."
    )
    db_group.add_argument(
        "--clone_collection",
        dest="clone_collection",
        default="clone",
        help="The collection to use for storing and searching clones. This is the collection that data is inserted into when the --mixcr-clone option is used to load files. Defaults to 'clone', which is the collection in the iReceptor Turnkey repository."
    )
    db_group.add_argument(
        "--cell_collection",
        dest="cell_collection",
        default="cell",
        help="The collection to use for storing and searching cells. This is the collection that data is inserted into when the --airr-cell option is used to load files. Defaults to 'cell', which is the collection in the iReceptor Turnkey repository."
    )
    db_group.add_argument(
        "--expression_collection",
        dest="expression_collection",
        default="expression",
        help="The collection to use for storing and searching gene expression. This is the collection that data is inserted into when the --airr-expression option is used to load files. Defaults to 'expression', which is the collection in the iReceptor Turnkey repository."
    )

    path_group = parser.add_argument_group("file options")
    path_group.add_argument(
        "-f",
        "--filename",
        dest="filename",
        default="",
        help="Name of the file to load. It is assumed that the filename provided is in the appropiate format that matches either the --sample, --imgt, --mixcr, or --airr command line options. An error will be reported if the formats do not match."
    )

    options = parser.parse_args()

    if options.verbose:
        print('HOST         :', options.host)
        print('PORT         :', options.port)
        print('USER         :', options.user[0] + (len(options.user) - 2) * "*" + options.user[-1] if options.user else "")
        print('PASSWORD     :', options.password[0] + (len(options.password) - 2) * "*" + options.password[-1] if options.password else "")
        print('DATABASE     :', options.database)
        print('DATABASE_MAP :', options.database_map)
        print('MAPFILE      :', options.mapfile)
        print('DATA_TYPE    :', options.type)
        print('FILE_NAME    :', options.filename)

    return options

if __name__ == "__main__":
    # Get the command line arguments.
    options = getArguments()

    # Create the repository object, which establishes the repository connection.
    #repository = Repository(options.user, options.password,
                            #options.host, options.port,
                            #options.database,
                            #options.repertoire_collection,
                            #options.rearrangement_collection,
                            #options.clone_collection,
                            #options.cell_collection,
                            #options.expression_collection,
                            #options.skipload, options.update,
                            #options.verbose)
    # Check on the successful creation of the repository
    #if repository is None or not repository:
        #sys.exit(1)
    # For now, we won't use the repository.
    repository = None

    # Create the AIRR mapping object, which has the mapping of fields between
    # the various components. This is essentially a mapping between the AIRR
    # standard fields, the fields in the input file being parsed, and the fields
    # that are stored in the repository.
    airr_map = AIRRMap(options.verbose)
    airr_map.readMapFile(options.mapfile)
    if airr_map.getRearrangementMapColumn(options.database_map) is None:
        print("ERROR: Could not find repository mapping %s in AIRR Mappings"%
              (options.database_map))
        sys.exit(1)

    # Start timing the file loading
    t_start = time.perf_counter()

    if options.type == "AIRR Repertoire":
        # process AIRR Repertoire metadata
        print("Info: Processing AIRR repertoire metadata file: {}".format(options.filename))
        parser = AIRRRepertoire(options.verbose, options.database_map, options.database_chunk,
                                airr_map, repository)
    #elif options.type == "AIRR TSV":
    #    # process AIRR TSV
    #    print("Info: Processing AIRR TSV annotation data file: ", options.filename)
    #    parser = AIRR_TSV(options.verbose, options.database_map, options.database_chunk,
    #                      airr_map, repository)
    else:
        print("ERROR: unknown data type '{}'".format(options.type))
        sys.exit(4)

    # Check for a valid parser.
    if not parser.checkValidity():
        print("ERROR: Parser not contructed correctly, exiting...")
        sys.exit(4)

    # Override what the default annotation tool that the Parser subclass set by default.
    if not options.annotation_tool == "":
        parser.setAnnotationTool(options.annotation_tool)

    # Parse the file
    parse_ok = parser.process(options.filename)
    operation = "loaded"
    if options.update:
        operation = "updated"
    if parse_ok:
        print("Info: %s file %s %s successfully"%(options.type,options.filename,operation))
    else:
        print("ERROR: %s file %s not %s successfully"%(options.type,options.filename,operation))

    # time end
    t_end = time.perf_counter()
    print("Info: Finished processing in {:.2f} mins".format((t_end - t_start) / 60))

    # Return success
    if parse_ok:
        sys.exit(0)
    else:
        sys.exit(1)
