# setblocking方法
'''
在默认情况下，sk.accept()，conn.recv()是一个阻塞状态，会一直等待连接请求
而setblocking方法可以让其跳过，直接执行下一步的操作
'''
import socket

sk = socket.socket()
sk.setblocking(False)
sk.bind(('127.0.0.1', 8080))
sk.listen()
# 这里会报错，需要抛一下异常
try:
    conn, addr = sk.accept()
except BlockingIOError:
    pass
print('+++++++++++++')
