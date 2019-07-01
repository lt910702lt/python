# 使用类来开启线程
import os
import time
from threading import Thread


# class MyThread(Thread):
#     def run(self):
#         time.sleep(1)
#         print('hello world', os.getpid())
#
#
# t = MyThread()
# t.start()

# -----------------------------------
# 计算开启的线程数量
# class MyThread(Thread):
#     count = 0
#
#     def run(self):
#         MyThread.count += 1
#         time.sleep(1)
#         # print('hello world', os.getpid())
#
#
# for i in range(10):
#     t = MyThread()
#     t.start()
# print(t.count)

# -----------------------------------
# 初始化传参
# class MyThread(Thread):
#     count = 0
#
#     def __init__(self, arg1, arg2):
#         super().__init__()
#         self.arg1 = arg1
#         self.arg2 = arg2
#
#     def run(self):
#         time.sleep(1)
#         MyThread.count += 1
#         print('%s,%s,hello world,%s' % (self.arg1, self.arg2, os.getpid()))
#
#
# for i in range(10):
#     t = MyThread(i, i * '*')
#     t.start()
# print(t.count)

# -----------------------------------
# 其他操作
import threading

print(threading.enumerate())    #返回正在运行着的线程列表
print(threading.activeCount())