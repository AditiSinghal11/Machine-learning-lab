import pandas as pd

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def minkowski_distance(vector1, vector2, p):

    distance = 0

    for i in range(len(vector1)):
        distance = distance + abs(vector1[i] - vector2[i]) ** p

    distance = distance ** (1 / p)

    return distance


numeric_df = df.select_dtypes(include=["int64", "float64"])

vector1 = numeric_df.iloc[0].tolist()
vector2 = numeric_df.iloc[1].tolist()

manhattan = minkowski_distance(vector1, vector2, 1)
euclidean = minkowski_distance(vector1, vector2, 2)

print("Manhattan Distance :", manhattan)
print("Euclidean Distance :", euclidean)