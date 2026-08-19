class MyKNN:

    def __init__(self, k=3, sort_type="bubble"):
        self.k = k
        self.sort_type = sort_type

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        result = []

        for test in X:
            label = knn_predict(
                self.X_train,
                self.y_train,
                test,
                self.k,
                self.sort_type
            )
            result.append(label)

        return np.array(result)

    def score(self, X, y):
        predictions = self.predict(X)
        return np.mean(predictions == y)


model = MyKNN(k=3, sort_type="bubble")

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = model.score(X_test, y_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy)