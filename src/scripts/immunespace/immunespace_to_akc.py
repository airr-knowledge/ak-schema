from src.ak_schema.datamodel.ak_schema import *

import pandas as pd
import sqlite3


pd.set_option('display.max_columns', None)

immport_db = '/Users/lscheffer/PycharmProjects/ak-schema/src/data/immunespace_example_data/immport_nanobot.db'
hcc_kb_db = '/Users/lscheffer/PycharmProjects/ak-schema/src/data/immunespace_example_data/hcc_kb_nanobot.db'


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


# def read_db_table_from_name_conditional(db_path, table_name, conditional_str):
#     with sqlite3.connect(db_path) as db_connection:
#         df = pd.read_sql_query(f"SELECT * FROM {table_name} {conditional_str}", db_connection)
#
#     return df

def whereis(field_to_look_for, db_path):
    all_tables = list_tables_from_db(db_path)

    for table_name in all_tables:
        try:
            imported_table = read_db_table_from_name(db_path, table_name)
            if field_to_look_for.upper() in [col.upper() for col in imported_table.columns]:
                if len(imported_table) > 0:
                    print("-", table_name)
                    print(imported_table)
                else:
                    print("-", table_name, "(empty)")
        except Exception:
            pass

def format_id(investigation_id, item_name, item_id):
    # could include investigation_id
    return f"ImmuneSpace:{item_name}-{item_id}"

def get_study_arms(db, investigation_id):
    #   investigation
    #   inclusion_criteria
    # x exclusion_criteria

    study_arms = []

    arm_table = read_db_table_from_name_and_id(db, "arm", investigation_id)

    # arm_table = read_db_table_from_name_conditional(hcc_kb_db, "arm", f"WHERE investigation_id='{investigation_id}'")

    for index, row in arm_table.iterrows():
        study_arms.append(
            StudyArm(akc_id=format_id(investigation_id, 'arm', row['arm_id']),
                     investigation=f"ImmuneSpace:{row['investigation_id']}",
                     inclusion_criteria=str(row["arm_description"]),
                     exclusion_criteria=None))

    return study_arms

def safe_get_ontology(ontology_cls, value):
    try:
        ontology = ontology_cls(value)
    except ValueError:
        ontology = value

    return ontology


def get_participants(db, investigation_id):
    # note (James, Scott?): for now ontologies are converted directly from str representation. is this sufficient?
    # immuneSpace also has other tables linking to curie/parent etc, but I think

    #    akc_id
    #    study_arm
    #    species -> always human
    #    biological_sex
    # x  phenotypic_sex
    #    age -> age. in immunespace is at "Age at Study Day 0"
    #    age_unit
    #    age_event -> now  "Age at Study Day 0" (alternative could be: e.event_type = vaccination)
    #    race -> how to deal with race & race_specify?
    #    ethnicity
    #    geolocation
    #    strain -> not needed for human

    # Valid age fields are from 'lk_age_event' https://gitlab.lji.org/hip3c/knowledgebase/hcc-knowledgebase/-/blob/master/src/immport/lk_age_event.tsv
    # Excluded: "Not Specified" and "Other", as these also occur in 'lk_t0_event' (which are not-age events) https://gitlab.lji.org/hip3c/knowledgebase/hcc-knowledgebase/-/blob/master/src/immport/lk_t0_event.tsv
    age_fields = ["Postmenstrual age", "Age at Study Day 0", "Age at enrollment", "Age at infection", "Age at initial treatment", "Age at initial vaccine administration"]
    age_fields_repr = "('" + "', '".join(age_fields) + "')"

    query = f'''
        SELECT p.*, p2a.arm_id, e.start, e.unit, e.t0_event_type
        FROM participant p
        JOIN participant_2_arm p2a ON p.participant_id = p2a.participant_id
        LEFT JOIN event e ON p.participant_id = e.participant_id 
                         AND e.investigation_id = '{investigation_id}' 
                         AND e.t0_event_type IN {age_fields_repr}
        ORDER BY p.row_order;
        '''

    participant_table = read_db_table_from_query(db, query)

    participants = []

    for index, row in participant_table.iterrows():
        participants.append(Participant(akc_id=format_id(investigation_id, 'participant', row['participant_id']), # @Scott/James not sure if subject ids are the same across studies or if we'd anyways still want to combine study+subject ID here
                                        study_arm=f"ImmuneSpace:{row['arm_id']}",
                                        species=safe_get_ontology(SpeciesOntology, "NCBITAXON:9606"), # = always Homo sapiens (human)
                                        biological_sex=safe_get_ontology(BiologicalSexOntology, row['biological_sex']),
                                        age=row['start'],
                                        age_unit=safe_get_ontology(AgeUnitOntology, row['unit']),
                                        age_event=row['t0_event_type'], # "Age at Study Day 0" or "Age at enrollment"
                                        race=safe_get_ontology(RaceOntology, row['race']),
                                        ethnicity=safe_get_ontology(EthnicityOntology, row['ethnicity']),
                                        geolocation=safe_get_ontology(GeolocationOntology, row['geolocation'])))

    return participants


def get_references(db, investigation_id):
    #    source_uri: @Scott: difference between source_uri (1) and sources (multiple)? immunespace has doi and pmid
    #    sources
    #    investigations -> can only list one! there is only one for an immunespace study.
    #    title
    #    authors
    #    journal
    #    issue
    #    month
    #    year
    #    pages

    # publications_table = read_db_table_from_name_conditional(db, "publication", f"WHERE study_accession='{investigation_id}'")
    publications_table = read_db_table_from_name_and_id(db, "publication", investigation_id, "study_accession")

    publications = []

    for index, row in publications_table.iterrows():
        sources = []

        if row['pubmed_id'] is not None:
            sources.append(Curie(f"PMID:{row['pubmed_id']}"))

        if row['doi'] is not None:
            sources.append(Curie(f"doi:{row['doi']}"))

        publications.append(Reference(source_uri=Curie(f"PMID:{row['pubmed_id']}"),
                                      sources=sources,
                                      investigations=f"ImmuneSpace:{investigation_id}", # todo how to deal with multiple investigations if I only know 1?
                                      title=row["title"],
                                      authors=row["authors"].split(", ") if row["authors"] is not None else None, # @James is the format always the same?
                                      journal=row["journal"],
                                      issue=row["issue"],
                                      month=row["month"],
                                      year=row["year"],
                                      pages=row["pages"]))

    return publications

def get_investigation_partial(db, investigation_id):
    # o   study_type -> @James I do not believe there is a 'study type' that can be inferred from these tables?
    # x   archival_id -> "Identifier for external archival resource for the investigation, e.g., BioProject" @Scott curie to https://immunespace.org/query/study/SDY460 sufficient? can also retrieve BioProject from linked ImmPort data
    # x  inclusion_criteria -> @James/Scott: immunespace does not have this on 'investigation' level?
    # x  exclusion_criteria
    #    release_date -> format: 2016-03-18 00:00:00
    # x  update_date -> @James said: I think ImmPort does have some sort of "study updated date" field, so we can add that to ImmuneSpace
    #     participants
    # o   assays -> ! relevant data not in immuneSpace now, should be added?
    # o   simulations -> @Scott ??
    #     documents
    # o   conclusions -> @Scott ??

    # investigation_table = read_db_table_from_name_conditional(db, "investigation", f"WHERE investigation_id='{investigation_id}'")
    investigation_table = read_db_table_from_name_and_id(db, "investigation", investigation_id)

    assert len(investigation_table) == 1

    return Investigation(akc_id=f"ImmuneSpace:{investigation_table['investigation_id'][0]}",
                         study_type=Curie("OBI:0000066"), # according to James
                         archival_id=None,
                         release_date=DateOrDatetime(investigation_table["initial_data_release_date"][0]),
                         participants=None, #to be filled in  #get_participants(db, investigation_id),
                         assays=None,
                         documents=None) #  #to be filled in  get_documents(db, investigation_id))

# get_investigation_partial(hcc_kb_db, "SDY460")

def row_to_description(row):
    '''Reformats a 'row' from a dataframe to a string describing the key-value pairs'''
    return "\n".join([f"{key} = {value}" for key, value in row.to_dict().items() if key not in ('row_number', 'row_order') and value is not None])


def get_planned_events(db, investigation_id):
    #    akc_id
    #    description
    #    name
    #    study_arms


    # {{}} represents planned_event_id to be filled in in query
    arms_query = f'''SELECT a2p.arm_id, a2p.planned_event_id
                FROM arm_2_planned_event a2p
                JOIN planned_event pe ON a2p.planned_event_id = pe.planned_event_id
                WHERE pe.investigation_id = '{investigation_id}'
                AND a2p.planned_event_id = '{{}}'
                '''

    planned_event_table = read_db_table_from_name_and_id(db, "planned_event", investigation_id)

    study_events = []

    for index, row in planned_event_table.iterrows():
        name = f"{row['event_type']}"
        name += f" - {row['event_subtype']}" if row['event_subtype'] is not None else ""

        arms_for_event_query = arms_query.format(row["planned_event_id"])

        raw_arm_ids = read_db_table_from_query(db, arms_for_event_query)["arm_id"].tolist()
        arm_ids = [format_id(investigation_id, 'arm', raw_id) for raw_id in raw_arm_ids]

        study_events.append(StudyEvent(akc_id=format_id(investigation_id, 'studyevent', row['planned_event_id']),
                                       name=name,
                                       description=row_to_description(row),
                                       study_arms=arm_ids))

def get_planned_visits(db, investigation_id):
    #    akc_id
    #    description
    #    name
    #    study_arms

    # {{}} represents planned_event_id to be filled in in query
    arms_query = f'''SELECT a2p.arm_id, pv.planned_visit_id
                    FROM arm_2_planned_event a2p
                    JOIN planned_visit pv ON a2p.planned_event_id = pv.planned_visit_id
                    WHERE pv.investigation_id = '{investigation_id}'
                    AND a2p.planned_event_id = '{{}}'
                    '''


    planned_visits = []

    planned_visit_table = read_db_table_from_name_and_id(db, "planned_visit", investigation_id)

    for index, row in planned_visit_table.iterrows():

        arms_for_event_query = arms_query.format(row["planned_visit_id"])
        raw_arm_ids = read_db_table_from_query(db, arms_for_event_query)["arm_id"].tolist()
        arm_ids = [format_id(investigation_id, 'arm', raw_id) for raw_id in raw_arm_ids]

        planned_visits.append(StudyEvent(akc_id=format_id(investigation_id, 'plannedvisit', row['planned_visit_id']),
                                         name=row['name'],
                                         description=row_to_description(row),
                                         study_arms=arm_ids))

    return planned_visits

def get_study_events(db, investigation_id):
    # study_events are a combination of planned events and planned visits

    return get_planned_events(db, investigation_id) # + get_planned_visits(db, investigation_id)


def get_life_events(db, investigation_id):
    # 1:1 from ImmuneSpace 'event' table

    events_table = read_db_table_from_name_and_id(db, "event", investigation_id)

    life_events = []

    for index, row in events_table.iterrows():
        life_events.append(LifeEvent(akc_id=format_id(investigation_id, 'lifeevent', row['event_id']),
                                     participant=format_id(investigation_id, 'participant', row['participant_id']),
                                     study_event=format_id(investigation_id, 'plannedvisit', row['planned_visit_id']),
                                     life_event_type=safe_get_ontology(LifeEventProcessOntology, row['event_type']),
                                     geolocation=safe_get_ontology(GeolocationOntology, row['geolocation']),
                                     t0_event=row['t0_event'],
                                     t0_event_type=row['t0_event_type'],
                                     start=row['start'],
                                     duration=row['duration'],
                                     time_unit=row['unit']))
    return life_events


def get_immune_exposures(db, investigation_id):
    # akc_id: Union[str, ImmuneExposureAkcId] = None
    # life_event: Optional[Union[str, LifeEventAkcId]] = None
    # exposure_material: Optional[Union[str, "ExposureMaterialOntology"]] = None
    # disease: Optional[Union[str, "DiseaseOntology"]] = None
    # disease_stage: Optional[str] = None
    # disease_severity: Optional[str] = None
    query='''
    '''

    print(read_db_table_from_name(db, "exposure_process")["label"])

    ImmuneExposure()

print(get_life_events(hcc_kb_db, "SDY460"))
# get_immune_exposures(hcc_kb_db, "SDY460")

def get_akc_container(db, investigation_id):
    #   investigations
    #   references
    #   study_arms
    #   study_events
    #   participants
    #   life_events
    # x immune_exposures
    # x assessments
    # x specimens
    # x specimen_collections
    # x specimen_processings
    # x assays
    # x datasets
    # x conclusions
    # x chains
    # x tcell_receptors
    # x epitopes

    participants = get_participants(db, investigation_id)
    references = get_references(db, investigation_id)

    investigation = get_investigation_partial(db, investigation_id)
    investigation.participants = [participant.akc_id for participant in participants]
    investigation.documents = [ref.source_uri for ref in references]

    return AIRRKnowledgeCommons(study_events=get_study_events(db, investigation_id),
                                study_arms=get_study_arms(db, investigation_id),
                                life_events=get_life_events(db, investigation_id),
                                participants=participants,
                                references=references)

# get_akc_container(hcc_kb_db, "SDY460")


# For each row in the TCell table, generate:
# 1 study arm
# 1 study events: specimen collection
# 1 participant
# 2 life events: 1st in vivo Process, specimen collection
# 1 immune exposure: 1st in vivo Process
# 0 assessments
# 1 specimen
# 1 assay
# 1 epitope
# 1+ t cell receptors
# 2 chains per TCR
# 1 dataset
# 1 conclusion
