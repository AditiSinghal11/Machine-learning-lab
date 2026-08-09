# AI-generated unit tests using ChatGPT
# Same tests are applied to Lab 3 and Lab 4 implementations.

import unittest
import importlib


class TestQ7Both(unittest.TestCase):

    def run_tests_for(self, module_name):
        module = importlib.import_module(module_name)

        self.assertEqual(
            module.dot_product([1, 2, 3], [4, 5, 6]),
            32
        )

        self.assertEqual(
            module.dot_product([1, 2, 3], [0, 0, 0]),
            0
        )

        self.assertEqual(
            module.euclidean_norm([3, 4]),
            5
        )

        self.assertEqual(
            module.euclidean_norm([0, 0]),
            0
        )

    def test_lab3(self):
        self.run_tests_for("q7")

    def test_lab4_ai(self):
        self.run_tests_for("q7_ai")


if __name__ == "__main__":
    unittest.main()
