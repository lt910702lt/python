'''
问：1234能组成多少个不重重复的不相同的三位数！
'''
# 使用一个排列的工具包
# from itertools import permutations
#
# ret = permutations('1234', 3)
# print(list(ret))
# print(len(list(ret)))

list1 = [11, 22, 33]
list2 = ['aa', 'bb', 'cc']
from itertools import chain

for i in chain(list1, list2):
    print(i)
