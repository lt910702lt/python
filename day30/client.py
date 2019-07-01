import socket
# sk = socket.socket()    # 买手机
#
# sk.connect(('127.0.0.1',8080))     #拨号，别人的！！
#
# sk.send(b'ni hao a')
# ret = sk.recv(1024)
# print(ret)
#
# sk.send(bytes('中午吃的什么呀？',encoding='utf-8'))
#
# ret = sk.recv(1024)
# print(ret.decode('utf-8'))
# sk.close()

# -----------------------------------------------------
sk = socket.socket()
sk.connect(('127.0.0.1',8080))
while True:
    info = input('>>>')
    sk.send(bytes(info,encoding='utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        sk.send(bytes('bye'))
sk.close()
