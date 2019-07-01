import time
import random
from multiprocessing import Process
from multiprocessing import JoinableQueue


# put q.join
# get 处理数据，task_done 消费完了

def producer(q, food):
    for i in range(5):
        q.put('%s-%s' % (food, i))
        print('生产了%s' % food)
        time.sleep(random.random())
    q.join()  # 等待消费者 把所有数据处理完


def consumer(q, name):
    while True:
        food = q.get()
        if food == None: break
        print('%s吃了%s' % (name, food))
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer, args=(q, '泔水'))
    p1.start()
    p2 = Process(target=producer, args=(q, '骨头'))
    p2.start()
    c1 = Process(target=consumer, args=(q, 'alex'))
    c1.daemon = True
    c1.start()
    c2 = Process(target=consumer, args=(q, 'egon'))
    c2.daemon = True
    c2.start()
    c3 = Process(target=consumer, args=(q, 'jin'))
    c3.daemon = True
    c3.start()

    p1.join()  # 等待p1代码执行完毕
    p2.join()  # 等待p2代码执行完毕

'''
1、生产者的数据全部被消费
2、生产者进程结束
3、主代码进程结束
4、消费者守护进程结束
'''
