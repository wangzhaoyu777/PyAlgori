# Zhaoyu Wang developed
# time: 2023-05-08 4:15 p.m.
# 没看懂要反复看

def sift(data_list, low, high):
    '''

    :param data_list: 列表
    :param low: 堆的根节点位置
    :param high: 堆 的最后一个元素的位置
    :return:
    '''
    i = low                             # i最开始指向根节点
    j = 2 * i +1                        # j还是是左孩子
    temp = data_list[i]                 # 把堆顶存起来
    while j <= high:                    # 只要j位置有数
        if j +1 <= high and data_list[j+1] >data_list[j]:   # 如果右孩子有且比较大
            j = j+1                     # j指向右孩子
        if data_list[j] > temp:
            data_list[i] = data_list[j]
            i = j                       # 往下看一层
            j = 2 * i +1
        else:                           # 如果temp更大，把temp放到i的位置上
            data_list[i] = temp         # 把temp放到某一级领导位置上
            break
    else:
        data_list[i] = temp             # 把temp放到叶子节点上

def heap_sort(data_list):
    n = len(data_list)
    for i in range((n-2)//2, -1, -1):   # i表示建堆的时候调整的部分的根的下标
        sift(data_list, i, n-1)         # 建堆完成
    for i in range(n-1, -1, -1):        # i纸箱当前堆的最后一个元素
        data_list[0], data_list[i] = data_list[i], data_list[0]
        sift(data_list, 0, i - 1)       # i-1是新的high

