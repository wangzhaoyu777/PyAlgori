# Zhaoyu Wang developed
# time: 2023-05-03 3:36 p.m.
import random


def bubble_sort(data_list):
    for i in range(len(data_list) - 1 ):
        exchange = False
        for j in range(len(data_list) - i - 1):
            if data_list[j] > data_list[j+1]:
                data_list[j] , data_list[j+1] = data_list[j+1],data_list[j]
                exchange = True
        print(data_list)
        if not exchange:
             return
a = [4,5,6,1,2,3,]
# a = [random.randint(0,99) for i in range(10)]
bubble_sort(a)
print(a)
