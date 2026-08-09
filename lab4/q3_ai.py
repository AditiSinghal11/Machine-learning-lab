# AI-assisted code generated using ChatGPT
# Experiment: Compare dataset shapes after encoding

import pandas as pd

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def label_encode(column):
    # AI-assisted implementation
    categories = pd.unique(column)
    mapping = {value: index for index, value in enumerate(categories)}
    return column.map(mapping)


def one_hot_encode(column):
    # AI-assisted implementation
    return pd.get_dummies(column, dtype=int)


label_df = df.copy()
label_df["Education"] = label_encode(label_df["Education"])
label_df["Marital_Status"] = label_encode(label_df["Marital_Status"])

onehot_df = df.copy()

education = one_hot_encode(onehot_df["Education"])
marital = one_hot_encode(onehot_df["Marital_Status"])

onehot_df = onehot_df.drop(
    columns=["Education", "Marital_Status"]
)

onehot_df = pd.concat(
    [onehot_df, education, marital],
    axis=1
)

print("Original Dataset Shape :", df.shape)
print("Label Encoded Dataset Shape :", label_df.shape)
print("One Hot Encoded Dataset Shape :", onehot_df.shape)
