# filter函数，语法：filter(function,iterable)

# # 留下列表里面的奇数
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def func(s):  # 判断奇数
#     return s % 2 == 1
#
#
# fl = filter(func, lst)  # 返回的是一个迭代器
# print("__iter__" in dir(fl))
# print("__next__" in dir(fl))
#
# print(list(fl))     #通过list打印出迭代器的内容


# 找出年龄大于40的人
lst = [
    {'id': 1, 'name': 'alex', 'age': 18},
    {'id': 2, 'name': 'taibai', 'age': 58},
    {'id': 3, 'name': 'wusir', 'age': 38},
    {'id': 4, 'name': 'ritian', 'age': 48},
    {'id': 5, 'name': '女神', 'age': 18}
]

# 通过filter找出年纪大于40的人
print(list(filter(lambda dic: dic['age'] > 40, lst)))