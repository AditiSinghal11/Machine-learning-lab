import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def minkowski_distance(vector1, vector2, p):

    distance = 0

    for i in range(len(vector1)):
        distance += abs(vector1[i] - vector2[i]) ** p

    return distance ** (1 / p)


numeric_df = df.select_dtypes(include=["int64", "float64"])

vector1 = numeric_df.iloc[0].tolist()
vector2 = numeric_df.iloc[1].tolist()

p_values = []
distances = []

for p in range(1, 11):

    d = minkowski_distance(vector1, vector2, p)

    p_values.append(p)
    distances.append(d)

print("p\tDistance")

for i in range(len(p_values)):
    print(p_values[i], "\t", distances[i])

plt.plot(p_values, distances, marker="o")
plt.xlabel("Value of p")
plt.ylabel("Minkowski Distance")
plt.title("Minkowski Distance for p = 1 to 10")
plt.grid(True)
plt.show()