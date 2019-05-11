# # *args：动态参数，接收所有的非位置参数
# # **kwargs：动态参数，接收所有的位置参数
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     # print(*args)
#     # print(**kwargs)   #**在执行时，打散（print(**{'name':'alex','age':'1000'})）,而print无法接收关键字参数，因此报错！
#
# # * : 当定义一个函数的时候：*代表 聚合
# #     当执行一个函数的时候：*代表 打散
# # func(1, 2, 3, name='alex', age=1000)
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# func(l1, l2)    #([1, 2, 3], [4, 5, 6])
# func(*l1, *l2)  #(1, 2, 3, 4, 5, 6)

##猜结果函数1
# def func1():
#     a = 1
#     b = 2
#     print(a)
#
#     def func2():
#         b = 3
#         print(b)
#
#     print(666)
#     func2()
#     print(111)
#
#
# func1()     # 1 666 3 111

# #猜结果函数2
# def func1():
#     a = 1
#     b = 2
#     print(a)
#
#     def func2():
#         b = 3
#         print(b)
#
#     print(666)
#     return func2
#
#
# func1()()   #1 666 3

l1 = [i for i in range(1, 100)]
l2 = [i for i in range(1, 100) if i > 50]
