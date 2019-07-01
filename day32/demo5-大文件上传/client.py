# 发送端
import socket
import json
import os
import struct

buffer = 1024

sk = socket.socket()
sk.connect(('127.0.0.1', 8090))

# 发送文件
# 定制一个报头
head = {'filepath': r'F:\01-视频\05-docker',
        'filename': r'12-1 不是总结的总结.mp4',
        'filesize': None}
file_path = os.path.join(head['filepath'], head['filename'])
filesize = os.path.getsize(file_path)
head['filesize'] = filesize
# 字典转换为字符串
json_head = json.dumps(head)
# 字符串转换为bytes
bytes_head = json_head.encode('utf-8')
# 计算head的长度
head_len = len(bytes_head)  # 报头的长度
pack_len = struct.pack('i', head_len)
#先发报头的长度
sk.send(pack_len)
#再发送bytes类型的报头
sk.send(bytes_head)
#打开需要传输的文件
with open(file_path,'rb') as f:
        while filesize:
                if filesize >= buffer:
                        content = f.read(buffer)        #每次读取出来的内容
                        sk.send(content)
                        filesize -= buffer
                else:
                        content = f.read(filesize)
                        sk.send(content)
                        break
sk.close()