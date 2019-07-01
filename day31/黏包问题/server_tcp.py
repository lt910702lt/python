# 基于tcp实现远程执行命令
# 在server端下发命令
# 在client端执行命令，并返回
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
while True:
    cmd = input('>>>')
    conn.send(cmd.encode('utf-8'))
    ret = conn.recv(1024).decode('utf-8')
    print(ret)

conn.close()
sk.close()

# 根据上面的代码，会发生数据紊乱的现象
# send的一条消息，没有接收完
# 下一次发送的时候又一起发送~~
# 这就是黏包现象
# tcp会出现黏包，但是不会出现丢包，udp不会出现黏包