import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


def yingying(url):
    data = 'ni fang wen de shi: {}'.format(url)
    return bytes(data, encoding='utf8')


def alex():
    data = 'alex de diannao bei tou le!'
    return bytes(data, encoding='utf8')


while True:
    conn, addr = sk.accept()
    data = conn.recv(9000)
    first_msg = str(data,encoding='utf8').split('\r\n')[0]
    url = first_msg.split(' ')[1]
    if url == '/yingying':
        msg = yingying(url)
    elif url == '/alex':
        msg = alex()
    else:
        msg = b'404 not fond!'
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(msg)
    conn.close()
