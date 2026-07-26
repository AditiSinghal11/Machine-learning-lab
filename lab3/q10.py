import pandas as pd
import matplotlib.pyplot as plt

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


feature = df["Income"].dropna()

print("Mean :", mean(feature.tolist()))
print("Variance :", variance(feature.tolist()))

plt.hist(feature, bins=10)
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.title("Histogram of Income")
plt.grid(True)
plt.show()