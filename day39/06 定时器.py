# Timer 定时开启一个线程
from threading import Timer


def hello():
    print('hello world')


# 定时开启一个线程，单位是秒
t = Timer(1, hello)

t.start()
