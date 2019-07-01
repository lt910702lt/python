'''
Event
flag标志
刚刚创建的时候，flga=False
wait() flag=False 阻塞
       flag=True  非阻塞
set() Fase --> True
clear() True -- > False
'''

# 连接mysql数据库
'''
连接三次数据库
每0.5秒连接一次
创建一个事件，来标志数据库的连接情况
如果连接成功，就显示成功
否则，就报错
'''

import time
import random
from threading import Event
from threading import Thread


def conn_mysql():
    count = 1
    while not e.is_set():
        if count > 3:
            raise TimeoutError
        print('尝试连接第%s次'% count)
        count += 1
        e.wait(0.5)

# 检测数据库的链接是否正常
def check_conn():
    # 模拟连接检测时间
    time.sleep(random.randint(1,3)) # 检测
    e.set() # 告诉时间的标志数据库可以连接



e = Event()
check = Thread(target=check_conn)
check.start()
conn = Thread(target=conn_mysql)
conn.start()
