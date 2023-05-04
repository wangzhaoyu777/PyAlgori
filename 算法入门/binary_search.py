# Zhaoyu Wang developed
# time: 2023-05-03 2:57 p.m.
a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6, 7]

def binary_search(data_list, value):
    left = 0
    right = len(data_list) - 1
    while left <= right:
        index = (left + right) // 2
        if data_list[index] == value:
            return index
        elif data_list[index] > value:
            right = index -1
        else: # data_list[index] < value:
            left = index +1
    else:
        return None
binary_search(b, 4)