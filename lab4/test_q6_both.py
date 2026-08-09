# AI-generated unit tests using ChatGPT
# Same tests are applied to Lab 3 and Lab 4 implementations.

import unittest
import importlib
import numpy as np


class TestQ6Both(unittest.TestCase):

    def run_tests_for(self, module_name):
        module = importlib.import_module(module_name)

        self.assertEqual(
            module.minkowski_distance([1, 2], [4, 6], 1),
            7
        )

        self.assertEqual(
            module.minkowski_distance([0, 0], [3, 4], 2),
            5
        )

        result = module.minkowski_distance(
            [1, 2, 3], [4, 5, 6], 2
        )
        self.assertAlmostEqual(result, np.sqrt(27))

        self.assertEqual(
            module.minkowski_distance([4, 4], [4, 4], 2),
            0
        )

    def test_lab3(self):
        self.run_tests_for("q6")

    def test_lab4_ai(self):
        self.run_tests_for("q6_ai")


if __name__ == "__main__":
    unittest.main()
