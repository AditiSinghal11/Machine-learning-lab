import pandas as pd

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def label_encode(column):

    unique = []

    for value in column:
        if value not in unique:
            unique.append(value)

    mapping = {}

    for i in range(len(unique)):
        mapping[unique[i]] = i

    encoded = []

    for value in column:
        encoded.append(mapping[value])

    return encoded


def one_hot_encode(column):

    unique = []

    for value in column:
        if value not in unique:
            unique.append(value)

    encoded = pd.DataFrame()

    for value in unique:

        temp = []

        for item in column:

            if item == value:
                temp.append(1)
            else:
                temp.append(0)

        encoded[str(value)] = temp

    return encoded


label_df = df.copy()

label_df["Education"] = label_encode(label_df["Education"])
label_df["Marital_Status"] = label_encode(label_df["Marital_Status"])


onehot_df = df.copy()

education = one_hot_encode(onehot_df["Education"])
marital = one_hot_encode(onehot_df["Marital_Status"])

onehot_df = onehot_df.drop(["Education", "Marital_Status"], axis=1)

onehot_df = pd.concat([onehot_df, education, marital], axis=1)


print("Original Dataset Shape :", df.shape)
print("Label Encoded Dataset Shape :", label_df.shape)
print("One Hot Encoded Dataset Shape :", onehot_df.shape)