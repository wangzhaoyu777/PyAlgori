# Zhaoyu Wang developed
# time: 2023-05-04 2:49 p.m.

# ?????????
def insert_sort(a):
    for i in range(1, len(a)):          # 遍历除了第一位以外的元素和第一位比大小，或者说是和i-1比大小；i指摸到的牌的下标
        temp = a[i]                     #
        j = i -1                        # j指手里牌的下标
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j-=1
        a[j+1] = temp
a = [6,8,7,4,5,2,1,3]
insert_sort(a)
print(a)