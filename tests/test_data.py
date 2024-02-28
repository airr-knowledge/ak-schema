"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from ak_schema.datamodel.ak_schema import Container

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "examples", "iedb")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            obj = yaml_loader.load(path, target_class=Container)
            assert obj
