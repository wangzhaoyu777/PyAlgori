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
#
# i = 1
# total = 0
# while i <=100:
#     total = total+i
#     i+=1
# print(total)
# given a list , return max number in the list, python
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
# def removeDuplicates(nums):
#     fast = 0
#     slow = 0
#     size = len(nums)
#     while fast < size:
#         if nums[fast] != nums[fast - 1]:
#             nums[slow + 1] = nums[fast]
#             slow += 1
#         fast += 1
#     return slow + 1
# a = [1,1,2,2,3,3,3,4,4]
# x=removeDuplicates(a)
# print(x)
i = 32156
x = len(i)
print(x)
