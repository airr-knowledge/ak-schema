import os
import unittest
from pathlib import Path

from src.ak_schema.datamodel.ak_schema import *
import src.scripts.immunespace.immunespace_to_akc as i2a
import src.scripts.immunespace.immunespace_to_vdjserver as i2v

ROOT = Path(os.path.dirname(__file__)) / "../../../"
DATA_DIR = ROOT / "src/data/immunespace_example_data"
STUDY_DB_FILE = DATA_DIR / "SDY2107.db"


STUDY_ID = "SDY2107"
ID_HANDLER = i2a.IdentifierHandler()
INVESTIGATION_KEY = ID_HANDLER.get_akc_id(immunespace_id=STUDY_ID, id_type="investigation",)


class TestImmuneSpaceToAKC(unittest.TestCase):

    def test_get_study_arms(self):
        study_arms = i2a.get_study_arms(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        assert len(study_arms) == 1
        assert sorted([arm.akc_id for arm in study_arms]) == [ID_HANDLER.get_akc_id(immunespace_id="ARM6832", id_type="arm", )]
        assert study_arms[0].investigation == INVESTIGATION_KEY

    def test_get_participants(self):
        participants = i2a.get_participants(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        assert len(participants) == 7

        study_arm_keys = [arm.akc_id for arm in i2a.get_study_arms(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)]

        assert all([participant.study_arm in study_arm_keys for participant in participants])

    def test_get_references(self):
        # todo the refs table is scrambled and needs fixing
        refs = i2a.get_references(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        assert len(refs) == 1
        assert len(refs[0].authors) == 15
        assert refs[0].investigations == [INVESTIGATION_KEY]
        assert refs[0].source_uri == 'PMID:36658238'
        assert refs[0].sources == ['PMID:36658238', 'doi:10.1038/s41590-022-01395-9']

    def test_get_study_events(self):
        study_events = i2a.get_study_events(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        assert len(study_events) == 1 # planned event table length
        study_arm_keys = [arm.akc_id for arm in i2a.get_study_arms(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)]

        for study_event in study_events:
            assert all([arm in study_arm_keys for arm in study_event.study_arms])

    def test_get_life_events(self):
        life_events = i2a.get_life_events(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        study_event_keys = [study_event.akc_id for study_event in i2a.get_study_events(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)]
        participant_keys = [participant.akc_id for participant in i2a.get_participants(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)]

        assert len(life_events) == 75 # event table length

        for life_event in life_events:
            # todo see long comment in 'get_life_events' -> if all life_events must have study_event = PV11666, then uncomment this line
            # assert life_event.study_event in study_event_keys or life_event.study_event is None
            assert life_event.participant in participant_keys

    def test_get_immune_exposures(self):
        immune_exposures = i2a.get_immune_exposures(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        assert len(immune_exposures) == 0  # this study has no immune exposures


    def test_get_assessments(self):
        result = i2a.get_assessments(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        assert type(result) == list
        assert len(result) == 0

    def test_get_specimens(self):
        specimens = i2a.get_specimens(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        assert len(specimens) == 68  # length of specimen table

        life_event_keys = [life_event.akc_id for life_event in i2a.get_life_events(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)]

        for specimen in specimens:
            assert specimen.life_event in life_event_keys


    def test_get_akc_container_investigation(self):
        akc_container = i2a.get_akc_container(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)

        assert type(akc_container) == AIRRKnowledgeCommons
        assert len(akc_container.investigations) == 1

        assert list(akc_container.investigations.keys()) == [INVESTIGATION_KEY]
        assert len(akc_container.investigations[INVESTIGATION_KEY].participants) == 7
        assert sorted(list(akc_container.participants.keys())) == sorted(akc_container.investigations[INVESTIGATION_KEY].participants)
        assert sorted(list(akc_container.participants.keys())) == sorted([participant.akc_id for participant in i2a.get_participants(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)])

        # todo test akc_container.investigations[INVESTIGATION_KEY].assays once implemented
        # todo test akc_container.investigations[INVESTIGATION_KEY].conclusions once there is an example

        assert akc_container.investigations[INVESTIGATION_KEY].documents == [ref.source_uri for ref in i2a.get_references(STUDY_DB_FILE, STUDY_ID, ID_HANDLER)]

        assert len(akc_container.study_arms) == 1
        assert all([arm.investigation == INVESTIGATION_KEY for arm in akc_container.study_arms.values()])

        assert len(akc_container.references) == 1
        assert akc_container.references['PMID:36658238'].investigations == [INVESTIGATION_KEY]


class TestImmuneSpaceToVDJServer(unittest.TestCase):

    def test_get_subject_metadata_tsv(self):
        pass # todo fill in test

    def test_get_sample_processing_metadata_tsv(self):
        pass # todo fill in test
