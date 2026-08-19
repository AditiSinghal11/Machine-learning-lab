import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

k_values = range(1, 11)

my_accuracy = []
sklearn_accuracy = []

for k in k_values:

    my_model = MyKNN(k=k, sort_type="bubble")
    my_model.fit(X_train, y_train)

    my_accuracy.append(my_model.score(X_test, y_test))

    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)

    sklearn_accuracy.append(model.score(X_test, y_test))

print("My kNN:", my_accuracy)
print("Sklearn:", sklearn_accuracy)

plt.plot(k_values, my_accuracy, marker="o", label="My kNN")
plt.plot(k_values, sklearn_accuracy, marker="o", label="Sklearn")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.legend()
plt.show()