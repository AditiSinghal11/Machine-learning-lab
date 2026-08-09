import pandas as pd

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def label_encode(column):

    unique_values = []

    for value in column:
        if value not in unique_values:
            unique_values.append(value)

    mapping = {}

    for i in range(len(unique_values)):
        mapping[unique_values[i]] = i

    encoded = []

    for value in column:
        encoded.append(mapping[value])

    return encoded


def one_hot_encode(column):

    unique_values = []

    for value in column:
        if value not in unique_values:
            unique_values.append(value)

    encoded = pd.DataFrame()

    for value in unique_values:

        temp = []

        for item in column:

            if item == value:
                temp.append(1)
            else:
                temp.append(0)

        encoded[str(value)] = temp

    return encoded


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