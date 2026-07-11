def transpose(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[j][i], end=" ")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose(matrix)