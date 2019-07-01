# 运行一个py文件的两种方式
# 1. 以模块的方式运行（导入）
# import my_moudle
# if __name__ == '__main__':
#     my_moudle.login()
# 2. 直接右键运行 cmd运行（直接）
# 以脚本的方式运行
# 那么需要在本文件中直接打印的代码上加上
# if __name__ == '__main__'

# 在编写py文件的时候
    # 所有不再函数和类中封装的内容，都应该写在
    # if __name__ == '__main__': 下面
    # 快捷键: main + tab
# sys.modules
# {'sys':文件的内存地址,
# 'my_module': my_module的地址
# '__main__':当前直接执行文件所在的地址}
# 存储了所有导入的文件的名字和这个文件的内存地址

# import sys
# print(sys.modules['__main__'])      #打印当前文件所在的地址
# import my_moudle
# print(__name__)
# print(sys.modules)

# 再使用反射自己模块中的内容的时候
# import sys
# getattr(sys.modules[__name__],变量名)

# print(__name__)

import module2
# print(module2.__name__)
