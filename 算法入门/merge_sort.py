# Zhaoyu Wang developed
# time: 2023-05-10 9:46 a.m.
import random
def merge(data_list, low, mid, high):
    i = low
    j = mid + 1
    temp_list =[]
    while i <= mid and j <=high:                # 左右两边都有数
        if data_list[i] < data_list[j]:
            temp_list.append(data_list[i])
            i +=1
        else:
            temp_list.append(data_list[j])
            j +=1
    # 执行完第一个while之后，肯定有一边的值没有了
    while i <= mid:
        temp_list.append(data_list[i])
        i +=1
    while j <= high:
        temp_list.append(data_list[j])
        j +=1
    data_list[low:high+1]= temp_list

def merge_sort(lst,low,high):
    if low < high:                          # 至少有两个元素
        mid = (low + high)//2
        merge_sort(lst, low, mid)
        merge_sort(lst, mid+1, high)
        merge(lst,low, mid, high)
data_list = list(range(100))
random.shuffle(data_list)
print(data_list)
merge_sort(data_list,0,len(data_list)-1)
print(data_list)