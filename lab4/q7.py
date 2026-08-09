import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def dot_product(vector1, vector2):

    result = 0

    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]

    return result


def euclidean_norm(vector):

    total = 0

    for value in vector:
        total += value ** 2

    return total ** 0.5


numeric_df = df.select_dtypes(include=["int64", "float64"])

vector1 = numeric_df.iloc[0].tolist()
vector2 = numeric_df.iloc[1].tolist()

my_dot = dot_product(vector1, vector2)
numpy_dot = np.dot(vector1, vector2)

my_norm1 = euclidean_norm(vector1)
numpy_norm1 = np.linalg.norm(vector1)

my_norm2 = euclidean_norm(vector2)
numpy_norm2 = np.linalg.norm(vector2)

print("My Dot Product :", my_dot)
print("Numpy Dot Product :", numpy_dot)

print()

print("My Norm (Vector1) :", my_norm1)
print("Numpy Norm (Vector1) :", numpy_norm1)

print()

print("My Norm (Vector2) :", my_norm2)
print("Numpy Norm (Vector2) :", numpy_norm2)