# Zhaoyu Wang developed
# time: 2023-05-03 3:36 p.m.
import random
# 原地一个个的移动元素，从小到大或者从大到小
# def bubble_sort(data_list):
#     n = len(data_list)
#     for i in range(n - 1 ):                     # 第i的数是暂时最大的或者是最上方的
#         exchange = False                        # exchange作为一个tag来标记是否有数值发生交换，一旦没有交换就停止遍历节省时间
#         for j in range(n - i - 1):              # 从最下方的第一个数开始依次向上比较
#             if data_list[j] > data_list[j+1]:   # 如果j的值大于j+1则与之交换
#                 data_list[j] , data_list[j+1] = data_list[j+1],data_list[j]
#                 exchange = True                 # 把exchange变为true是因为发生了交换
#         print(data_list)
#         if not exchange:                        # 不发生交换之后就停止
#              return
a = [10, 18, 11, 19, 20, 8, 6, 16, 17]
# a = [random.randint(0,99) for i in range(10)]
def bubble_sort(a:list):
    n = len(a)
    for i in range(n-1):
        exchange = False
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]= a[j+1],a[j]
                exchange = True
        print(a)
        if not exchange:
            return
bubble_sort(a)
print(a)