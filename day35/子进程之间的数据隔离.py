# 数据隔离
# 进程与进程之间的数据是共享的
from multiprocessing import Process
def func():
    global n
    n = n-1
if __name__ == '__main__':
    n = 100
    p = Process(target=func)
    p.start()
    print('主进程: ',n)