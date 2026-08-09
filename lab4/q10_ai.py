# AI-assisted code generated using ChatGPT
# Experiment: Income Mean, Variance and Histogram

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def mean(values):
    # AI-assisted implementation using Pandas
    return pd.Series(values).mean()


def variance(values):
    # AI-assisted implementation using Pandas
    return pd.Series(values).var(ddof=0)


feature = df["Income"].dropna()

print("Mean :", mean(feature))
print("Variance :", variance(feature))

plt.figure(figsize=(8, 5))
plt.hist(feature, bins=10, edgecolor="black")

plt.xlabel("Income")
plt.ylabel("Frequency")
plt.title("Histogram of Income")

plt.tight_layout()
plt.show()
