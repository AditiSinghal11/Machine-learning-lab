def minkowski_distance(A, B, p):
    total = 0

    for i in range(len(A)):
        total += abs(A[i] - B[i]) ** p

    distance = total ** (1 / p)

    return distance