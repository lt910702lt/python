# from my_moudle import login
# 不是python解释器发现的错误，而是pycharm根据它的一些判断而得出的结论

# from import 的时候发生了什么？
    # 仍然相当于执行了整个py文件
    # 1.找到my_moudle模块
    # 2.开辟一块属于这个模块的命名空间
    # 3.执行这个模块
    # 4.只带了要import的是login这个名字，那么就会在本文建中创建一个login变量，指向模块命名空间的login函数

# 在from import的时候命名空间的变换
# login()
# 导入了什么，就能使用什么，不导入的变量，不能使用
# 不导入并不意味着不存，而是没有建立文件到模块中其他名字的引用
# def login():
#     print('in my login')
# login()
# 当模块中导入的方法或者变量 和 本文件重命名的时候，那么这个名字只代表最后一次对它复制的那个方法或者变量
# name = '太亮'
# login()
# 在本文件中对全局变量的修改，是完全不影响模块中的变量引用的

# 重命名
# from my_moudle import login as l
# l()

# 导入多个模块
# from my_moudle import login,name
# login()
# print(name)
# name = '太亮'
# login()

# 导入多个再重命名
# from my_moudle import login as l,name as n

# from 模块 import *
# from my_moudle import *

# __all__ 可以控制*导入的内容
# from my_moudle import *
# login()
# print(name)
print('xxx')