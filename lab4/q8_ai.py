# AI-assisted code generated using ChatGPT
# Experiment: Mean, Variance and Standard Deviation

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
    variances = []
    stds = []

    for column in data.columns:
        values = data[column].dropna().to_numpy()

        means.append(mean(values))
        variances.append(variance(values))
        stds.append(standard_deviation(values))

    return means, variances, stds


numeric_df = df.select_dtypes(include=["int64", "float64"])

means, variances, stds = dataset_statistics(numeric_df)

print("Mean")
print(means)

print("\nVariance")
print(variances)

print("\nStandard Deviation")
print(stds)
