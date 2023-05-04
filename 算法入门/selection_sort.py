# Zhaoyu Wang developed
# time: 2023-05-03 8:17 p.m.
import random


def selection_sort(data_list):
    for i in range(len(data_list)-1):
        min_index = i
        for j in range(i+1, len(data_list)):
            if data_list[j] < data_list[min_index]:
                min_index = j
        data_list[i],data_list[min_index] = data_list[min_index], data_list[i]
a = [random.randint(0,20) for i in range(9)]
print(a)
selection_sort(a)
print(a)