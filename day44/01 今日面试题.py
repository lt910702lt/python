# # 第一题
# def extend_list(v, li=[]):
#     li.append(v)
#     return li
#
#
# list1 = extend_list(10)
# list2 = extend_list(123, [])
# list3 = extend_list('a')
#
# print(list1)
# print(list2)
# print(list3)
#
# # 第二题：下面代码的输出结果
# list1 = ['a', 'b', 'c', 'd', 'e']
# print(list1[10:])
#
# # 第三题：如何打乱一个有序列表
# list1 = ['a', 'b', 'c', 'd', 'e']
# # list2 = list1[::-1]
# list2 = reversed(list1)
# print(list2)

list1 = [11, 22, 33, 44]
ret = "+".join([str(x) for x in list1])
print(ret)
