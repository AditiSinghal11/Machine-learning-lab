import pandas as pd
import numpy as np

# Load Excel sheet
def load_data():
    df = pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase data")
    return df

# Separate features and output
def get_matrices(df):
    X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]]
    y = df["Payment (Rs)"]
    return X, y

# Find dimension of vector space
def get_dimension(X):
    return X.shape[1]

# Find number of vectors
def get_vectors(X):
    return X.shape[0]

# Find rank of feature matrix
def get_rank(X):
    return np.linalg.matrix_rank(X)

# Find cost of each product using pseudo inverse
def get_product_cost(X, y):
    pseudo_inverse = np.linalg.pinv(X)
    cost = np.dot(pseudo_inverse, y)
    return cost

# Main function
def main():

    df = load_data()

    X, y = get_matrices(df)

    print("Feature Matrix:")
    print(X)

    print("\nOutput Vector:")
    print(y)

    print("\nDimension of Vector Space:", get_dimension(X))

    print("Number of Vectors:", get_vectors(X))

    print("Rank of Matrix:", get_rank(X))

    print("\nCost of each Product:")
    print(get_product_cost(X, y))

# Run the program
main()