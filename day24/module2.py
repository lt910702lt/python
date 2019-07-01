import sys
print(__name__)
print(sys.modules['__main__'])  #获取当前文件的内存地址
print(sys.modules[__name__])    #如果想要当作脚本来被引用，那么就要用__name__来使用

def func():
    print('aaa')

# getattr(sys.modules['__main__'],'func')()
getattr(sys.modules[__name__],'func')()