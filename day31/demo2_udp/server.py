import socket

sk = socket.socket(type=socket.SOCK_DGRAM)  # dagagram，数据报文
sk.bind(('127.0.0.1', 8080))

# sk.recvfrom(1024)       #udp的连接，不需要listing，直接resvfrom
msg, addr = sk.recvfrom(1024)

print(msg.decode('utf-8'))
sk.sendto(b'byebye', addr)

sk.close()

# udp的server 不需要进行监听， 也不需要建立连接
# 在启动服务之后只能被动的等待客户端发送消息过来
# 客户端发送消息的同时，还会自带地址信息
# 消息回复的时候，不仅要发送消息，还要把对方的地址填写上