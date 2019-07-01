import os
import time
# print(os.getpid())      # 获取进程ID
# print(os.getppid())     # 获取父进程ID
# time.sleep(100)

# python当中创建进程来替我做事
# multiprocess模块，是一个综合的、管理进程的包

# Process 和创建进程相关
from multiprocessing import Process


# 进程的使用
# def func():
#     print('子进程：', os.getpid())
#     print('父进程：', os.getppid())
#     print(123)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)  # 创建一个进程对象
#     print('主进程：', os.getpid())
#     p.start()  # 执行start才开始执行进程。告诉操作系统我要创建的进程，是异步的！！
#     print('主进程：', os.getpid())

# -------------------------------------------------------------
# 进程传参
def func(money):
    print('取钱 : %d' % money)


if __name__ == '__main__':
    # 给子进程传参，args=(,)，args内容必须是元组，如果只有一个，也需要用逗号','
    p = Process(target=func, args=(1,))
    p.start()
    p.join()  # 先执行子进程的内容，然后再往下执行，但是程序又阻塞了。
    print('取完钱了')

'''
创建进程对象，传要执行的函数以及参数
进程对象.start()
主进程和子进程就是异步执行
如果主进程中的代码已经结束了，子进程还没有结束，主进程会等待子进程

p.join就是主进程会阻塞在join的位置，等待p进程结束
在windows操作系统中，创建进程的语句一定要放在if __name__ == '__main__':条件语句下
'''
