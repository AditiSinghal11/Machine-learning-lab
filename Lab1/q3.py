def common_elements(list1, list2):
    count = 0

    for i in list1:
        if i in list2:
            count += 1

    print("Common elements =", count)


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common_elements(list1, list2)