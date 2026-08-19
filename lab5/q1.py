import numpy as np

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def bubble_sort(data):
    data = data.copy()
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][0] > data[j + 1][0]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def selection_sort(data):
    data = data.copy()
    n = len(data)

    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if data[j][0] < data[min_pos][0]:
                min_pos = j
        data[i], data[min_pos] = data[min_pos], data[i]

    return data

def insertion_sort(data):
    data = data.copy()

    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1

        while j >= 0 and data[j][0] > temp[0]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = temp

    return data

def get_sort_function(name):
    if name == "bubble":
        return bubble_sort
    elif name == "selection":
        return selection_sort
    else:
        return insertion_sort

def knn_predict(X_train, y_train, test, k, sort_type="bubble"):
    distances = []

    for i in range(len(X_train)):
        d = euclidean_distance(X_train[i], test)
        distances.append((d, y_train[i]))

    sort_function = get_sort_function(sort_type)
    distances = sort_function(distances)

    neighbors = distances[:k]

    count = {}

    for distance, label in neighbors:
        if label not in count:
            count[label] = 0
        count[label] += 1

    return max(count, key=count.get)