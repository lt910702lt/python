import socket
from multiprocessing import Process


def talk(conn):
    conn.send(b'connected')
    ret = conn.recv(1024)
    print(ret)


if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8080))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        p = Process(target=talk, args=(conn,))
        p.start()
    conn.close()
    sk.close()
