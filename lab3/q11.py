import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def euclidean_distance(a, b):

    total = 0

    for i in range(len(a)):
        total += (a[i] - b[i]) ** 2

    return total ** 0.5


def assign_clusters(data, centroids):

    clusters = []

    for point in data:

        distances = []

        for centroid in centroids:
            distances.append(euclidean_distance(point, centroid))

        clusters.append(distances.index(min(distances)))

    return clusters


def update_centroids(data, clusters, k):

    centroids = []

    for i in range(k):

        points = []

        for j in range(len(data)):

            if clusters[j] == i:
                points.append(data[j])

        if len(points) == 0:
            centroids.append(data[0])
        else:
            centroids.append(np.mean(points, axis=0))

    return centroids


def kmeans(data, k, iterations):

    centroids = data[:k]

    for i in range(iterations):

        clusters = assign_clusters(data, centroids)

        centroids = update_centroids(data, clusters, k)

    return clusters, centroids


numeric_df = df.select_dtypes(include=["int64", "float64"]).dropna()

data = numeric_df.values

clusters, centroids = kmeans(data, 3, 10)

print("Cluster of each data point")
print(clusters)

print()

print("Centroids")
print(np.array(centroids))