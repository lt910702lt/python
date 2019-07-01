import socket
import time
import threading


def func():
    sk = socket.socket()
    sk.connect(('127.0.0.1', 8080))
    time.sleep(1)
    sk.send(b'hi')
    print(sk.recv(10))
    sk.close()


for i in range(10):
    threading.Thread(target=func, ).start()
