'''
1、协程的概念。 对于协程来说始终是在一个线程之间切换
2、如何实现在两个函数之间的切换？

greenlet模块：切换执行
gevent协程模块，内部也是实现了greenlet模块的封装

在代码之间切换执行，反而会降低效率，切换不能规避IO时间
如果在同一个程序中，有IO的情况下才切换，效率会提高很多
yield，greenlet 也无法规避IO时间
'''

# 用yeild实现两个函数交替执行
# def func1():
#     print(1)
#     yield
#     print(3)
#     yield
#
#
# def func2():
#     g = func1()
#     next(g)
#     print(2)
#     next(g)
#     print(4)
#
# func2()
# -----------------------------------
# 用yeild实现生产者 - 消费者模型
# def consumer():
#     while True:
#         n = yield
#         print('消费了一个包子%s'% n)
# def producer():
#     g = consumer()
#     next(g)
#     for i in range(10):
#         print('生产了包子%s'% i)
#         g.send(i)
# producer()

# -----------------------------------
# greenlet模块+switch()方法
# from greenlet import greenlet       #在单线程中切换状态的模块
# def eat1():
#     print('吃鸡腿1')
#     g2.switch()
#     print('吃鸡腿2')
#     g2.switch()
#
# def eat2():
#     print('吃饺子1')
#     g1.switch()
#     print('吃饺子2')
#
# g1 = greenlet(eat1)
# g2 = greenlet(eat2)
# g1.switch()

# -----------------------------------
# 协程的切换，不能规避IO的时间