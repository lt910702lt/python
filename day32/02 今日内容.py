# 网络编程
# 重要协议: tcp udp ip arp
# 应用层的协议: http、https、ftp、smtp
# osi模型对应的协议在哪里

# 黏包问题
# 什么是黏包？
    #

'''
连续send两个小数据
两个recv，第一个recv特别小
远程执行命令的程序
ipconfig -> 2000字节
2000-1024 = 976
dir --> 200
200+976 --> 黏包
    # 2
    # 8
两个recv，第一个recv特别小
    # recv（数据的长度）
本质：你不知道到底要接收多大的数据

解决：
首先 发送一下这个数据有多大
再按照数据的长度接收数据

'''

# 我们在网络上传输的所有数据，都叫数据包
# 数据包里的所有数据 都叫报文
# 报文里不止有你的数据 ip地址 mac地址 端口号
# 所有的报文 都有报头
# 协议 包头 接收多少字节
# 自己定义报文
    # 比如说 复杂的应用上就会用到
    # 传输文件的时候就够复杂了
        # 文件的名字
        # 文件的大小
        # 文件的类型
        # 存储的路径
head = {'filename':'test','filesize':409600,'filetype':'txt','filepath':r'\user\bin'}
# 报头的长度                  # 先接收4个字节
# send(head)    # 报头        # 根据这四个字节获取报头
# send(file)    # 报文        # 从报头中获取filesize，然后根据filesize接收文件