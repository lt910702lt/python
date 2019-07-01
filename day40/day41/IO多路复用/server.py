import select
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

# # 使用多路复用select
# while True:
#     # def select(rlist, wlist, xlist, timeout=None):
#     rl, wl, xl = select.select([sk], [], [])  # 阻塞在此，三个列表分别为可读，可写，可执行
#     # print(ret)  # ([<socket.socket fd=520, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080)>], [], [])
#     print(rl)  # rl里面全是socket
#     for i in rl:
#         conn, addr = i.accept()
# --------------------------------
# 设置rlist的列表,默认有一个sk。这个程序实现在同一时刻，select只接收到一个数据（sk或者conn的数据）
# read_list = [sk]
# while True:
#     # 开启多路复用，阻塞在此
#     rl, wl, xl = select.select(read_list, [], [])
#     # 有连接了，打印rl
#     print(rl)
#     # 判断是否为socket接收到数据，如果是，则得到conn，并将其放入select阻塞里面
#     if rl[0] == sk:
#         conn, addr = rl[0].accept()
#         print(conn, addr)
#         read_list.append(conn)
#     # 判断是否为socket接收到数据，如果不是sk，那么就是一个conn，通过这个conn处理数据
#     else:
#         ret = rl[0].recv(1024)
#         print(ret)
#         # 判断conn获取数据是否为0，如果是0，则是断开conn，随即将conn移除出select
#         if not ret:
#             rl[0].close()
#             read_list.remove(rl[0])

# -----------------------------------------------------
# select可以并发收到sk或者conn的数据实现
read_lst = [sk]
while True:
    rl, wl, xl = select.select(read_lst, [], [])
    for item in rl:
        if item == sk:
            conn, addr = item.accept()
            read_lst.append(conn)
        else:
            ret = item.recv(1024).decode('utf-8')
            if not ret:
                item.close()
                read_lst.remove(item)
            else:
                print(ret)
                item.send(('reveived %s' % ret).encode('utf-8'))
