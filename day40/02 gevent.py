from gevent import monkey;monkey.patch_all()    #会把下面内倒入的所有模块的I/O都打成一个报包
import time
# gevent模块：遇到认识的I/O会自动切换
import gevent   # greenlet gevent在切换程序的基础上，又实现了规避I/O
from threading import current_thread

def func1():
    print(current_thread().name)
    print(123)
    time.sleep(1)
    print(456)


def func2():
    print(current_thread().name)
    print('hahaha')
    time.sleep(1)
    print('hehehe')


g1 = gevent.spawn(func1)
g2 = gevent.spawn(func2)
# g1.join()
# g2.join()
gevent.joinall([g1, g2])
