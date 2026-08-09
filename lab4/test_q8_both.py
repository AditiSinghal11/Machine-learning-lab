# AI-generated unit tests using ChatGPT
# Same tests are applied to Lab 3 and Lab 4 implementations.

import unittest
import importlib


class TestQ8Both(unittest.TestCase):

    def run_tests_for(self, module_name):
        module = importlib.import_module(module_name)

        self.assertEqual(
            module.mean([1, 2, 3, 4, 5]),
            3
        )

        self.assertEqual(
            module.variance([1, 2, 3, 4, 5]),
            2
        )

        self.assertAlmostEqual(
            module.standard_deviation([1, 2, 3, 4, 5]),
            2 ** 0.5
        )

        self.assertEqual(
            module.variance([5, 5, 5]),
            0
        )

        self.assertEqual(
            module.standard_deviation([5, 5, 5]),
            0
        )

    def test_lab3(self):
        self.run_tests_for("q8")

    def test_lab4_ai(self):
        self.run_tests_for("q8_ai")


if __name__ == "__main__":
    unittest.main()
