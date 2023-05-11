# Zhaoyu Wang developed
# time: 2023-05-04 2:49 p.m.

# ?????????
def insert_sort(li):
    for i in range(1, len(li)):         # 遍历除了第一位以外的元素和第一位比大小，或者说是和i-1比大小；i指摸到的牌的下标
        temp = li[i]                    # 
        j = i -1                        # j指手里牌的下标
        while j >= 0 and li[j] > temp:
            li[j+1] = li[j]
            j-=1
        li[j+1] = temp
