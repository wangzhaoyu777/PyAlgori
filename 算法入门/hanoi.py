# Zhaoyu Wang developed
# time: 2023-05-03 11:16 a.m.
# 递归（recursion）实例：汉诺塔问题
# 不是很明白？？？

def hanoi(n, a, b, c):                          # 把n个盘子从a 经过b 送到c上

    if n >0:                                    # n = 0 时终止程序
        hanoi(n-1, a, c, b)                     # 1. 把 n-1 个盘子从 a 经过c 移动到b
        print('moving from %s to %s' % (a,c))   # 2. 把最大的盘子从a 移动到c
        hanoi(n-1, b, a, c)                     # 3. 因为在第一步时， n-1 个盘子已经在b上，把n-1个盘子从b 经过a 移动到c

hanoi(3, 'A', 'B', 'C')
