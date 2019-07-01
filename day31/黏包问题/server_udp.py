import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))
msg, addr = sk.recvfrom(1024)

while True:
    cmd = input('>>>')
    if cmd.upper() == 'Q':
        break
    sk.sendto(cmd.encode('utf-8'), addr)
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
sk.close()

# udp不会黏包，但是会丢包