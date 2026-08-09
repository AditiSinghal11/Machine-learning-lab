import pandas as pd
import numpy as np
import time

import q11
import q11_ai


# Load the same dataset for both algorithms
df = pd.read_excel(
    "Lab Session Data_final.xlsx",
    sheet_name="marketing_campaign"
)

numeric_df = df.select_dtypes(
    include=["int64", "float64"]
).dropna()

data = numeric_df.to_numpy()

k = 3
iterations = 10
runs = 10


def measure_time(kmeans_function):

    times = []

    for _ in range(runs):

        start = time.perf_counter()

        clusters, centroids = kmeans_function(
            data,
            k,
            iterations
        )

        end = time.perf_counter()

        times.append(end - start)

    return np.mean(times), np.std(times)


# Test YOUR K-means
original_time, original_std = measure_time(
    q11.kmeans
)


# Test AI K-means
ai_time, ai_std = measure_time(
    q11_ai.kmeans
)


print("K-MEANS PERFORMANCE COMPARISON")
print("--------------------------------")

print("Dataset size :", len(data))
print("Number of features :", data.shape[1])
print("K :", k)
print("Iterations :", iterations)
print("Number of runs :", runs)

print("\nYOUR LAB 3 VERSION")
print("Average time :", original_time, "seconds")
print("Standard deviation :", original_std)

print("\nAI LAB 4 VERSION")
print("Average time :", ai_time, "seconds")
print("Standard deviation :", ai_std)

print("\nSpeedup :", original_time / ai_time)