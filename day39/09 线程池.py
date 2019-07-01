import time
import random
from concurrent import futures

'''
线程池 和 进程池，是用来坐池操作的最新进的模块
1、开启线程池需要成本，比开启进程池要低
2、高I/O的情况下，多开线程
3、不能任意开启多个线程
4、开启线程池
'''


# futures.ThreadPoolExecutor  # 线程池 cpu个数*5
# futures.ProcessPoolExecutor # 进程池 cpu个数+1

# def funamame(n):
#     print(n)
#     time.sleep(random.randint(1,3))
#
#
#
# thread_pool = futures.ThreadPoolExecutor(3)
# for i in range(10):
#     thread_pool.submit(funamame, 'hello world')     # submit合并了创建线程对象和start的功能


# ------------------------------------------
# 回调函数add_done_callback(call)
def funcname(n):
    print(n)
    time.sleep(random.randint(1, 3))
    return n * '*'


def call(args):
    print(args.result())


thread_pool = futures.ThreadPoolExecutor(5)

thread_pool.submit(funcname, 3).add_done_callback(call)

# 统一了入口和方法 简化了操作 降低了学习的时间成本