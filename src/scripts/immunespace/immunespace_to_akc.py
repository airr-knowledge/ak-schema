from src.ak_schema.datamodel.ak_schema import *
from linkml_runtime.dumpers import yaml_dumper, json_dumper

import pandas as pd
import sqlite3
import os
from pathlib import Path


def list_tables_from_db(db_path):
    with sqlite3.connect(db_path) as db_connection:
        df = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", db_connection)

    return df["name"].tolist() if not df.empty else []

def read_db_table_from_name(db_path, table_name):
    with sqlite3.connect(db_path) as db_connection:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", db_connection)

    return df

def read_db_table_from_name_and_id(db_path, table_name, investigation_id, id_field_name="investigation_id"):
    query = f"SELECT * FROM {table_name} WHERE {id_field_name}='{investigation_id}'"

    with sqlite3.connect(db_path) as db_connection:
        df = pd.read_sql_query(query, db_connection)

    return df

def read_db_table_from_query(db_path, query):
    with sqlite3.connect(db_path) as db_connection:
        df = pd.read_sql_query(query, db_connection)

    return df

def list_to_query_repr(list_to_convert):
    return "('" + "', '".join(list_to_convert) + "')"

def table_to_permissible_values(hcc_db, table_name, label_name="label", curie_name="curie", offset ="    "):
    '''Utility function to convert an ImmuneSpace table to AK enum 'permissible values' section

    examples:

        table_to_permissible_values(hcc_kb_db, "exposure_material") # -> ExposureMaterialOntology

        table_to_permissible_values(hcc_kb_db, "event_type") # -> LifeEventProcessOntology

        table_to_permissible_values(hcc_kb_db, "disease") # -> DiseaseOntology
    '''

    immune_exposures_table = read_db_table_from_name(hcc_db, table_name)

    print(f"{offset}permissible_values:")
    for index, row in immune_exposures_table.iterrows():

        print(f"{offset}  {row[label_name]}:")
        print(f"{offset}    meaning: {row[curie_name]}")


def format_id(investigation_id, item_name, item_id):
    if item_id is None:
        return None

    # todo: these are not really curie's (only ImmuneSpace:investigation_id would be a valid curie)
    # could include investigation_id
    return f"ImmuneSpace:{item_name}-{item_id}"

def get_study_arms(hcc_db, investigation_id):
    #   investigation
    #   inclusion_criteria
    # x exclusion_criteria

    study_arms = []

    arm_table = read_db_table_from_name_and_id(hcc_db, "arm", investigation_id)

    for index, row in arm_table.iterrows():
        study_arms.append(
            StudyArm(akc_id=format_id(investigation_id, 'arm', row['arm_id']),
                     investigation=format_id(investigation_id, 'investigation', row['investigation_id']),
                     name=str(row["arm_name"]),
                     description=str(row["arm_description"])))

    return study_arms
#
# def safe_get_ontology(ontology_cls, value):
#     return None if value is None else ontology_cls(value)


def valid_biological_sex(value):
    if value == 'female':
        return 'PATO:0020002'
    elif value == 'male':
        return 'PATO:0020001'
    else:
        print(f"WARNING: Untranslated biological sex: {value}")
        return None

def get_valid_age_fields(immport_db):
    query = '''SELECT NAME FROM lk_age_event WHERE NAME NOT IN (SELECT NAME FROM lk_t0_event)'''
    age_names = read_db_table_from_query(immport_db, query)["NAME"].tolist()

    return list_to_query_repr(age_names)

def get_participants(hcc_db, immport_db, investigation_id):
    # x  phenotypic_sex -> not in immunespace/immport
    #    race -> how to deal with race & race_specify?
    #    strain -> not needed for human

    # Valid age fields are determined based on immport db values (age fields defined in lk_age_event, not overlapping with lk_t0_event)
    age_fields = get_valid_age_fields(immport_db)

    query = f'''
        SELECT p.*, p2a.arm_id, e.start, e.unit, e.t0_event_type
        FROM participant p
        JOIN participant_2_arm p2a ON p.participant_id = p2a.participant_id
        LEFT JOIN event e ON p.participant_id = e.participant_id 
                         AND e.investigation_id = '{investigation_id}' 
                         AND e.t0_event_type IN {age_fields}
        ORDER BY p.row_order;
        '''

    participant_table = read_db_table_from_query(hcc_db, query)

    participants = []

    for index, row in participant_table.iterrows():
        print(row)
        participants.append(Participant(akc_id=format_id(investigation_id, 'participant', row['participant_id']),
                                        study_arm=format_id(investigation_id, 'arm', row['arm_id']),
                                        species="NCBITAXON:9606", # for now always human
                                        sex=valid_biological_sex(row['biological_sex']),
                                        age=row['start'],
                                        age_unit=row['unit'], # todo AgeUnitOntology dynamic fields doesnt work yet
                                        age_event=row['t0_event_type'], # "Age at Study Day 0" or "Age at enrollment"
                                        race=row['race'],
                                        ethnicity=row['ethnicity'],
                                        geolocation=row['geolocation'])) # GeolocationOntology,

    return participants


def get_references(hcc_db, investigation_id):
    #    investigations -> can only list one! there is only one for an immunespace study.

    publications_table = read_db_table_from_name_and_id(hcc_db, "publication", investigation_id, "study_accession")

    publications = []

    for index, row in publications_table.iterrows():
        sources = []

        if row['pubmed_id'] is not None:
            sources.append(Curie(f"PMID:{row['pubmed_id']}"))

        if row['doi'] is not None:
            sources.append(Curie(f"doi:{row['doi']}"))

        publications.append(Reference(source_uri=Curie(f"PMID:{row['pubmed_id']}"),
                                      sources=sources,
                                      investigations=format_id(investigation_id, "investigation", investigation_id), # todo how to deal with multiple investigations if I only know 1?
                                      title=row["title"],
                                      authors=row["authors"].split(", ") if row["authors"] is not None else None, # todo is the format always the same?
                                      journal=row["journal"],
                                      issue=row["issue"],
                                      month=row["month"],
                                      year=row["year"],
                                      pages=row["pages"]))

    return publications

def get_udpated_release_data(immport_db, investigation_id):
    query = f'''SELECT s.DATA_RELEASE_DATE 
    FROM study_data_release s
    WHERE s.STUDY_ACCESSION='{investigation_id}'
    AND s.STATUS='Updated'
    AND s.DATA_RELEASE_VERSION = (SELECT MAX(DATA_RELEASE_VERSION) FROM study_data_release);
    '''

    release_date_table = read_db_table_from_query(immport_db, query)

    if len(release_date_table) == 0:
        return None
    else:
        return release_date_table["DATA_RELEASE_DATE"][0]

def get_investigation_partial(hcc_db, immport_db, investigation_id):
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

    inc_exc_table = read_db_table_from_name_and_id(immport_db, "inclusion_exclusion", investigation_id, id_field_name="STUDY_ACCESSION")
    inc_criteria = inc_exc_table[inc_exc_table["CRITERION_CATEGORY"] == "Inclusion"]["CRITERION"].tolist()
    exc_criteria = inc_exc_table[inc_exc_table["CRITERION_CATEGORY"] == "Exclusion"]["CRITERION"].tolist()

    return Investigation(akc_id=format_id(investigation_id, "investigation", investigation_id), # f"ImmuneSpace:{investigation_table['investigation_id'][0]}",
                         investigation_type=Curie("OBI:0000066"), # according to James
                         archival_id=None,
                         inclusion_exclusion_criteria=inc_criteria + exc_criteria,
                         release_date=DateOrDatetime(investigation_table["initial_data_release_date"][0]),
                         update_date=DateOrDatetime(get_udpated_release_data(immport_db, investigation_id)))



def row_to_description(row):
    '''Reformats a 'row' from a dataframe to a string describing the key-value pairs'''
    return "\n".join([f"{key} = {value}" for key, value in row.to_dict().items() if key not in ('row_number', 'row_order') and value is not None])


def format_type_subtype(row, type_field, subtype_field):
    name = f"{row[type_field]}"
    name += f" - {row[subtype_field]}" if row[subtype_field] is not None else ""

    return name

def get_study_events(hcc_db, investigation_id):
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
        arm_ids = [format_id(investigation_id, 'arm', raw_id) for raw_id in raw_arm_ids]

        study_events.append(StudyEvent(akc_id=format_id(investigation_id, 'plannedevent', row['planned_event_id']),
                                       name=format_type_subtype(row, "event_type", "event_subtype"),
                                       description=row_to_description(row),
                                       study_arms=arm_ids))
    return study_events


def get_life_events(hcc_db, investigation_id):
    # 1:1 from ImmuneSpace 'event' table

    events_table = read_db_table_from_name_and_id(hcc_db, "event", investigation_id)

    life_events = []


    for index, row in events_table.iterrows():
        life_events.append(LifeEvent(akc_id=format_id(investigation_id, 'event', row['event_id']),
                                     participant=format_id(investigation_id, 'participant', row['participant_id']),
                                     study_event=format_id(investigation_id, 'plannedevent', row['planned_visit_id']),
                                     life_event_type=row['event_type'], # LifeEventProcessOntology
                                     geolocation=row['geolocation'], # GeolocationOntology
                                     t0_event=row['t0_event'],
                                     # t0_event_type=row['t0_event_type'], # field that formerly existed, the value is for instance 'Age at study day 0'
                                     start=row['start'],
                                     duration=row['duration'],
                                     time_unit=row['unit']))
    return life_events


def get_immune_exposures(hcc_db, investigation_id):
    # 1:1 translation from immune_exposure table

    immune_exposures_table = read_db_table_from_name(hcc_db, "immune_exposure")

    immune_exposures = []

    for index, row in immune_exposures_table.iterrows():
        immune_exposures.append(ImmuneExposure(akc_id=format_id(investigation_id, 'immuneexposure', row['event_id']),
                                               # life_event=format_id(investigation_id, 'event', row['event_id']),
                                               exposure_material=row['exposure_material'],
                                               disease=row['disease'],
                                               disease_stage=row['disease_stage'],
                                               disease_severity=row['disease_severity']))

    return immune_exposures


def get_assessments(hcc_db, investigation_id):
    # 1:1 translation from assessment table (note: this table is empty in the example)

    assessment_table = read_db_table_from_name(hcc_db, "assessment")

    assessments = []

    for index, row in assessment_table.iterrows():
        assessments.append(Assessment(akc_id=format_id(investigation_id, 'assessment', row['assessment_id']),
                                      life_event=format_id(investigation_id, 'event', row['event_id']),
                                      assessment_type=format_type_subtype(row, "assessment_type", "assessment_subtype"),
                                      target_entity_type=format_type_subtype(row, "target_entity_type", "assessment_subtypetarget_entity_subtype"),
                                      value=row["value"],
                                      unit=row["unit"],))

    return assessments

def get_specimens(hcc_db, investigation_id):
    # 1:1 translation from specimen table

    specimen_table = read_db_table_from_name(hcc_db, "specimen")

    specimens = []

    for index, row in specimen_table.iterrows():
        specimens.append(Specimen(akc_id=format_id(investigation_id, 'specimen', row['specimen_id']),
                                  life_event=format_id(investigation_id, 'event', row['event_id']),
                                  # specimen_type=row['specimen_type'], # no longer in AKC, but could be useful somewhere? 'peripheral blood mononuclear cell'
                                  tissue=row['tissue']))


    return specimens

def get_datasets(hcc_db, investigation_id):
    # todo get assays first

    # In ImmuneSpace, dataset table has: dataset_id, description, arm_id, assay_type, target_entity_type, planned_event_id
    # In AKC, it's akc_id, assessments, assays

    # akc_id: Union[str, DatasetAkcId] = None
    # assessments: Optional[Union[Union[str, AssessmentAkcId], List[Union[str, AssessmentAkcId]]]] = empty_list()
    # assays: Optional[Union[Union[str, AssayAkcId], List[Union[str, AssayAkcId]]]] = empty_list()

    return []

def get_conclusions(hcc_db, investigation_id):
    # 1:1 conversion from signature table (with addition of 'results' field)
    # (note: this table is empty in the example)

    signature_table = read_db_table_from_name(hcc_db, "signature")

    conclusions = []

    for index, row in signature_table.iterrows():

        data_id_query = f'''
                SELECT s2a.dataset_id
                FROM signature_2_dataset s2a
                WHERE s2a.signature_id = '{row['signature_id']}'
                '''

        dataset_ids = read_db_table_from_query(hcc_db, data_id_query)["dataset_id"].tolist()

        conclusions.append(Conclusion(akc_id=format_id(investigation_id, 'signature', row['signature_id']),
                                      investigations=investigation_id,
                                      datasets=dataset_ids,
                                      description=row['description'],
                                      data_location_type=row['data_location_type'],
                                      data_location_value=row['data_location_value'],
                                      organism=row['organism'],
                                      experiment_type=row['experiment_type'],
                                      result=None)) # todo what is 'result'?

    return conclusions

def get_akc_container(hcc_db, immport_db, investigation_id):
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

    participants = get_participants(hcc_db, immport_db, investigation_id)
    references = get_references(hcc_db, investigation_id)
    conclusions = get_conclusions(hcc_db, investigation_id)

    investigation = get_investigation_partial(hcc_db, immport_db, investigation_id)
    investigation.participants = [participant.akc_id for participant in participants]
    investigation.documents = [ref.source_uri for ref in references]
    investigation.conclusions = [concl.akc_id for concl in conclusions]
    # todo add investigation.assays

    return AIRRKnowledgeCommons(investigations=investigation,
                                references=references,
                                study_arms=get_study_arms(hcc_db, investigation_id),
                                study_events=get_study_events(hcc_db, investigation_id),
                                participants=participants,
                                life_events=get_life_events(hcc_db, investigation_id),
                                immune_exposures=get_immune_exposures(hcc_db, investigation_id),
                                assessments=get_assessments(hcc_db, investigation_id),
                                specimens=get_specimens(hcc_db, investigation_id),
                                datasets=get_datasets(hcc_db, investigation_id),
                                conclusions=conclusions)

def main():
    # todo: much of this stuff should be moved to a make file

    ak_schema_root = Path(os.path.dirname(__file__)) / "../../../"

    investigation_id = "SDY460"
    immport_db = ak_schema_root / "src/data/immunespace_example_data/immport_nanobot.db"
    hcc_db = ak_schema_root / "src/data/immunespace_example_data/hcc_kb_nanobot.db"
    output_file = ak_schema_root / f"examples/immunespace/investigation_{investigation_id}.json"

    akc_container = get_akc_container(hcc_db, immport_db, investigation_id)

    with open(output_file, "w") as file:
        print(json_dumper.dumps(akc_container), file=file)

# main()


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

