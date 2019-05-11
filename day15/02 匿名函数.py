def func(n):
    return n * n


print(func(3))
print(func.__name__)  # 查看函数的函数名   func
# lambda匿名函数
# x 参数
# :后面是函数体（直接return的内容）
# a = lambda x: x * x  # 一行搞定一个函数，但是不能完成复杂的函数
# print(a)
# print(a(6))
#
b = lambda x, y: x + y
print(b(2, 3))
print(b.__name__)  # <lambda>
