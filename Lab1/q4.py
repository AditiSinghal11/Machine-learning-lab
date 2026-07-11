rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

print("Enter the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Transpose:")

for i in range(cols):
    for j in range(rows):
        print(matrix[j][i], end=" ")
    print()