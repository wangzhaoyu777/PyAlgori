# Zhaoyu Wang developed
# time: 2023-05-03 1:13 p.m.
# def linear_search(li, value):
#     for index, v in enumerate(li):
#         if v == value:
#             return print(index)
#     else:
#         return print('None')
def linear_search(data_list, value):
    for i in range(len(data_list)-1):
        if value == data_list[i]:
            return print(i)
linear_search([1,2,3,4,5,6], 2)
