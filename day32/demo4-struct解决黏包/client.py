import socket
import subprocess
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
while True:
    cmd = sk.recv(1024).decode('utf-8')
    if cmd.upper() == 'Q':
        break
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out = res.stdout.read()
    str_err = res.stderr.read()
    # sk.send(str(len(std_out)+len(str_err)).encode('utf-8'))
    len_num = len(std_out) + len(str_err)
    num_by = struct.pack('i', len_num)
    sk.send(num_by)
    sk.send(std_out)
    sk.send(str_err)
sk.close()

