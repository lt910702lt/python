'''
多路复用的机制：
    1、select：windows只有select，linux三者皆有
    2、poll
    3、epoll

    select 和 poll 轮询 ，conn越多就越会照成时延，不适合大并发！
    epoll 能处理多对象，不使用轮询，而使用回调函数  -- linux

多路复用的过程：
    1、import select; select([conn1,conn2,conn3,conn4])
    2、想要接收的数据 --> 通知操作系统
    3、操作系统等待数据(同时监听多个conn)
    4、当有数的的时候，操作系统通知进程有数据来了
    5、程序回复操作系统，我可以开始接收数据了
    6、操作系统copydata

'''