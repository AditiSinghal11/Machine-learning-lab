import pandas as pd

data = pd.read_excel(
    "C:/Users/91971/Downloads/Lab Session Data.xlsx",
    sheet_name="thyroid0387_UCI"
)

# Keep only columns that contain t/f values
binary = data.replace({"t": 1, "f": 0})

binary = binary.select_dtypes(include=["object"])

for col in binary.columns:
    binary[col] = binary[col].replace({1: 1, 0: 0, "1": 1, "0": 0})
    binary[col] = binary[col].map({"t": 1, "f": 0}).fillna(binary[col])

# Convert everything possible to numbers
binary = binary.apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)

v1 = binary.iloc[0]
v2 = binary.iloc[1]

f11 = f10 = f01 = f00 = 0

for i in range(len(v1)):
    if v1[i] == 1 and v2[i] == 1:
        f11 += 1
    elif v1[i] == 1 and v2[i] == 0:
        f10 += 1
    elif v1[i] == 0 and v2[i] == 1:
        f01 += 1
    else:
        f00 += 1

if (f11 + f10 + f01) == 0:
    jc = 0
else:
    jc = f11 / (f11 + f10 + f01)

smc = (f11 + f00) / (f11 + f10 + f01 + f00)

print("Jaccard Coefficient =", jc)
print("Simple Matching Coefficient =", smc)