# Zhaoyu Wang developed
# time: 2023-05-03 2:57 p.m.
a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6, 7]

def binary_search(data_list, value):
    # 建立两个指针分别从数列的最左和右端开始查找
    left = 0                    # 数列第一个下标是0
    right = len(data_list) - 1  # 最后一个是lenth - 1
    while left <= right:        # 左指针和右指针没有重合时继续查找
        index = (left + right) // 2     # 取中间值和目标值比较，缩小搜索范围
        if data_list[index] == value:   # 如果index对应的值和target相等则返回 index
            return index
        elif data_list[index] > value:  # 如果index对应的值大于target，说明target在index的左边，
            right = index -1            # 所以要把右指针放在中间值左边一位；因为上一步判断过index对应的值不等于target
        else: # data_list[index] < value:   # 同理，如果index对应的值小于target，则应该把左指针放在index or mid的右边一个位置
            left = index +1
    else:
        return None
binary_search(b, 4)
