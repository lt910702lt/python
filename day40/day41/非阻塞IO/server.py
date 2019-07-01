import time
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
sk.setblocking(False)   #设置不阻塞,打开非阻塞的开关
conn_lst = []

while True:
    try:
        conn, addr = sk.accept()
        conn_lst.append(conn)
    except BlockingIOError:
        del_lst = []
        for i in conn_lst:
            try:
                msg = i.recv(10).decode('utf-8')
                if not msg:
                    i.close()
                    del_lst.append(i)
                else:
                    print(msg)
                    i.send(msg.upper().encode('utf-8'))
            except BlockingIOError:
                pass
        if del_lst:
            for del_item in del_lst:
                conn_lst.remove(del_item)
