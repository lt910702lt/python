'''
单线程的效率和协程的效率之比
'''
from gevent import monkey;

monkey.patch_all()
import time
import gevent


# ----------单线程--------------
def task(args):
    time.sleep(1)
    print(args)


def sync_func():
    for i in range(10):
        task(i)


def async_func():
    g_1 = []
    for i in range(10):
        g_1.append(gevent.spawn(task, i))  # 给协程任务传参
    gevent.joinall(g_1)

start = time.time()
sync_func()
print(time.time()-start)    # 10.132195472717285

start = time.time()
async_func()
print(time.time()-start)    # 1.0054430961608887
