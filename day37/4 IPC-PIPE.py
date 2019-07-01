# ipc机制 -- 队列
# ipc机制 -- 管道 pipe -- 双向通道，都可以发和收
# from multiprocessing import Pipe
#
# p1, p2 = Pipe()
# # send  发送
# p1.send('hello')
# # recv  接收
# print(p2.recv())
# p2.send('hi')
# print(p1.recv())
# # close 关闭
# p2.close()
# p1.close()

'''
close方法
管道：双向通信
注意关闭foo和son
'''
from multiprocessing import Process
from multiprocessing import Pipe


def func(p):
    foo, son = p
    foo.close()
    while True:
        try:
            print(son.recv())
        except EOFError:
            break

    # print(son_p.recv())
    # print(son_p.recv()) #已经消费完了,再次消费会报错EOFError


if __name__ == '__main__':
    foo, son = Pipe()
    p = Process(target=func, args=((foo, son),))
    p.start()
    # 需要关闭son，不影响子进程
    son.close()
    foo.send('hello')
    foo.send('hello')
    foo.send('hello')
    foo.close()
