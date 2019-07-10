import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


def yingying(url):
    data = 'ni fang wen de shi: {}'.format(url)
    return bytes(data, encoding='utf8')


def alex(url):
    data = 'alex de shou ji bei tou le,haha: {} '.format(url)
    return bytes(data, encoding='utf8')


def login(url):
    with open('login.html', mode='rb') as f:
        data = f.read()
        return data


url_list = [
    ('/yingying', yingying),
    ('/alex', alex),
    ('/login', login),

]

while True:
    conn, addr = sk.accept()
    data = conn.recv(9000)
    # 把收到的字节类型的数据转换成字符串
    data_str = str(data, encoding='utf8')
    # 切割字符串，得到请求url
    first_line = data_str.split('\r\n')[0]
    url = first_line.split(' ')[1]
    # print(url)
    # -------------业务逻辑处理部分------------------
    # 使用func变量保存将要执行的函数
    for i in url_list:
        if i[0] == url:
            func = i[1]
            break
    else:
        func = None
    # 执行函数
    if func:
        msg = func(url)
    else:
        msg = b'404 not found!'

    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(msg)
    conn.close()
