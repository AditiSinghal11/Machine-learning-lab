# AI-generated unit tests using ChatGPT
# Same tests are applied to Lab 3 and Lab 4 implementations.

import unittest
import pandas as pd
import importlib


class TestQ2Both(unittest.TestCase):

    def run_tests_for(self, module_name):
        module = importlib.import_module(module_name)

        data = pd.Series(["A", "B", "A", "C"])
        self.assertEqual(module.label_encode(data), [0, 1, 0, 2])

        data2 = pd.Series(["A", "A", "B"])
        self.assertEqual(module.label_encode(data2), [0, 0, 1])

        data3 = pd.Series(["A", "B", "A"])
        result = module.one_hot_encode(data3)
        self.assertEqual(result.shape, (3, 2))
        self.assertTrue((result.sum(axis=1) == 1).all())

    def test_lab3(self):
        self.run_tests_for("q2")

    def test_lab4_ai(self):
        self.run_tests_for("q2_ai")


if __name__ == "__main__":
    unittest.main()
