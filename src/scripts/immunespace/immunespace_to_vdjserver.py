import os
from pathlib import Path
from immunespace_to_akc import read_db_table_from_query



def get_subject_metadata_tsv(hcc_db):
    # join on these tables:
    # **** event : ['event_id', 'participant_id', 'planned_event_id', 'event_type', 'geolocation', 'study_time', 'earliest_start', 'latest_start', 'unit']
    # **** exposure : ['event_id', 'exposure_material', 'disease', 'disease_stage', 'disease_severity']

    query = f'''
            SELECT p.*, a.*, ex.*
            FROM participant p
            JOIN participant_2_arm p2a ON p2a.participant_id = p.participant_id
            JOIN arm a ON p2a.arm_id = a.arm_id
            LEFT JOIN event ev ON p.participant_id = ev.participant_id
            LEFT JOIN exposure ex ON ev.event_id = ex.event_id
            '''

    subject_metadata = read_db_table_from_query(hcc_db, query)

    # Omitted AIRR fields:
    # disease_length, prior_therapies, intervention, medical_history, ancestry_population, strain_name, linked_subjects, link_type

    mapping = {"participant_id": "subject_id",
               "biological_sex": "sex",
               "min_age": "age_min",
               "max_age": "age_max",
               "age_unit": "age_unit",
               "age_event": "age_event",
               "ethnicity": "ethnicity",
               "race": "race",
               "arm_description": "diagnosis.0.study_group_description",
               "disease": "diagnosis.0.disease_diagnosis",
               "disease_stage": "diagnosis.0.disease_stage",
               "exposure_material": "diagnosis.0.immunogen"}

    subject_metadata.rename(columns=mapping, inplace=True)
    subject_metadata = subject_metadata[mapping.values()]

    subject_metadata["synthetic"] = "false"
    subject_metadata["species"] = "NCBITAXON:9606"

    subject_metadata.replace({"None": "",  None: ""}, inplace=True)

    return subject_metadata


def get_sample_processing_metadata_tsv(hcc_db):
    # join on these tables:
    # **** specimen : ['specimen_id', 'event_id', 'participant_id', 'specimen_type', 'tissue', 'process']
    # **** event : ['event_id', 'participant_id', 'planned_event_id', 'event_type', 'geolocation', 'study_time', 'earliest_start', 'latest_start', 'unit']
    # potential relevant table: immunespace specimen.process, not currenlty used

    query = f'''
            SELECT s.*, ev.*
            FROM specimen s
            LEFT JOIN event ev ON ev.event_id = s.event_id WHERE ev.event_type='specimen collection'
            ''' # todo somehow subset on the events associated with a BCR/TCR sequencing sample? -> can only implement once SRA datasets have been added

    sample_metadata = read_db_table_from_query(hcc_db, query)


    mapping = {"participant_id": "subject_id",
               # ".": "sample_processing_id",
               "specimen_id": "sample_id",
               "specimen_type": "sample_type", # lung/bone marrow/skin/etc
               "tissue": "tissue",
               # ".": "anatomic_site",
               # ".": "disease_state_sample", # I believe we have disease state as part of exposure but not linked to sample
               "study_time": "collection_time_point_relative",
               "unit": "collection_time_point_relative_unit",
               # ".": "collection_time_point_reference", # ???
               # ".": "biomaterial_provider", # ???
               # ".": "tissue_processing", # I do have 'specimen.process', not sure if the same, is None in this dataset
               # ".": "cell_subset",
               # ".": "cell_phenotype",
               # ".": "cell_species",
               # ".": "single_cell", # inferred if GEO?
               # ".": "sequencing_run_id", # SRA ref!! SRR...
               }

    sample_metadata.rename(columns=mapping, inplace=True)
    sample_metadata = sample_metadata[mapping.values()]

    sample_metadata.replace({"None": "", None: ""}, inplace=True)

    return sample_metadata


def main():
    ak_schema_root = Path(os.path.dirname(__file__)) / "../../../"

    investigation_id = "SDY2107"
    hcc_db = ak_schema_root / "src/data/immunespace_example_data/SDY2107.db"
    output_folder = ak_schema_root / f"examples/immunespace/"

    subject_metadata = get_subject_metadata_tsv(hcc_db)
    sample_processing_metadata = get_sample_processing_metadata_tsv(hcc_db)

    subject_metadata.to_csv(str(output_folder / f"subject_metadata_{investigation_id}.tsv"), index=False, sep="\t")
    sample_processing_metadata.to_csv(str(output_folder / f"sample_processing_metadata_{investigation_id}.tsv"), index=False, sep="\t")


main()
