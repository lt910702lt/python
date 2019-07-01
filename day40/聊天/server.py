from gevent import monkey

monkey.patch_all()
import gevent
import socket


def talk(conn):
    while True:
        ret = conn.recv(1024).decode('utf-8')
        print(ret)
        conn.send(ret.upper().encode('utf-8'))
    conn.close()


sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
while True:
    conn, addr = sk.accept()
    gevent.spawn(talk,conn)

sk.close()
