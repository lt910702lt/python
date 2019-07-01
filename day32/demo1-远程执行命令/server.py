# 负责下发命令给client端
import socket

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
    res = conn.recv(1024).decode('gbk')
    print(res)
conn.close()
sk.close()
