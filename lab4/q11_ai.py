# AI-assisted code generated using ChatGPT
# Experiment: K-Means Clustering
# AI approach: NumPy vectorization and broadcasting

import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def euclidean_distance(a, b):
    # AI-assisted implementation using NumPy
    return np.linalg.norm(np.asarray(a) - np.asarray(b))


def assign_clusters(data, centroids):
    # AI-assisted implementation using NumPy broadcasting
    data = np.asarray(data)
    centroids = np.asarray(centroids)

    distances = np.linalg.norm(
        data[:, np.newaxis, :] - centroids[np.newaxis, :, :],
        axis=2
    )

    return np.argmin(distances, axis=1).tolist()


def update_centroids(data, clusters, k):
    # AI-assisted implementation using boolean indexing
    data = np.asarray(data)
    clusters = np.asarray(clusters)

    centroids = []

    for i in range(k):
        points = data[clusters == i]

        if len(points) == 0:
            centroids.append(data[0])
        else:
            centroids.append(np.mean(points, axis=0))

    return np.asarray(centroids)


def kmeans(data, k, iterations):
    # AI-assisted K-means implementation
    data = np.asarray(data)
    centroids = data[:k].copy()

    for _ in range(iterations):
        clusters = assign_clusters(data, centroids)

        new_centroids = update_centroids(
            data,
            clusters,
            k
        )

        if np.allclose(centroids, new_centroids):
            centroids = new_centroids
            break

        centroids = new_centroids

    return clusters, centroids


numeric_df = df.select_dtypes(
    include=["int64", "float64"]
).dropna()

data = numeric_df.to_numpy()

clusters, centroids = kmeans(data, 3, 10)

print("Cluster of each data point")
print(clusters)

print("\nCentroids")
print(centroids)
