'''
在不同的线程中，恰好要对两个数据进行操作
'''
# 科学家吃面

# from threading import Thread
# from threading import Lock
# import time
#
# chopsticks = Lock()  # 筷子锁
# noodle = Lock()  # 面条锁
#
#
# def eat(name):
#     chopsticks.acquire()
#     print('%s拿到筷子了' % name)
#     noodle.acquire()
#     print('%s拿到面条了' % name)
#     print('%s吃面' % name)
#     chopsticks.release()
#     noodle.release()
#
#
# def eat2(name):
#     noodle.acquire()
#     print('%s拿到面了' % name)
#     time.sleep(1)
#     chopsticks.acquire()
#     print('%s拿到筷子了' % name)
#     print('%s吃面' % name)
#     noodle.release()
#     chopsticks.release()
#
#
# Thread(target=eat, args=('alex',)).start()
# Thread(target=eat2, args=('etiantian',)).start()
# Thread(target=eat, args=('liutao',)).start()
# Thread(target=eat2, args=('fengj',)).start()
# Thread(target=eat, args=('wangj',)).start()

#--------------解决死锁RLock------------------
'''
from threading import Lock      互斥锁
from threading import RLock     递归锁
允许别人进行多个acquire，多个‘回’
'''
from threading import Thread
from threading import RLock
import time

noodle =chopsticks = RLock()  # 筷子锁
#noodle = RLock()  # 面条锁


def eat(name):
    chopsticks.acquire()
    print('%s拿到筷子了' % name)
    noodle.acquire()
    print('%s拿到面条了' % name)
    print('%s吃面' % name)
    chopsticks.release()
    noodle.release()


def eat2(name):
    noodle.acquire()
    print('%s拿到面了' % name)
    time.sleep(1)
    chopsticks.acquire()
    print('%s拿到筷子了' % name)
    print('%s吃面' % name)
    noodle.release()
    chopsticks.release()


Thread(target=eat, args=('alex',)).start()
Thread(target=eat2, args=('etiantian',)).start()
Thread(target=eat, args=('liutao',)).start()
Thread(target=eat2, args=('fengj',)).start()
Thread(target=eat, args=('wangj',)).start()