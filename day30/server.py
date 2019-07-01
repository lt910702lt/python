import socket
# sk = socket.socket()     # 买手机
# sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #避免服务重启的时候报address already in use
# # sk.bind(('ip','port'))
# sk.bind(('127.0.0.1',8080))               # 绑定手机卡
# sk.listen()              # 监听，等着有人打电话
#
# # sk.accept()             # 接收到别人的电话，connection 链接，address 对端地址
# conn,addr = sk.accept()
#
# #conn.recv(1024)                 # 听别人说话
# conn.recv(1024)
#
# #conn.send()                     # 和别人说话,必须传一个bytes类型
# conn.send(b'hi')
#
# ret = conn.recv(1024)
# print(ret.decode('utf-8'))
# conn.send(bytes('大碗油泼面',encoding='utf-8'))
#
# #conn.close()                    # 挂电话
# conn.close()
#
# #sk.close()                      # 关手机
# sk.close()
#
#
# # 有收必有发，收发必相等

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
while True:
    ret = conn.recv(1024).decode('utf-8')
    if ret == 'bye':
        break
    print(ret)
    info = input('>>>')
    conn.send(bytes(info,encoding='utf-8'))
sk.close()