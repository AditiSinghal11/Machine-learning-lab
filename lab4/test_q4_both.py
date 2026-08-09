# AI-generated unit tests using ChatGPT
# Same tests are applied to Lab 3 and Lab 4 implementations.

import unittest
import importlib


class TestQ4Both(unittest.TestCase):

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

        self.assertEqual(
            module.minkowski_distance([5, 5], [5, 5], 2),
            0
        )

        self.assertEqual(
            module.minkowski_distance([2], [7], 1),
            5
        )

    def test_lab3(self):
        self.run_tests_for("q4")

    def test_lab4_ai(self):
        self.run_tests_for("q4_ai")


if __name__ == "__main__":
    unittest.main()
