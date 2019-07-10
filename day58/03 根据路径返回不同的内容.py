import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

while True:
    conn, addr = sk.accept()
    data = conn.recv(9000)
    first_line = str(data, encoding='utf8').split('\r\n')[0]
    url = first_line.split(' ')[1]
    print(url)
    if url == '/yingying':
        msg = b'hands up!'
    elif url == '/alex':
        msg = b'stone!'
    else:
        msg = b'404 not fond!'
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(msg)
    conn.close()
