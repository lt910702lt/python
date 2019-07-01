import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    sk.send(b'hi')
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
    time.sleep(1)
sk.close()