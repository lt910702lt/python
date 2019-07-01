import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8080))
while True:
    info = input('>>>')
    if info == 'bye':
        sk.send(bytes('bye',encoding='utf-8'))
        break
    sk.send(bytes(info,encoding='utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    if ret == 'bye':
        break
    print(ret)
sk.close()
