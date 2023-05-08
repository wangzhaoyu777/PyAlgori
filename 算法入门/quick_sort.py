# Zhaoyu Wang developed
# time: 2023-05-08 9:14 a.m.

# 此方法也用到了递归
def partition (data_list, left, right):
    temp = data_list[left] # 空出第一个位置给，确定中间值temp
    while left < right :
        # 注意！！！左右指针交替进行；先右再左，因为第一步已经把最左边的值赋值给了temp，所以左边先空出一个位置
        while left < right and data_list[right] >= temp:    # 从右边 找比temp小的数值
            right -=1                                       # 往左走一步
        data_list[left] = data_list[right]                  # 把右边的值给到左边的空位上
        print(data_list, 'right')                           # 显示每次right指针对列表的改变
        while left < right and data_list[left] <=temp:      # 从左边找比temp打的数值
            left += 1                                       # 往右走一步
        data_list[right] = data_list[left]                  # 把左边的比temp大的值给到邮编的空位上
        print(data_list, ' left')                           # 显示每次left指针对列表的改变
    data_list[left] = temp                                  # 在两个指针重合时，把temp归位
    return left                                             # 返回中间值

def quick_sort (data_list, left, right):
    if left < right:                                        # 至少有两个元素
        mid = partition(data_list, left, right)
        quick_sort(data_list, left, mid -1)                 # 排序左边部分
        quick_sort(data_list, mid+1, right)                 # 排序右边的部分

a = [6,6,1,3,4,7,9,5,6]
print(a)
quick_sort(a, 0, len(a)-1)
print(a)