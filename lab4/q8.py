import pandas as pd

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
    variances = []
    stds = []

    for column in data.columns:

        values = data[column].tolist()

        means.append(mean(values))
        variances.append(variance(values))
        stds.append(standard_deviation(values))

    return means, variances, stds


numeric_df = df.select_dtypes(include=["int64", "float64"])

means, variances, stds = dataset_statistics(numeric_df)

print("Mean")
print(means)

print()

print("Variance")
print(variances)

print()

print("Standard Deviation")
print(stds)