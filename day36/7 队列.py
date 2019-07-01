# 进程之间的通信
# 子进程与子进程之间的通信
# from multiprocessing import Queue
# q = Queue()   # 实例化一个队列
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())  # 如果队列里面没有值了，就会阻塞等待一个值
# 1、进程之间通信，可以使用multiprocessing的Queue模块
# 2、队列由两种创建方式，第一种不传参数，这个队列就没有长度限制；传参数，创建一个有最大长度限制的队列
# 3、提供两个重要方法：put get
# 4、qsize

# from multiprocessing import Process
# from multiprocessing import Queue
#
#
# def q_put(q):
#     q.put('hello')
#
#
# def q_get(q):
#     print(q.get())
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=q_put, args=(q,))
#     p.start()
#     p1 = Process(target=q_get, args=(q,))
#     p1.start()

# 通过队列，实现了主进程与子进程的通信，子进程与子进程的通信
# 生产者消费者模型

# 我要生产一个数据，然后给一个函数，让这个函数依赖这个数据进行运算，拿到结果 -- 同步过程

# 生产者-消费者模型（做包子-吃包子）
from multiprocessing import Queue
from multiprocessing import Process
import time


def producer(q):
    for i in range(100):
        q.put('包子%s' % i)


def consumer(q):
    for i in range(100):
        time.sleep(1)
        print(q.get())


if __name__ == '__main__':
    q = Queue()  # 托盘
    p = Process(target=producer, args=(q,))
    p.start()
    c = Process(target=consumer, args=(q,))
    c.start()
