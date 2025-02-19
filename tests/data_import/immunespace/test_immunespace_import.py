import os
import unittest
from pathlib import Path


import src.scripts.immunespace.immunespace_to_akc as i2a

ROOT = Path(os.path.dirname(__file__)) / "../../../"
DATA_DIR = ROOT / "src/data/immunespace_example_data"
HCC_DB_FILE = DATA_DIR / "hcc_kb_nanobot.db"
IMMPORT_DB_FILE = DATA_DIR / "immport_nanobot.db"


# todo 'fill out' tests: test that values are correct

class TestImmuneSpaceToAKC(unittest.TestCase):

    def test_get_study_arms(self):
        print(i2a.get_study_arms(HCC_DB_FILE, "SDY460"))

    def test_get_participants(self):
        print(i2a.get_participants(HCC_DB_FILE, IMMPORT_DB_FILE,"SDY460"))

    def test_get_references(self):
        print(i2a.get_references(HCC_DB_FILE, "SDY460"))

    def test_get_investigation(self):
        print(i2a.get_investigation_partial(HCC_DB_FILE, IMMPORT_DB_FILE,"SDY460"))

    def test_get_study_events(self):
        print(i2a.get_study_events(HCC_DB_FILE, "SDY460"))

    def test_get_life_events(self):
        print(i2a.get_life_events(HCC_DB_FILE, "SDY460"))

    def test_get_immune_exposures(self):
        print(i2a.get_immune_exposures(HCC_DB_FILE, "SDY460"))

    def test_get_assessments(self):
        result = i2a.get_assessments(HCC_DB_FILE, "SDY460")

        assert type(result) == list
        assert len(result) == 0

    def test_get_specimens(self):
        print(i2a.get_specimens(HCC_DB_FILE, "SDY460"))

    def test_get_datasets(self):
        result = i2a.get_datasets(HCC_DB_FILE, "SDY460")

        assert type(result) == list
        assert len(result) == 0

    def test_get_conclusions(self):
        print(i2a.get_conclusions(HCC_DB_FILE, "SDY460"))

    def test_get_akc_container(self):
        print(i2a.get_akc_container(HCC_DB_FILE, IMMPORT_DB_FILE, "SDY460"))
