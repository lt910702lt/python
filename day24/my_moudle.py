__all__ = ['name','login']  #控制 * 导入的内容

name = 'alex'

def login():
    print('login',name)

import sys
print(__name__)
print('****',sys.modules['__main__'])
print(sys.modules)
# name = 'egon'

if __name__ == '__main__':
    print('饿了么')
    print(__name__,type(__name__))