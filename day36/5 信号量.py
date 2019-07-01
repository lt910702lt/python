# 信号量
# from multiprocessing import Semaphore
#
# sem = Semaphore(4)
# sem.acquire()  # 需要钥匙
# print(0)
# sem.acquire()
# print(1)
# sem.acquire()
# print(2)
# sem.release()
# sem.acquire()
# print(3)
# sem.acquire()
# print(4)

# 举例：迷你唱吧，20个屋子，同时只能进4人
from multiprocessing import Semaphore
from multiprocessing import Process
import time
import random


def sing(i, sem):
    sem.acquire()
    print('%s : 进入ktv' % i)
    time.sleep(random.randint(1, 10))
    print('%s : 离开ktv' % i)
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(20):
        p = Process(target=sing, args=(i, sem))
        p.start()
