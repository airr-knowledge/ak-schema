import os
import unittest
from pathlib import Path

from src.ak_schema.datamodel.ak_schema import *
import src.scripts.immunespace.immunespace_to_akc as i2a

ROOT = Path(os.path.dirname(__file__)) / "../../../"
DATA_DIR = ROOT / "src/data/immunespace_example_data"
HCC_DB_FILE = DATA_DIR / "hcc_kb_nanobot.db"
IMMPORT_DB_FILE = DATA_DIR / "immport_nanobot.db"


STUDY_ID = "SDY460"
INVESTIGATION_KEY = f"ImmuneSpace:investigation-{STUDY_ID}"


class TestImmuneSpaceToAKC(unittest.TestCase):

    def test_get_study_arms(self):
        study_arms = i2a.get_study_arms(HCC_DB_FILE, STUDY_ID)

        assert len(study_arms) == 3
        assert sorted([arm.akc_id for arm in study_arms]) == sorted(["ImmuneSpace:arm-ARM2480", "ImmuneSpace:arm-ARM2479", "ImmuneSpace:arm-ARM2478"])
        assert study_arms[0].investigation == INVESTIGATION_KEY

    def test_get_participants(self):
        participants = i2a.get_participants(HCC_DB_FILE, IMMPORT_DB_FILE, STUDY_ID)

        assert len(participants) == 27

        study_arm_keys = [arm.akc_id for arm in i2a.get_study_arms(HCC_DB_FILE, STUDY_ID)]

        assert all([participant.study_arm in study_arm_keys for participant in participants])

    def test_get_references(self):
        refs = i2a.get_references(HCC_DB_FILE, STUDY_ID)

        assert len(refs) == 1
        assert len(refs[0].authors) == 16
        assert refs[0].investigations == [INVESTIGATION_KEY]
        assert refs[0].source_uri == 'PMID:24337376'
        assert refs[0].sources == ['PMID:24337376', 'doi:10.4049/jimmunol.1301384']

    def test_get_study_events(self):
        study_events = i2a.get_study_events(HCC_DB_FILE, STUDY_ID)

        assert len(study_events) == 6 # planned event table length
        study_arm_keys = [arm.akc_id for arm in i2a.get_study_arms(HCC_DB_FILE, STUDY_ID)]

        for study_event in study_events:
            assert all([arm in study_arm_keys for arm in study_event.study_arms])

    def test_get_life_events(self):
        life_events = i2a.get_life_events(HCC_DB_FILE, STUDY_ID)

        study_event_keys = [study_event.akc_id for study_event in i2a.get_study_events(HCC_DB_FILE, STUDY_ID)]
        participant_keys = [participant.akc_id for participant in i2a.get_participants(HCC_DB_FILE, IMMPORT_DB_FILE, STUDY_ID)]

        assert len(life_events) == 81 # event table length

        for life_event in life_events:
            assert life_event.study_event in study_event_keys or life_event.study_event is None
            assert life_event.participant in participant_keys

    def test_get_immune_exposures(self):
        immune_exposures = i2a.get_immune_exposures(HCC_DB_FILE, STUDY_ID)

        assert len(immune_exposures) == 27  # immune_exposures table length

        life_event_keys = [life_event.akc_id for life_event in i2a.get_life_events(HCC_DB_FILE, STUDY_ID)]

        for immune_exposure in immune_exposures:
            assert immune_exposure.life_event in life_event_keys

    def test_get_assessments(self):
        result = i2a.get_assessments(HCC_DB_FILE, STUDY_ID)

        assert type(result) == list
        assert len(result) == 0

    def test_get_specimens(self):
        specimens = i2a.get_specimens(HCC_DB_FILE, STUDY_ID)

        assert len(specimens) == 54  # length of specimen table

        life_event_keys = [life_event.akc_id for life_event in i2a.get_life_events(HCC_DB_FILE, STUDY_ID)]

        for specimen in specimens:
            assert specimen.life_event in life_event_keys

    def test_get_datasets(self):
        result = i2a.get_datasets(HCC_DB_FILE, STUDY_ID)

        assert type(result) == list
        assert len(result) == 0

    def test_get_conclusions(self):
        conclusions = i2a.get_conclusions(HCC_DB_FILE, STUDY_ID)

        assert type(conclusions) == list
        assert len(conclusions) == 0  # length of signature table

    def test_get_akc_container_investigation(self):
        akc_container = i2a.get_akc_container(HCC_DB_FILE, IMMPORT_DB_FILE, STUDY_ID)

        assert type(akc_container) == AIRRKnowledgeCommons
        assert len(akc_container.investigations) == 1

        assert list(akc_container.investigations.keys()) == [INVESTIGATION_KEY]
        assert len(akc_container.investigations[INVESTIGATION_KEY].participants) == 27
        assert sorted(list(akc_container.participants.keys())) == sorted(akc_container.investigations[INVESTIGATION_KEY].participants)
        assert sorted(list(akc_container.participants.keys())) == sorted([participant.akc_id for participant in i2a.get_participants(HCC_DB_FILE, IMMPORT_DB_FILE, STUDY_ID)])

        # todo test akc_container.investigations[INVESTIGATION_KEY].assays once implemented
        # todo test akc_container.investigations[INVESTIGATION_KEY].conclusions once there is an example

        assert akc_container.investigations[INVESTIGATION_KEY].documents == [ref.source_uri for ref in i2a.get_references(HCC_DB_FILE, STUDY_ID)]

        assert len(akc_container.study_arms) == 3
        assert all([arm.investigation == INVESTIGATION_KEY for arm in akc_container.study_arms.values()])

        assert len(akc_container.references) == 1
        assert akc_container.references['PMID:24337376'].investigations == [INVESTIGATION_KEY]



