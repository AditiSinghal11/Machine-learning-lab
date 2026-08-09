# AI-generated unit tests using ChatGPT
# Same tests are applied to Lab 3 and Lab 4 implementations.

import unittest
import importlib


class TestQ9Both(unittest.TestCase):

    def run_tests_for(self, module_name):
        module = importlib.import_module(module_name)

        self.assertEqual(
            module.mean([2, 4, 6]),
            4
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
            module.mean([7, 7, 7]),
            7
        )

        self.assertEqual(
            module.standard_deviation([7, 7, 7]),
            0
        )

    def test_lab3(self):
        self.run_tests_for("q9")

    def test_lab4_ai(self):
        self.run_tests_for("q9_ai")


if __name__ == "__main__":
    unittest.main()
