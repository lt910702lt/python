# 1. 写函数，接收n个数字，求这些参数数字的和

# def func(*args):
#     # sum = 0
#     # for n in args:
#     #     sum = sum + n
#     # return sum
#     return sum(args)
#
# print(func(2, 3, 4, 5))

# 2. 写函数，传入函数中多个实参（均为可迭代对象，入字符串、列表、元组、集合等），将每个实参的每个元素依次添加到函数的动态参数args里面
# 例如： 传入函数两个参数[1,2,3](22,33)，最终args为(1,2,3,22,33)

# 3. 写函数，接收两个数字参数，将较小的数字返回
# def func(a, b):
#     return (a if a < b else b)
#
#
# print(func(3, 2))

# 4. 接收n个参数，返回最大值和最小值（字典）
# def func(*args):
#     return {"最大值是:": max(args), "最小值是": min(args)}

##方式二(注意掌握)
# def func(*args):
#     max = args[0]
#     min = args[0]
#     for el in args:
#         if el > max:
#             max = el
#         if el < min:
#             min = el
#     return {"最大值是:": max, "最小值是:": min}
#
#
# print(func(3, 2, 1, 100, 0, -20))

# 5. 写函数，传入一个参数n，返回n的阶乘
# def func(content):
#     sum = 1
#     n = 1
#     while n <= content:
#         sum = sum * n
#         n += 1
#     return sum
#
#
# print(func(4))

# 6. 返回扑克字典
# color = ["红桃", "黑桃", "梅花", "方块"]
# num = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# result = []
# for dianshu in num:
#     for el in color:
#         result.append((dianshu,el))
# print(result)

# 7. 有函数定义如下，判断结果
# def calc(a, b, c, d=1, e=2):
#     return (a + b) * (c - d) + e
#
#
# print(calc(1, 2, 3, 4, 5))  # 2
# #print(calc(1, 2))  # error
# print(calc(e=4, c=5, a=2, b=3))  # 24
# print(calc(1, 2, 3))  # 8
# print(calc(1, 2, 3, e=4))  # 10
# # print(calc(1,2,3,d=5,4))  # error


# 如果默认值参数是一个可变的数据类型, 如果有人调用的时候改变了他. 其他位置看到的也跟着改变了
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# print('list1=%s' % list1)  # list = [10]
#
# list2 = extendList(123, [])
# print('list2=%s' % list2)  # [123]
#
# list3 = extendList('a')  # list = [10, 'a']
# print('list3=%s' % list3)
