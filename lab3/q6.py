import pandas as pd
from scipy.spatial.distance import minkowski

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def minkowski_distance(vector1, vector2, p):

    distance = 0

    for i in range(len(vector1)):
        distance += abs(vector1[i] - vector2[i]) ** p

    return distance ** (1 / p)


numeric_df = df.select_dtypes(include=["int64", "float64"])

vector1 = numeric_df.iloc[0].tolist()
vector2 = numeric_df.iloc[1].tolist()

p = 2

my_distance = minkowski_distance(vector1, vector2, p)
package_distance = minkowski(vector1, vector2, p)

print("My Function :", my_distance)
print("Scipy Function :", package_distance)