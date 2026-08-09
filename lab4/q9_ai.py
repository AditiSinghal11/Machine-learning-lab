# AI-assisted code generated using ChatGPT
# Experiment: Compare custom mean and standard deviation with NumPy

import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def mean(values):
    # AI-assisted implementation using NumPy
    return np.mean(values)


def variance(values):
    # AI-assisted implementation using NumPy
    return np.var(values)


def standard_deviation(values):
    # AI-assisted implementation using NumPy
    return np.std(values)


def dataset_statistics(data):
    means = []
    stds = []

    for column in data.columns:
        values = data[column].dropna().to_numpy()

        means.append(mean(values))
        stds.append(standard_deviation(values))

    return means, stds


numeric_df = df.select_dtypes(include=["int64", "float64"])

my_mean, my_std = dataset_statistics(numeric_df)

numpy_mean = np.mean(numeric_df, axis=0)
numpy_std = np.std(numeric_df, axis=0)

print("My Mean")
print(my_mean)

print("\nNumpy Mean")
print(numpy_mean)

print("\nMy Standard Deviation")
print(my_std)

print("\nNumpy Standard Deviation")
print(numpy_std)

print("\nMeans Match :", np.allclose(my_mean, numpy_mean, equal_nan=True))
print("Standard Deviations Match :",
      np.allclose(my_std, numpy_std, equal_nan=True))
