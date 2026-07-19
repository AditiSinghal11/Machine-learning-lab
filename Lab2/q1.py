import pandas as pd
import numpy as np

def load_data():
    df = pd.read_excel(
        "C:/Users/91971/Downloads/Lab Session Data.xlsx",
        sheet_name="Purchase data"
    )
    return df

def main():
    df = load_data()

    X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]]
    y = df["Payment (Rs)"]

    print("Feature Matrix (X):")
    print(X)

    print("\nOutput Vector (y):")
    print(y)

    print("\nDimension of Vector Space:", X.shape[1])
    print("Number of Vectors:", X.shape[0])

    rank = np.linalg.matrix_rank(X)
    print("Rank of Feature Matrix:", rank)

    cost = np.linalg.pinv(X) @ y

    print("\nCost of each product:")
    print("Candies      :", round(cost[0], 2))
    print("Mangoes      :", round(cost[1], 2))
    print("Milk Packets :", round(cost[2], 2))

if __name__ == "__main__":
    main()