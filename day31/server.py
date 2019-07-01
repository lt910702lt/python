# tcp连接时长连接，会占着连接
import socket

sk = socket.socket()  # 买手机，创建一个socket对象
sk.bind(('127.0.0.1', 8080))  # 给server端绑定一个端口
sk.listen()
conn, addr = sk.accept()  # 获取到一个客户端的连接，已经完成三次握手，建立了一个连接（阻塞在此）
while True:
    msg = conn.recv(1024).decode('utf-8')  # 阻塞，直到收到一个客户端发来的消息
    print(msg)
    if msg == 'bye':break
    info = input('>>>')
    if info == 'bye':
        conn.send(b'bye')
        break
    conn.send(info.encode('utf-8'))  # 发消息
conn.close()  # 关闭连接（tcp）
sk.close()  # 关闭socket对象，如果不关闭还能继续接收


# server client1 建立了长连接         #占线！
# client2 等待 直到client1连接断开