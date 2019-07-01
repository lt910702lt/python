# 通过一个例子来认识网络编程中一个重要的概念
# 所有客户端执行server端下发指令
# 将结果反馈回来，我来接收

# ret = os.popen()  #运行shell命令，获取执行结果
# import os
# ret = os.popen('dir')
# print(ret.read())

import subprocess

res = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print('stdout:', res.stdout.read().decode('gbk'))
print('stderr:', res.stderr.read().decode('gbk'))
