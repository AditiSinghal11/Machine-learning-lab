list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

count = 0

for item in list1:
    if item in list2:
        count += 1

print("Number of common elements =", count)