# 负责接收命令，并在本地执行
import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    cmd = sk.recv(1024).decode('gbk')
    if cmd.upper() == 'Q':
        break
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sk.send(res.stdout.read())
    sk.send(res.stderr.read())
sk.close()
