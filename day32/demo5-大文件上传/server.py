# 实现一个大文件的上传或下载
import socket
import struct
import json

buffer = 1024   #这里如果是4096，暂时会报错

sk = socket.socket()
sk.bind(('127.0.0.1', 8090))
sk.listen()
conn, addr = sk.accept()

# 接收
head_len = conn.recv(4)
head_len = struct.unpack('i', head_len)[0]
json_head = conn.recv(head_len).decode('utf-8')
head = json.loads(json_head)
filesize = head['filesize']

with open(head['filename'], 'wb') as f:
    while filesize:
        if filesize >= buffer:
            content = conn.recv(buffer)
            f.write(content)
            filesize -= buffer
        else:
            content = conn.recv(filesize)
            break
conn.close()
sk.close()
