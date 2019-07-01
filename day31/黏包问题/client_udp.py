import socket
import subprocess

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

sk.sendto('吃了么'.encode('utf-8'), ip_port)
while True:
    cmd, addr = sk.recvfrom(1024)
    ret = subprocess.Popen(cmd.decode('gbk'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out = 'stdout: ' + (ret.stdout.read()).decode('gbk')
    std_err = 'stderr: ' + (ret.stderr.read()).decode('gbk')
    print(std_out)
    print(std_err)
    sk.sendto(std_out.encode('utf-8'),ip_port)
    sk.sendto(std_err.encode('utf-8'),ip_port)
sk.close()