# AI-generated unit tests using ChatGPT
# Same tests are applied to Lab 3 and Lab 4 implementations.

import unittest
import importlib


class TestQ10Both(unittest.TestCase):

    def run_tests_for(self, module_name):
        module = importlib.import_module(module_name)

        self.assertEqual(
            module.mean([10, 20, 30]),
            20
        )

        self.assertAlmostEqual(
            module.variance([10, 20, 30]),
            200 / 3
        )

        self.assertEqual(
            module.mean([5, 5, 5]),
            5
        )

        self.assertEqual(
            module.variance([5, 5, 5]),
            0
        )

    def test_lab3(self):
        self.run_tests_for("q10")

    def test_lab4_ai(self):
        self.run_tests_for("q10_ai")


if __name__ == "__main__":
    unittest.main()
