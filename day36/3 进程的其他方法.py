# 两个方法：
# is_alive: 判断进程是否存活
# terminate: 结束一个进程
from multiprocessing import Process
import time


# def func():
#     print('wahaha')
#     time.sleep(5)
#     print('qqxing')
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     print(p.is_alive())
#     time.sleep(0.1)
#     p.terminate()  # 关闭程序(异步)，只是用操作系统的接口去执行这个命令，至于什么时候去执行，由操作系统而定
#     print(p.is_alive())
#     time.sleep(1)
#     print(p.is_alive())

# ---------------------------------------------
# 两个属性
# pid   查看这个进程的pid
# name  查看这个进程的名字

# 在父进程里查看pid和name
# def func():
#     print('wahaha')
#     time.sleep(5)
#     print('qqxing')
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     print(p.name, p.pid)

# 在子进程里获取进程pid和name，需要用到class来定义子进程
class MyProcess(Process):
    def run(self):
        print(self.pid, self.name)


if __name__ == '__main__':
    p = MyProcess()
    p.start()
