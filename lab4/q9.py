import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def mean(values):

    total = 0

    for value in values:
        total += value

    return total / len(values)


def variance(values):

    avg = mean(values)

    total = 0

    for value in values:
        total += (value - avg) ** 2

    return total / len(values)


def standard_deviation(values):

    return variance(values) ** 0.5


def dataset_statistics(data):

    means = []
    stds = []

    for column in data.columns:

        values = data[column].tolist()

        means.append(mean(values))
        stds.append(standard_deviation(values))

    return means, stds


numeric_df = df.select_dtypes(include=["int64", "float64"])

my_mean, my_std = dataset_statistics(numeric_df)

numpy_mean = np.mean(numeric_df, axis=0)
numpy_std = np.std(numeric_df, axis=0)

print("My Mean")
print(my_mean)

print()

print("Numpy Mean")
print(numpy_mean)

print()

print("My Standard Deviation")
print(my_std)

print()

print("Numpy Standard Deviation")
print(numpy_std)