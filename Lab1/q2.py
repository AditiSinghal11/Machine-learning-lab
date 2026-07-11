r1 = int(input("Rows of Matrix A: "))
c1 = int(input("Columns of Matrix A: "))

A = []
print("Enter Matrix A:")
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

r2 = int(input("Rows of Matrix B: "))
c2 = int(input("Columns of Matrix B: "))

B = []
print("Enter Matrix B:")
for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

if c1 != r2:
    print("Matrices cannot be multiplied.")
else:
    result = []

    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    print("Product Matrix:")
    for row in result:
        print(row)