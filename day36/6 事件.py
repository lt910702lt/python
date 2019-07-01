# 事件
# 所有的阻塞 都是同步阻塞
# recv accept input sleep
# 阻塞多个进程    异步阻塞
# lock 10进程
# 事件 -- 异步阻塞
# 事件：通知、标识，可以同时使多有的进程，都陷入阻塞

# from multiprocessing import Event
#
# e = Event()  # 实例化一个事件 标志/红绿灯
# e.set()     # 将标志变成非阻塞（交通灯变绿）
# e.wait()    # 刚实例化出来的一个事件对象，默认的信号是阻塞信号
#             # 执行到wait，要先看灯，绿灯行红灯停，如果在停的过程中灯绿了，就变成非阻塞了
# e.clear()   # 将标志变成阻塞（交通灯变红）
#
# e.is_set()  # 是否阻塞，True是绿灯，False就是红灯

# 红绿灯题目
# import time
# import random
# for i in range(100):
#     if i%6 == 0:
#         time.sleep(random.randint(1,3))
#     print(i)

import time
import random
from multiprocessing import Process
from multiprocessing import Event


def triffic_light(e):
    while True:
        if e.is_set():
            time.sleep(3)
            print('红灯亮')
            e.clear()  # 绿变红
        else:
            time.sleep(3)
            print('绿灯量')
            e.set()  # 红变绿


def car(i, e):
    e.wait()
    print('%s车通过' % i)


if __name__ == '__main__':
    e = Event()  # 立一个红绿灯
    tra = Process(target=triffic_light, args=(e,))
    tra.start()
    for i in range(50):
        if i % 3 == 0:
            time.sleep(random.randint(1, 3))
        car_pro = Process(target=car, args=(i, e))
        car_pro.start()
