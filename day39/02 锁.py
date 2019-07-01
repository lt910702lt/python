# 数据不安全
# 为什么有了GIL锁，数据还不安全？因为 GIL是一个线程锁，针对同一时刻，只能运行一个线程
'''
针对数据不安全:
一个CPU时间片，第一个线程拿到了数据，但是还没有进行运算，这个CPU的时间片就切到了另外一个线程，
另外一个线程经过了运算后，CPU时间片又切换回原来的线程，原来的线程再去执行数据操作，计算的数据
还是最开始的数据，而不是第二个线程计算后的结果！

针对这种情况，需要对数据也加锁，即使切换了时间片，但是锁任然在原来的线程上，仍然未被释放~~

GIL锁：锁线程，不是数据锁
本章的锁：锁数据
'''
#------------加锁------------------
from threading import Thread
from threading import Lock
import time


def func():
    global n
    lock.acquire()
    temp = n  # 从进程中获取n
    time.sleep(0.01)
    n = temp - 1  # 得到结果，再存储回进程
    lock.release()
    # n -= 1

n = 100
lock = Lock()
t_lst = []

for i in range(100):
    t = Thread(target=func)
    t.start()
    t_lst.append(t)
[t.join() for t in t_lst]
print(n)

# 虽然加了锁，数据安全了，但是速度慢，和join差不多了
