# AI-assisted code generated using ChatGPT
# Experiment: Label Encoding and One-Hot Encoding

import pandas as pd

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def label_encode(column):
    # AI-assisted implementation
    categories = pd.unique(column)
    mapping = {value: index for index, value in enumerate(categories)}
    return column.map(mapping).tolist()


def one_hot_encode(column):
    # AI-assisted implementation
    return pd.get_dummies(column, dtype=int)


education_label = label_encode(df["Education"])
marital_label = label_encode(df["Marital_Status"])

education_onehot = one_hot_encode(df["Education"])
marital_onehot = one_hot_encode(df["Marital_Status"])

print("Education Label Encoding")
print(education_label[:10])

print("\nMarital Status Label Encoding")
print(marital_label[:10])

print("\nEducation One Hot Encoding")
print(education_onehot.head())

print("\nMarital Status One Hot Encoding")
print(marital_onehot.head())
