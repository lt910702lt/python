# lst = [5, 7, 6, 12, 1, 13, 9, 18, 5]
# lst.sort()  #sort是list里面的一个方法
# print(lst)

# ll = sorted(lst, reverse=True)  # 内置函数，返回一个新列表。新列表是排了序的。
# print(ll)

# # 给列表排序，要求根据字符串的长度进行排序
# lst = ['abbb', 'aab', 'aaabb', 'abbbb', 'aabbbbb', 'aaabbb']
#
# # def func(s):
# #     return s.count('b') #返回数字
# #
# #
# # ll = sorted(lst, key=func)  #内部，把可迭代对象中的每一个元素传递给func
# ll = sorted(lst, key=lambda s: s.count('b'))
# print(ll)


# 将下列列表的人民按照年龄排序
lst = [
    {'id': 1, 'name': 'alex', 'age': 18},
    {'id': 2, 'name': 'taibai', 'age': 58},
    {'id': 3, 'name': 'wusir', 'age': 38},
    {'id': 4, 'name': 'ritian', 'age': 48},
    {'id': 5, 'name': '女神', 'age': 18}
]

# def func(dic):
#     return dic['age']
#
#
# ll = sorted(lst, key=func)
ll = sorted(lst, key=lambda s: s['age'])
print(ll)


