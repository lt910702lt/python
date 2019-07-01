import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1',8080))

# while True:
i = 0
while i < 10:
    stamp = str(time.time())
    sk.send(bytes(stamp,encoding='utf-8'))
    time.sleep(10)
    i += 1
sk.send(bytes('bye',encoding='utf-8'))