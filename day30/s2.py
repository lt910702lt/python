import socket
import time

'''
时间格式转换：
时间戳->结构化：localtime、gmtime
结构化->时间戳：mktime

格式化->结构化：strptime
结构化->格式化：strftime

'''
sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
conn,addr = sk.accept()
while True:
    ret = conn.recv(1024).decode('utf-8')
    if ret == 'bye':
        break
    #先将时间戳转化为结构化时间
    str_time = time.localtime(float(ret))
    #再将结构化转化为格式化
    for_time = time.strftime('%Y-%m-%d %H:%M:%S',str_time)
    #打印出格式化后的时间
    print(for_time)
sk.close()