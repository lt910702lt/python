# 开启多个子进程
import os
import time
from multiprocessing import Process


# def func():
#     print('子进程%d干的事,父进程：%d' % (os.getpid(), os.getppid()))
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p1 = Process(target=func)
#     p2 = Process(target=func)
#     p.start()
#     p1.start()
#     p2.start()
#     p.join()
#
#     print('-----------主进程------------')

# --------------------------
# 多进程之间的先执行
def func(i):
    time.sleep(1)
    print('%d: 子进程%d干的事,父进程：%d' % (i, os.getpid(), os.getppid()))
if __name__ == '__main__':
    p_lst = []
    for i in range(10):
        p=Process(target=func,args=(i,))
        p.start()
        p_lst.append(p)
    for p in p_lst:
        p.join()
    print('-----------主进程------------')
