# from multiprocessing import Manager
# Pipe      管道  双向通信    数据不安全
# Queue     管道+锁    双向通信    数据安全
# JoinableQueue    put和get的一个计数机制，每次get数据之后，发送task_done，put端接收到计数-1，直到计数为0就能感知到
# Manager是一个类，提供了可以进行数据共享的一个机制 提供了很多数据类型 dict list
# 先定义一个manager的对象，然后通过这个对象来创建数据类型
# Manager: 不提供数据的安全

# if __name__ == '__main__':
#     m = Manager()
#     d = m.dict()
#     print(d)
#     d['count'] =0
#     print(d)

from multiprocessing import Manager
import time
from multiprocessing import Process


def func(dic):
    while True:
        print(dic)
        time.sleep(3)


if __name__ == '__main__':
    # d = {}
    m = Manager()
    d = m.dict()
    p = Process(target=func, args=(d,))
    p.start()
    d['count'] = 0
    p.join()    # 必须要执行join，才能正常
