# 进程 执行中的程序
# 线程 轻量级的进程

# 进程可以处理一个任务
# 听课 + 记笔记 + 看屏幕

# 进程 一个时间点 只能做一个事

# 对于一个人来说，一个人就是一个进程
# 一个人可以做的多件事情，每一件事都是一个线程
# 进程包含着线程

# 进程是资源分配的最小单位，线程是CPU调度的最小单位

# 开进程时间 - 长 , 开线程时间 - 短
# cpu在进程之间切换 - 慢，在线程之间切换 - 快

# 如果两个任务 需要共享内存 又想实现异步 多线程
# 如果两个任务 需要数据隔离 多进程

# 多线程的优点：轻量级，多线程数据共享

# GIL 全局解释器锁 -- 同一时间，只会有一个线程被CPU执行

# 一个程序中，可以同时有多进程和多线程

# ----------启动一个线程------------------
# from threading import Thread
# import os
# import time
#
#
# def func():
#     time.sleep(1)
#     print('我是线程', os.getpid())
#
#
# t = Thread(target=func)
# t.start()
# print(os.getpid())

# ----------启动多个线程------------------
from threading import Thread
import os
import time


def func():
    time.sleep(1)
    print('hello world', os.getpid())

thread_lst = []
for i in range(10):
    t = Thread(target=func)
    t.start()
    thread_lst.append(t)
[t.join() for t in thread_lst]
print(os.getpid())
