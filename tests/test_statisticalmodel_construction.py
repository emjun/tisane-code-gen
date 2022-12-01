"""
Tests that the statistical model is constructed accurately from an input JSON file
"""
from tisanecodegenerator.statisticalModel import StatisticalModel


# import pandas as pd
import os
import unittest
import logging

log = logging.getLogger("")
log.setLevel(logging.ERROR)

### Import helper functions
from helpers import *

test_data_repo_name = os.path.join(os.path.dirname(__file__), "input_json/")

class ConstructStatisticalModelTest(unittest.TestCase):
    def test_construct_main_only(self): 
        filename = "main_only.json"
        filepath = os.path.join(test_data_repo_name, filename)

        sm = construct_statistical_model(filepath)

        self.assertIsNotNone(sm)
        self.assertEqual(sm.dependent_variable, "PINCP")
        self.assertIsInstance(sm.main_effects, set)
        self.assertIn("AGEP", sm.main_effects)
        self.assertIn("SCHL", sm.main_effects)
        self.assertIsInstance(sm.interaction_effects, set)
        self.assertEqual(len(sm.interaction_effects), 0)
        self.assertIsInstance(sm.random_effects, set)
        self.assertEqual(len(sm.random_effects), 0)
        self.assertEqual(sm.family_function, "Gaussian")
        self.assertEqual(sm.link_function, "identity")