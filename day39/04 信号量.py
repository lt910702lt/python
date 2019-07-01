import time
import random
from threading import Semaphore
from threading import Thread


def func(n, sem):
    sem.acquire()
    print('thread -%s start' % n)
    time.sleep(random.randint(1,3))
    print('thread -%s done' % n)
    sem.release()


sem = Semaphore(5)  # 一把锁5把钥匙
for i in range(20):
    t = Thread(target=func, args=(i, sem))
    t.start()

# 信号量 和 线程池 有什么区别？
'''
相同点： 在信号量acquire之后，和线程池一样，同时在执行的只能有n个
不同点：
    1、开的线程数不一样，对于线程池来说，一共就只开5个线程，信号量有几个任务就有几个线程，只是无法同时执行
对有信号量的程序来说，可以同时执行很多个线程吗？
    答：可以。实际上，信号量并不影响线程或进程的并发，只是在加锁的阶段进行流量限制
'''