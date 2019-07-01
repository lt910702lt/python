# 进程能无限开吗？
# cpu 16核 同时处理16个任务
# 160个进程/16 10*0101 = 0.1
# 100个任务
# 4核 --> 4个进程
# 第五个任务进来 占用进程 执行任务
# ------------------------------------
# 进程池：
# 造一个池子 放4个进程来完成工作
# 发任务
# 循环使用池子中的进程来完成任务
# 进程池 已经被实现了
from multiprocessing import Pool
from multiprocessing import Process
import time


# def func(i):
#     time.sleep(0.1)
#     print(i)
#
#
# if __name__ == '__main__':
#     p = Pool(5)  # 一般大小为cpu核数+1,可以通过os.cpu_count来查看
#     p.map(func, range(20))
#     p.close()   # 不允许再向进程池中添加任务了
#     p.join()
#     print('======>')

# 进程池和普通多进程执行时间对比
# 进程池
def func(i):
    i += 1


if __name__ == '__main__':
    p = Pool(5)
    start = time.time()
    p.map(func, range(100))
    p.close()
    p.join()
    print(time.time()-start)

# 多进程
def func(i):
    i += 1


if __name__ == '__main__':
    start=time.time()
    l =[]
    for i in range(100):
        p = Process(target=func,args=(i,))
        p.start()
        l.append(p)
    [i.join() for i in l]
    print(time.time()-start)