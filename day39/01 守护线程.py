from threading import Thread
import time


def func():
    print('开始执行子线程')
    time.sleep(3)
    print('子线程执行完毕')


t = Thread(target=func)
t.setDaemon(True)   #进程设置守护进程是一个属性：p.daemon = True
t.start()

# 守护线程 守护进程 都是等待主进程或者主线程中的代码 执行完毕
#
