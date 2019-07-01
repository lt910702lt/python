# struct模块
# 什么是固定长度的bytes
# 为什么要用固定长度的bytes
# import struct
#
# # struct.pack('i')    # 'i'代表int，即将要把一个数字转换成固定长度的bytes类型
# ret = struct.pack('i', 4096)
# print(ret)      # b'\x00\x08\x00\x00'
#
# num = struct.unpack('i',ret)    #获得一个元组类型的数据(4096,)
# print(num[0])

# ------------------------------------------
import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()
while True:
    cmd = input('>>>')
    if cmd.upper() == 'Q':
        conn.send(b'q')
        break
    conn.send(cmd.encode('gbk'))
    num = conn.recv(4)
    num = struct.unpack('i', num)[0]
    res = conn.recv(int(num)).decode('gbk')
    print(res)
conn.close()
sk.close()
