# AI-generated unit tests using ChatGPT
# Same tests are applied to Lab 3 and Lab 4 implementations.

import unittest
import importlib
import numpy as np


class TestQ11Both(unittest.TestCase):

    def run_tests_for(self, module_name):
        module = importlib.import_module(module_name)

        # Test Euclidean distance
        self.assertEqual(
            module.euclidean_distance([0, 0], [3, 4]),
            5
        )

        # Test cluster assignment
        data = np.array([
            [1, 1],
            [9, 9]
        ])

        centroids = np.array([
            [0, 0],
            [10, 10]
        ])

        self.assertEqual(
            module.assign_clusters(data, centroids),
            [0, 1]
        )

        # Test centroid update
        data2 = np.array([
            [1, 1],
            [3, 3],
            [9, 9],
            [11, 11]
        ])

        clusters = [0, 0, 1, 1]

        result = module.update_centroids(
            data2,
            clusters,
            2
        )

        expected = np.array([
            [2, 2],
            [10, 10]
        ])

        np.testing.assert_array_equal(
            result,
            expected
        )

        # Test K-means output structure
        data3 = np.array([
            [1, 1],
            [2, 2],
            [9, 9],
            [10, 10]
        ])

        clusters_result, centroids_result = module.kmeans(
            data3,
            2,
            10
        )

        self.assertEqual(len(clusters_result), 4)
        self.assertEqual(len(centroids_result), 2)

    def test_lab3(self):
        self.run_tests_for("q11")

    def test_lab4_ai(self):
        self.run_tests_for("q11_ai")


if __name__ == "__main__":
    unittest.main()
