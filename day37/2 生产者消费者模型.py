# 矛盾：解决 数据供需不平衡
# 同步 生产数据 使用数据
# 异步 主进程 生产数据 子进程使用数据
# 异步 子进程 生产数据 子进程处理数据

'''
3个子进程   生产泔水
2个子进程   吃泔水
生产的快    吃的慢     泔水溢出
生产的慢    吃的快     不够吃
如果增加生产者 -- 让生产变快
减少生产者 -- 找一个容器，约束容器的容量
'''

import time
import random
from multiprocessing import Process
from multiprocessing import Queue


def producer(q, food):
    for i in range(10):
        q.put('%s-%s' % (food, i))
        print('生产了%s' % food)
        time.sleep(random.randint(1, 3))
    q.put(None)


def consumer(q, name):
    while True:
        food = q.get()
        print('%s吃了%s' % (name, food))


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q, '泔水'))
    p1.start()
    p2 = Process(target=producer, args=(q, '骨头'))
    p2.start()
    c1 = Process(target=consumer, args=(q, 'alex'))
    c1.start()

# 列队不会不安全
# 现在，通过Queue，生产者消费者模型
    # 1.消费者要处理多少条数据是不确定的
    # 2.所以只能用while循环来处理数据，但是while循环无法结束
    # 3.需要生产者发送信号
    # 4.有多少个消费者，就需要发送多少个信号
    # 5.但是发送的信号数量，要根据生产者和消费者的数量进行计算，所以非常不方便
    # 6.引出了joinableQueue队列