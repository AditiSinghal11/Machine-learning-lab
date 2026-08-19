weighted_accuracy = []

for k in k_values:

    predictions = []

    for test in X_test:
        prediction = weighted_knn_predict(
            X_train,
            y_train,
            test,
            k,
            "bubble"
        )
        predictions.append(prediction)

    accuracy = np.mean(np.array(predictions) == y_test)
    weighted_accuracy.append(accuracy)

print("Normal kNN:", my_accuracy)
print("Weighted kNN:", weighted_accuracy)

plt.plot(k_values, my_accuracy, marker="o", label="Normal kNN")
plt.plot(k_values, weighted_accuracy, marker="o", label="Weighted kNN")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.legend()
plt.show()