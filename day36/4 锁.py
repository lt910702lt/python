# 锁 就是在并发编程中 保证数据安全
# from multiprocessing import Lock
# lock = Lock()
# lock.acquire()  # 需要锁   拿钥匙
# lock.release()  # 释放锁   还钥匙

# 锁的使用案例
# from multiprocessing import Lock
# from multiprocessing import Process


# def func(num):
#     print(num)
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(20):
#         p = Process(target=func, args=(i,))
#         p.start()
# 抢票
import json
import time
import random
from multiprocessing import Process
from multiprocessing import Lock


def search(i):
    with open('ticket') as f:
        print(i, json.load(f)['count'])


def get(i):
    with open('ticket') as f:
        ticket_num = json.load(f)['count']
    time.sleep(random.random())
    if ticket_num > 0:
        with open('ticket', 'w') as f:
            json.dump({'count': ticket_num - 1}, f)
        print('%s抢到票了' % i)
    else:
        print('%s没票了' % i)


def task(i,lock):
    search(i)  # 查票
    lock.acquire()
    get(i)  # 抢票
    lock.release()

# 要加锁
if __name__ == '__main__':
    lock = Lock()
    for i in range(20):
        p = Process(target=task, args=(i,lock))
        p.start()
