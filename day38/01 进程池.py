import time
from multiprocessing import Pool
import os

# def func(i):
#     time.sleep(1)
#     i += 1
#     print(i)
#
#
# if __name__ == '__main__':
#     p = Pool(4)
#     for i in range(10):
#         # p.apply(func, args=(i,))    #apply是一个同步调用（顺序执行，没有并发效果，平时基本不用，都用异步）
#         p.apply_async(func, args=(i,))  # apply是一个异步调用
#     p.close()  # 不能再往进程池中添加新的任务
#     p.join()  # 只能进程池中的所有任务直到执行结束

# ------------------------------------------------------
# 异步调用，用列表接收返回值，然后再打印列表
# def func(i):
#     i += 1
#     return i
#
#
# if __name__ == '__main__':
#     p = Pool(4)
#     res_l = []
#     for i in range(10):
#         res = p.apply_async(func, args=(i,))
#         res_l.append(res)
#     p.close()
#     p.join()
#     [print(res.get()) for res in res_l]
# ------------------------------------------------------
# 异步调用，使用map
# def func(i):
#     time.sleep(1)
#     i += 1
#     return i
#
#
# if __name__ == '__main__':
#     s = time.time()
#     p = Pool(4)
#     res_l = []
#     ret = p.map(func, range(10))    #map传参的时候，必须是一个可迭代的
#     print(ret)
#     print(time.time() - s)

# apply、apply_async、map

# 参数 回调函数
# 回调函数：执行完函数的返回值，传递给下一个函数执行
# 回调函数是在主进程完成的，不能传参，只能接收多进程函数的返回值
# 什么时候使用？，例子：
# 请求网页，网络延时 IO操作
# 单进程 10各页面 同时访问多个 - >多进程 分析页面 -> 回调函数
# def func(i):
#     print('子进程%s:%s' % (i, os.getppid()))
#     return i * '*'
#
#
# def call(arg):  # 回调函数是在主进程完成的，不能传参，只能接收多进程函数的返回值
#     print('回调函数%s' % os.getppid())
#     print(arg)
#
#
# if __name__ == '__main__':
#     print('主进程%s' % os.getppid())
#     p = Pool(5)
#     for i in range(10):
#         p.apply_async(func, args=(i,), callback=call)
#     p.close()
#     p.join()

# ---------------------------------------------------------
# 单进程 10各页面 同时访问多个 - >多进程 分析页面 -> 回调函数
# 多进程去访问多个网页，回调函数来计算每个网页的长度
# import requests
# from multiprocessing import Pool
#
#
# def get_url(url):
#     ret = requests.get(url)
#     return {'url': url, 'status_code': ret.status_code, 'content': ret.text}
#
#
# def parser(dic):
#     with open('result', mode='w') as f:
#         ret = str(dic['url'])+str(dic['status_code'])+str(len(dic['content']))
#         f.write(ret)
#
#
# if __name__ == '__main__':
#     url_l = [
#         'https://www.baidu.com',
#         'https://www.cnblogs.com',
#         'http://www.gdyzzd.com:8081/GDYY/',
#         'https://www4.bing.com/',
#         'https://mikanani.me/'
#     ]
#     p = Pool(4)
#     for url in url_l:
#         p.apply_async(get_url, args=(url,), callback=parser)
#     p.close()
#     p.join()


# Pool(4)
# 如果使用进程池 -- 都可以拿到返回值
# apply_async 异步调用
    # 在完成所有进程后，close表示不再接受新任务
    # join 让主进程等到子进程执行结束
    # 如果需要获得返回值，提价任务之后返回的对象.get()就可以获取返回值
    # callback 回调函数 : 主进程执行 参数是子进程执行函数的返回值
# map(func,iterable) ,map不支持callback