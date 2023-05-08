# Zhaoyu Wang developed
# time: 2023-05-04 2:49 p.m.

# ?????????
def insert_sort(li):
    for i in range(1, len(li)):
        temp = li[li]
        j = i -1
        while j >= 0 and li[j] > temp:
            li[j+1] = li[j]
            j-=1
        li[j+1] = temp