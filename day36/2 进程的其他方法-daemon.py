# start 开启一个进程
# join 用join可以让主进程等待子进程结束

# 守护进程
# 守护进程会跟随着主进程的代码执行结束而结束
# 正常的子进程没有执行完的时候，主进程要一直等着

# -------------------------------------------------
# 主进程执行完了，子进程还在执行
import time
from multiprocessing import Process


# def cal_time():
#     while True:
#         time.sleep(1)
#         print('过去了1秒')
#
#
# if __name__ == '__main__':
#     p = Process(target=cal_time)
#     p.start()
#     for i in range(100):
#         time.sleep(0.1)
#         print('*' * i)

# 设置一个守护进程
# 1、守护进程会跟随着主进程的代码执行结束而结束
# 2、守护进程要在start之前设置
# 3、在守护进程中，不能再开启子进程
def cal_time():
    while True:
        time.sleep(1)
        print('过去了1秒')


if __name__ == '__main__':
    p = Process(target=cal_time)
    p.daemon = True  # 设置位守护进程，注意必须要在进程启动前执行
    p.start()
    for i in range(100):
        time.sleep(0.1)
        print('*' * i)
