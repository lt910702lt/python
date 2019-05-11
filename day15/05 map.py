# 语法：map(function.iterable)
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 23, 23, 4, 52, 35, 234, 234, 234, 234, 234, 23, 4]
# it = map(lambda i: i * i, lst)
# print(list(it))


lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8]
print(list(map(lambda x, y: x + y, lst1, lst2)))
