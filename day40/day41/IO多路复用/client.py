# import time
# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1',8080))
# time.sleep(10)
# sk.send(b'hello')
# time.sleep(10)
# sk.close()
# ------------------------------------
# 客户端来一个并发的
import time
import socket
import threading


def client_async(args):
    sk = socket.socket()
    sk.connect(('127.0.0.1', 8080))
    for i in range(10):
        time.sleep(2)
        sk.send(('%s[%s] : hello' % (args, i)).encode('utf-8'))
        print(sk.recv(1024))
    sk.close()


for i in range(10):
    threading.Thread(target=client_async, args=(i * '*',)).start()
