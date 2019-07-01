# 提供服务
# 接收信息 时间的格式
# 将我的时间转换成接收到的格式
# 再发送回客户端

import socket
import time

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))

while True:
    msg, addr = sk.recvfrom(1024)
    ret = msg.decode('utf-8')
    if ret == '1':
        res = str(time.time()).encode('utf-8')
        sk.sendto(res, addr)
    elif ret == "2":
        res = str(time.localtime()).encode('utf-8')
        sk.sendto(res, addr)
    elif ret == '3':
        res = time.strftime('%Y-%m-%d %H:%M:%S').encode('utf-8')
        sk.sendto(res, addr)
    elif ret.upper() == 'Q':
        break
    else:
        res = 'please input 1|2|3'.encode('utf-8')
        sk.sendto(res, addr)
sk.close()
