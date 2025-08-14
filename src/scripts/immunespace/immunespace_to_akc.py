from src.ak_schema.datamodel.ak_schema import *
from linkml_runtime.dumpers import yaml_dumper, json_dumper

import uuid
import pandas as pd
import sqlite3
import os
from pathlib import Path




class IdentifierHandler():
    def __init__(self, id_file=None):
        if id_file and id_file.is_file():
            self.identifiers = pd.read_csv(id_file, sep="\t")
        else:
            self.identifiers = pd.DataFrame(columns=["immunespace_id", "id_type", "akc_id"])

    def get_akc_id(self, immunespace_id, id_type):
        row = self.identifiers[(self.identifiers.immunespace_id==immunespace_id) & (self.identifiers.id_type==id_type)]

        if row.empty:
            akc_id = str(uuid.uuid4())
            self.identifiers.loc[len(self.identifiers)] = [immunespace_id, id_type, akc_id]
        else:
            akc_id = row.iloc[0].akc_id

        return akc_id

    def write_mapping_to_file(self, file_path):
        self.identifiers.to_csv(file_path, index=False, sep="\t")


def list_tables_from_db(db_path):
    with sqlite3.connect(db_path) as db_connection:
        df = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", db_connection)

    return df["name"].tolist() if not df.empty else []

def read_db_table_from_name(db_path, table_name):
    with sqlite3.connect(db_path) as db_connection:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", db_connection)

    return df.replace({"None": None, "": None})

def read_db_table_from_name_and_id(db_path, table_name, investigation_id, id_field_name="investigation_id"):
    query = f"SELECT * FROM {table_name} WHERE {id_field_name}='{investigation_id}'"

    with sqlite3.connect(db_path) as db_connection:
        df = pd.read_sql_query(query, db_connection)

    return df.replace({"None": None, "": None})

def read_db_table_from_query(db_path, query):
    with sqlite3.connect(db_path) as db_connection:
        df = pd.read_sql_query(query, db_connection)

    return df.replace({"None": None, "": None})

def list_to_query_repr(list_to_convert):
    return "('" + "', '".join(list_to_convert) + "')"

def table_to_permissible_values(hcc_db, table_name, label_name="label", curie_name="curie", offset ="    "):
    '''Utility function to convert an ImmuneSpace table to AK enum 'permissible values' section

    examples:

        table_to_permissible_values(hcc_kb_db, "exposure_material") # -> ExposureMaterialOntology

        table_to_permissible_values(hcc_kb_db, "event_type") # -> LifeEventProcessOntology

        table_to_permissible_values(hcc_kb_db, "disease") # -> DiseaseOntology
    '''

    table = read_db_table_from_name(hcc_db, table_name)

    print(f"{offset}permissible_values:")
    for index, row in table.iterrows():

        print(f"{offset}  {row[label_name]}:")
        print(f"{offset}    meaning: {row[curie_name]}")


# def format_id(investigation_id, item_name, item_id):
#     if item_id is None:
#         return None
#
#     # todo: these are not really curie's (only ImmuneSpace:investigation_id would be a valid curie)
#     # could include investigation_id
#     return f"ImmuneSpace:{item_name}-{item_id}"

def get_study_arms(hcc_db, investigation_id, id_handler):
    study_arms = []

    arm_table = read_db_table_from_name_and_id(hcc_db, "arm", investigation_id)

    for index, row in arm_table.iterrows():
        study_arms.append(
            StudyArm(akc_id=id_handler.get_akc_id(immunespace_id=row['arm_id'], id_type="arm"),
                     investigation=id_handler.get_akc_id(immunespace_id=row['investigation_id'], id_type="investigation"),
                     name=str(row["arm_name"]),
                     description=str(row["arm_description"])))

    return study_arms


def valid_biological_sex(value):
    if value == 'female':
        return 'PATO:0020002'
    elif value == 'male':
        return 'PATO:0020001'
    else:
        print(f"WARNING: Untranslated biological sex: {value}")
        return None

def get_participants(hcc_db, investigation_id, id_handler):
    ### seems like the participants table got simplified a lot and does not need to be joined with events
    # todo remove comments??

    # # x  phenotypic_sex -> not in immunespace/immport
    # #    race -> how to deal with race & race_specify?
    # #    strain -> not needed for human
    #
    # # Valid age fields are determined based on immport db values (age fields defined in lk_age_event, not overlapping with lk_t0_event)
    # # age_fields = get_valid_age_fields(immport_db)
    # age_fields = ('Age at Study Day 0', 'Age at enrollment', 'Age at infection', 'Age at initial treatment', 'Age at initial vaccine administration', 'Postmenstrual age')
    #
    # # query = f'''
    # #     SELECT p.*, p2a.arm_id, e.start, e.unit, e.t0_event_type
    # #     FROM participant p
    # #     JOIN participant_2_arm p2a ON p.participant_id = p2a.participant_id
    # #     LEFT JOIN event e ON p.participant_id = e.participant_id
    # #                      AND e.t0_event_type IN {age_fields};
    # #     '''
    # # # removed from event e because missing?:  # AND e.investigation_id = '{investigation_id}'
    # # # also removed: ORDER BY p.row_order
    # # # todo ask about this missing investigation id from table, or look once website is up again
    # #

    participant_table = read_db_table_from_name(hcc_db, "participant")

    participants = []


    for index, row in participant_table.iterrows():
        assert row['min_age'] == row['max_age'], f"AKC only handles one age, found min_age {row['min_age']} =/= max_age {row['max_age']}"

        participants.append(Participant(akc_id=id_handler.get_akc_id(immunespace_id=row['participant_id'], id_type="participant"),
                                        study_arm=id_handler.get_akc_id(immunespace_id=row['arm_id'], id_type="arm"),
                                        species="NCBITAXON:9606", # for now always human
                                        sex=valid_biological_sex(row['biological_sex']),
                                        age=row['min_age'],
                                        age_unit=row['age_unit'],
                                        age_event=row['age_event'],
                                        race=row['race'],
                                        ethnicity=row['ethnicity'],
                                        geolocation=row['geolocation'])) # GeolocationOntology,

    return participants


def get_references(hcc_db, investigation_id, id_handler):
    return []
    #  todo refrences has broken input data, remove this return statement once input is fixed

    publications_table = read_db_table_from_name_and_id(hcc_db, "publication", investigation_id)

    publications = []

    for index, row in publications_table.iterrows():
        sources = []

        if row['pubmed_id'] is not None:
            sources.append(Curie(f"PMID:{row['pubmed_id']}"))

        if row['doi'] is not None:
            sources.append(Curie(f"doi:{row['doi']}"))

        publications.append(Reference(source_uri=Curie(f"PMID:{row['pubmed_id']}"),
                                      sources=sources,
                                      investigations=id_handler.get_akc_id(immunespace_id=investigation_id, id_type="investigation"), # todo how to deal with multiple investigations if I only know 1?
                                      title=row["title"],
                                      authors=row["authors"].split(", ") if row["authors"] is not None else None,
                                      journal=row["journal"],
                                      issue=row["issue"],
                                      month=row["month"],
                                      year=row["year"],
                                      pages=row["pages"]))

    return publications


def get_investigation_partial(hcc_db, investigation_id, id_handler):
    # x   study_type -> ?
    # x   archival_id -> "Identifier for external archival resource for the investigation, e.g., BioProject"
    #     inclusion_criteria -> retrieved from immport (should it be in immuneSpace also?). I changed the type of this to 'multivalued'.
    #     exclusion_criteria
    #     release_date -> format: 2016-03-18 00:00:00
    #     update_date -> add to ImmuneSpace?
    #     participants
    # x   assays -> ! relevant data not in immuneSpace now, should be added?
    # x   simulations -> not needed
    #     documents
    #     conclusions

    # investigation_table = read_db_table_from_name_conditional(db, "investigation", f"WHERE investigation_id='{investigation_id}'")
    investigation_table = read_db_table_from_name_and_id(hcc_db, "investigation", investigation_id)

    assert len(investigation_table) == 1

    # todo get inclusion and exclusion criteria in immuneSpace
    # inc_exc_table = read_db_table_from_name_and_id(immport_db, "inclusion_exclusion", investigation_id, id_field_name="STUDY_ACCESSION")
    # inc_criteria = inc_exc_table[inc_exc_table["CRITERION_CATEGORY"] == "Inclusion"]["CRITERION"].tolist()
    # exc_criteria = inc_exc_table[inc_exc_table["CRITERION_CATEGORY"] == "Exclusion"]["CRITERION"].tolist()

    # inclusion_exclusion_criteria=inc_criteria + exc_criteria,
    # in immport, would have to be included in immunespace if deemed important
    # update_date=DateOrDatetime(get_updated_release_data(immport_db, investigation_id)))

    return (Investigation(akc_id=id_handler.get_akc_id(immunespace_id=investigation_id, id_type="investigation"), # f"ImmuneSpace:{investigation_table['investigation_id'][0]}",
                         investigation_type=Curie("OBI:0000066"), # according to James
                         archival_id=None,
                         release_date=DateOrDatetime(investigation_table["initial_data_release_date"][0])))

def row_to_description(row):
    '''Reformats a 'row' from a dataframe to a string describing the key-value pairs'''
    return "\n".join([f"{key} = {value}" for key, value in row.to_dict().items() if key not in ('row_number', 'row_order') and value is not None])


def format_type_subtype(row, type_field, subtype_field):
    name = f"{row[type_field]}"
    name += f" - {row[subtype_field]}" if row[subtype_field] is not None else ""

    return name

def get_study_events(hcc_db, investigation_id, id_handler):
    # info collected/reformatted from planned_event table
    # Note: some additional info may be in planned_visit table (only for the subset of planned events that are planned visits)
    #       this is currently not retrieved because it is unclear what information would be needed


    # {{}} represents planned_event_id to be filled in in query
    arms_query = f'''SELECT a2p.arm_id, a2p.planned_event_id
                FROM arm_2_planned_event a2p
                JOIN planned_event pe ON a2p.planned_event_id = pe.planned_event_id
                WHERE pe.investigation_id = '{investigation_id}'
                AND a2p.planned_event_id = '{{}}'
                '''

    planned_event_table = read_db_table_from_name_and_id(hcc_db, "planned_event", investigation_id)

    study_events = []

    for index, row in planned_event_table.iterrows():
        arms_for_event_query = arms_query.format(row["planned_event_id"])

        raw_arm_ids = read_db_table_from_query(hcc_db, arms_for_event_query)["arm_id"].tolist()
        arm_ids = [id_handler.get_akc_id(immunespace_id=raw_id, id_type="arm") for raw_id in raw_arm_ids]

        study_events.append(StudyEvent(akc_id=id_handler.get_akc_id(immunespace_id=row['planned_event_id'], id_type="planned_event"),
                                       name=format_type_subtype(row, "event_type", "event_subtype"),
                                       description=row_to_description(row),
                                       study_arms=arm_ids))
    return study_events


def get_life_events(hcc_db, investigation_id, id_handler):
    # 1:1 from ImmuneSpace 'event' table

    events_table = read_db_table_from_name(hcc_db, "event")

    life_events = []

    # todo study_event was formerly set to planned_event_id (which is sthe same, PV11666, for all events in this study)
    #  now this was changed to event_id, which seems to be unique for event+participant+study combo
    #  question for tuesday: should study_event be the same across all? or be this unique one??

    for index, row in events_table.iterrows():
        start = row['earliest_start']
        if row['latest_start'] is not None:
            assert start == row['latest_start'], f"AKC only handles one event start, found earliest_start {row['earliest_start']} =/= latest_start {row['latest_start']}"

        life_events.append(LifeEvent(akc_id=id_handler.get_akc_id(immunespace_id=row['event_id'], id_type="event"),
                                     participant=id_handler.get_akc_id(immunespace_id=row['participant_id'], id_type="participant"),
                                     study_event=id_handler.get_akc_id(immunespace_id=row['planned_event_id'], id_type="planned_event"),
                                     life_event_type=row['event_type'], # LifeEventProcessOntology
                                     geolocation=row['geolocation'], # GeolocationOntology
                                     # t0_event=row['t0_event'], # todo not in immunespace? I have study_time, earliest_start, latest_start (all the same thing)
                                     start=start,
                                     # duration=row['duration'], # todo don't have duration??
                                     time_unit=row['unit']))
    return life_events


def get_immune_exposures(hcc_db, investigation_id, id_handler):
    # 1:1 translation from immune_exposure table

    immune_exposures_table = read_db_table_from_name(hcc_db, "exposure")

    immune_exposures = []

    for index, row in immune_exposures_table.iterrows():
        immune_exposures.append(ImmuneExposure(akc_id=id_handler.get_akc_id(immunespace_id=row['event_id'], id_type="event"),
                                               exposure_material=row['exposure_material'],
                                               disease=row['disease'],
                                               disease_stage=row['disease_stage'],
                                               disease_severity=row['disease_severity']))

    return immune_exposures


def get_assessments(hcc_db, investigation_id, id_handler):
    # 1:1 translation from assessment table (note: this table is empty in the example)

    assessment_table = read_db_table_from_name(hcc_db, "assessment")

    assessments = []

    for index, row in assessment_table.iterrows():
        assessments.append(Assessment(akc_id=id_handler.get_akc_id(immunespace_id=row['assessment_id'], id_type="assessment"),
                                      life_event=id_handler.get_akc_id(immunespace_id=row['event_id'], id_type="event"),
                                      assessment_type=format_type_subtype(row, "assessment_type", "assessment_subtype"),
                                      target_entity_type=format_type_subtype(row, "target_entity_type", "assessment_subtypetarget_entity_subtype"),
                                      value=row["value"],
                                      unit=row["unit"],))

    return assessments

def get_specimens(hcc_db, investigation_id, id_handler):
    # 1:1 translation from specimen table

    specimen_table = read_db_table_from_name(hcc_db, "specimen")

    specimens = []

    for index, row in specimen_table.iterrows():
        specimens.append(Specimen(akc_id=id_handler.get_akc_id(immunespace_id=row['specimen_id'], id_type="specimen"),
                                  life_event=id_handler.get_akc_id(immunespace_id=row['event_id'], id_type="event"),
                                  # specimen_type=row['specimen_type'], # todo no longer in AKC, but could be useful somewhere? 'peripheral blood mononuclear cell'
                                  tissue=row['tissue']))


    return specimens

def get_akc_container(hcc_db, investigation_id, id_handler):
    #   investigations
    #   references
    #   study_arms
    #   study_events
    #   participants
    #   life_events
    #   immune_exposures
    #   assessments
    #   specimens
    # x specimen_collections # todo not in immuneSpace
    # x specimen_processings # todo not in immuneSpace
    # x assays # todo: capture specific Assay types in ImmuneSpace: AIRRSequencingAssay & TCellReceptorEpitopeBindingAssay
    # x datasets # todo does not match immuneSpace meaning
    #   conclusions
    # x chains # todo need to be added to immuneSpace or retrieved from ImmPort?
    # x tcell_receptors
    # x epitopes

    participants = get_participants(hcc_db, investigation_id, id_handler)
    references = get_references(hcc_db, investigation_id, id_handler)

    investigation = get_investigation_partial(hcc_db, investigation_id, id_handler)
    investigation.participants = [participant.akc_id for participant in participants]
    investigation.documents = [ref.source_uri for ref in references]
    # todo add investigation.assays??

    return AIRRKnowledgeCommons(investigations={investigation.akc_id: investigation},
                                references=references,
                                study_arms=get_study_arms(hcc_db, investigation_id, id_handler),
                                study_events=get_study_events(hcc_db, investigation_id, id_handler),
                                participants=participants,
                                life_events=get_life_events(hcc_db, investigation_id, id_handler),
                                immune_exposures=get_immune_exposures(hcc_db, investigation_id, id_handler),
                                assessments=get_assessments(hcc_db, investigation_id, id_handler),
                                specimens=get_specimens(hcc_db, investigation_id, id_handler))


    # intentionally omitted (not expected to be in immunespace as direct field):
    # repertoire_id
    # cell_number	cells_per_reaction
    # cell_storage	cell_quality	cell_isolation	cell_processing_protocol	template_class	template_quality
    # template_amount	template_amount_unit	library_generation_method	library_generation_protocol
    # library_generation_kit_version	complete_sequences	physical_linkage
    # total_reads_passing_qc_filter	sequencing_platform	sequencing_facility	sequencing_run_date	sequencing_kit
    # pcr_target.0.pcr_target_locus	pcr_target.0.forward_pcr_primer_target_location
    # pcr_target.0.reverse_pcr_primer_target_location
    # sequencing_files.sequencing_data_id	sequencing_files.file_type	sequencing_files.filename
    # sequencing_files.read_direction	sequencing_files.read_length	sequencing_files.paired_filename
    # sequencing_files.paired_read_direction	sequencing_files.paired_read_length	sequencing_files.index_filename
    # sequencing_files.index_length


def main():
    ak_schema_root = Path(os.path.dirname(__file__)) / "../../../"

    investigation_id = "SDY2107"
    # immport_db = ak_schema_root / "src/data/immunespace_example_data/immport_nanobot.db"
    hcc_db = ak_schema_root / "src/data/immunespace_example_data/SDY2107.db"
    output_folder = ak_schema_root / f"examples/immunespace/"

    output_file = output_folder / f"investigation_{investigation_id}.json"
    id_file = output_folder / f"{investigation_id}_ids.tsv"

    id_handler = IdentifierHandler(id_file)


    akc_container = get_akc_container(hcc_db, investigation_id, id_handler)

    with open(output_file, "w") as file:
        print(json_dumper.dumps(akc_container), file=file)

    id_handler.write_mapping_to_file(id_file)


main()


# Note: can also get from immPort
# - Subject 2 biosample: https://hcc-kb-dev.lji.org/SDY460/immport/biosample
# - HLA type: https://hcc-kb-dev.lji.org/SDY888/immport/hla_typing_result
# - grant: https://hcc-kb-dev.lji.org/SDY460/immport/contract_grant


# - file_info https://hcc-kb-dev.lji.org/SDY888/immport/file_info
# - experiment (describes 'IGH sequencing') https://hcc-kb-dev.lji.org/SDY460/immport/experiment
# --- expsample (more sequencing details) https://hcc-kb-dev.lji.org/SDY460/immport/expsample
# --- protocol (describes protocol for sequencing experiment) https://hcc-kb-dev.lji.org/SDY460/immport/protocol
# --- treatment "Action applied to a sample ex vivo by an agent (e.g. a compound), a temperature change, and or a duration of some action (e.g. a time course)." https://hcc-kb-dev.lji.org/SDY888/immport/treatment


# ELISA/ELISPOT/HAI/FCS is directly captured and stored in ImmPort. Should something be added for AIRR assay?

