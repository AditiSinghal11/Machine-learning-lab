import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

data = pd.read_excel(
    "C:/Users/91971/Downloads/Lab Session Data.xlsx",
    sheet_name="IRCTC Stock Price"
)

price = data["Price"]

mean1 = np.mean(price)
var1 = np.var(price)

print("Mean (NumPy):", mean1)
print("Variance (NumPy):", var1)


def my_mean(arr):
    s = 0
    for i in arr:
        s += i
    return s / len(arr)


def my_variance(arr):
    m = my_mean(arr)
    s = 0
    for i in arr:
        s += (i - m) ** 2
    return s / len(arr)


print("Mean (Own):", my_mean(price))
print("Variance (Own):", my_variance(price))


start = time.time()
for i in range(10):
    np.mean(price)
np_time = (time.time() - start) / 10

start = time.time()
for i in range(10):
    my_mean(price)
my_time = (time.time() - start) / 10

print("Average NumPy Time:", np_time)
print("Average Own Function Time:", my_time)


wed = data[data["Day"] == "Wed"]
print("Wednesday Mean:", np.mean(wed["Price"]))


apr = data[data["Month"] == "Apr"]
print("April Mean:", np.mean(apr["Price"]))


loss = data["Chg%"] < 0
print("Probability of Loss:", loss.mean())


profit_wed = wed["Chg%"] > 0
print("Probability of Profit on Wednesday:", profit_wed.mean())


print("Conditional Probability:", profit_wed.sum() / len(wed))


plt.scatter(data["Day"], data["Chg%"])
plt.xlabel("Day")
plt.ylabel("Chg%")
plt.title("Day vs Chg%")
plt.show()