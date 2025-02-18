import os
import unittest
from pathlib import Path


import src.scripts.immunespace.immunespace_to_akc as i2a

ROOT = Path(os.path.dirname(__file__)) / "../../../"
DATA_DIR = ROOT / "src/data/immunespace_example_data"
DB_FILE = DATA_DIR / "hcc_kb_nanobot.db"


# todo 'fill out' tests: test that values are correct

class TestImmuneSpaceToAKC(unittest.TestCase):

    def test_get_study_arms(self):
        print(i2a.get_study_arms(DB_FILE, "SDY460"))

    def test_get_participants(self):
        print(i2a.get_participants(DB_FILE, "SDY460"))

    def test_get_references(self):
        print(i2a.get_references(DB_FILE, "SDY460"))

    def test_get_investigation(self):
        print(i2a.get_investigation_partial(DB_FILE, "SDY460"))

    def test_get_study_events(self):
        print(i2a.get_study_events(DB_FILE, "SDY460"))

    def test_get_life_events(self):
        print(i2a.get_life_events(DB_FILE, "SDY460"))

    def test_get_akc_container(self):
        print(i2a.get_akc_container(DB_FILE, "SDY460"))
