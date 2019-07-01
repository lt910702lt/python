import os
import sys
#加目录（把client的目录加到sys.path里面）
sys.path.append(os.path.dirname(os.getcwd()))

#导入主程序函数
from core import client
if __name__ == '__main__':
    #执行主程序
    client.main()
