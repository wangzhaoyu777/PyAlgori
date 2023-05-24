# Zhaoyu Wang developed
# time: 2023-05-16 3:28 p.m.
# Given 2 strings, needle and haystack, write a function that given
# the first index of string needle in haystack, and returns -1 if needle does not exist in haystack. use python

# needle = 'aa'
# haystack = 'sdfaasdg'
# def find_needle(needle, haystack):
#     n = len(needle)
#     h = len(haystack)
#     for i in range(h - n +1):
#         if haystack[i:i+n] == needle:
#             return i
#     return -1
# a= find_needle(needle, haystack)
# print(a)

# given a list , return max number in the list, python

# def max_num (data:list[int]):
#     temp = data[0]
#     for i in data:
#         if i > temp:
#             temp = i
#     return temp
# l = [1,8,45,6,3,2,9,7]
# a = max_num(l)
# print(a)

# t = [1,5,3,9,7,32,5687,35,15]
# def find_max(data_list:list):
#     max_num = 0
#     for i in range(len(data_list)):
#         if data_list[i] >max_num:
#             max_num =data_list[i]
#     return max_num
# c = find_max(t)
# print(c)
# given a string, return the count of each character in that string, python

# def count_character(data:str):
#     collect = {}
#     for i in data:
#         if i in collect:
#             collect[i] = collect[i]+1
#         else:
#             collect[i] = 1
#     return collect
# char = 'asfdgrkjngasdffgarzxcvas'
# x = count_character(char)
# print(x)


roman = {1:'i',2:'ii'}
d,r=roman
print(d,r)