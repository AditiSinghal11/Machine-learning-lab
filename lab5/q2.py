def weighted_knn_predict(X_train, y_train, test, k, sort_type="bubble"):
    distances = []

    for i in range(len(X_train)):
        d = euclidean_distance(X_train[i], test)
        distances.append((d, y_train[i]))

    sort_function = get_sort_function(sort_type)
    distances = sort_function(distances)

    neighbors = distances[:k]

    weights = {}

    for distance, label in neighbors:
        if distance == 0:
            weight = 1000000
        else:
            weight = 1 / distance

        if label not in weights:
            weights[label] = 0

        weights[label] += weight

    return max(weights, key=weights.get)