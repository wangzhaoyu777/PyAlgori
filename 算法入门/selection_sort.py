# Zhaoyu Wang developed
# time: 2023-05-03 8:17 p.m.
import random

def selection_sort(a):
    #从第i+1个数开始到最后一个进行查找，选最小的数然后和i换位置
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j]<a[min]:
                min = j
        a[i], a[min]= a[min],a[i]
# a = [random.randint(0,20) for i in range(9)]
a = [10, 18, 11, 19, 20, 8, 6, 16, 17]
print(a)
selection_sort(a)
print(a)