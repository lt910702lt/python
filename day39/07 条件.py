# 条件 Condition() = 锁 + wait功能
'''
方法：
acquire()
release()
wait()
notity()
notify_all()
'''
from threading import Condition
from threading import Thread
import threading


def run(n):
    con.acquire()
    con.wait()
    print('\nrun the thread: %s' % n)
    con.release()


if __name__ == '__main__':
    con = Condition()
    for i in range(10):
        t = Thread(target=run, args=(i,))
        t.start()
    while True:
        inp = input('>>>')
        if inp.upper() == 'Q':
            break
        con.acquire()
        con.notify(int(inp))    # 传递信号给条件，notify(1) -->可以放行一个线程
        con.release()
        print('***')
