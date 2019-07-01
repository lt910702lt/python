# 通过类来开启一个子进程注意事项
'''
1、这个类必须继承Process类
2、这个类必须实现run方法
3、参数的接收需要初始化__init__方法，并且__init__的时候需要实现父类的__init__方法：super().__init__()
4、类中方法的调用，通过在run方法内部调用来完成，如果在父进程执行的话，就不是在子进程里面执行的了
'''

import os
from multiprocessing import Process


# 这个类必须继承Process类
class MyProcess(Process):
    # 使用__init__来接收参数，不过必须实现父类Process的__init__方法
    def __init__(self, arg1, arg2, arg3):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    # 必须实现run方法
    def run(self):
        print('这里是子进程:%d,它父进程是:%d' % (os.getpid(), os.getppid()))
        print(self.arg1, self.arg2, self.arg3)
        self.wakl()

    def wakl(self):
        print('走路啊')


if __name__ == '__main__':
    # 实例化这个类
    p = MyProcess(1, 2, 3)
    # 启动子进程
    p.start()

    print('父进程: ', os.getpid())
