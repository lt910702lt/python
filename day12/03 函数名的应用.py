def func():
    print("你吃了吗")


# func()
#
# a = func
# print(a)
# a() #就是一个函数的调用

def a():
    print("我吃了")


# func = a
# func()
#
# a = 8
# b = 7
# c = 3
# d = 1
# lst = [a, b, c, d]
# print(lst)

def f1():
    print("我是马云")


def f2():
    print("我是马化腾")


def f3():
    print("我是马赛克")


def f4():
    print("我是马蔚华")


lst = [f1, f2, f3, f4]
for el in lst:
    el()
