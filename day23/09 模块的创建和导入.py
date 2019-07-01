import my_moudle    #要导入一个py文件夹的名字，但是不加.py后缀
# 一般情况下，模块都是小写字母开头的名字
# import my_moudle
# import语句相当于什么呢？？
# import这个模块相当于执行了这个模块所在的py文件

# 模块可以被多次导入么？？
    # 一个模块不会被重复导入
# my_moudle.login()
# print(my_moudle.name)

# 在导入一个模块的过程中，到底发生了哪些事情
    # 1.找到这个my_moudle模块
    # 2.创建一个属于my_moudle的内存空间
    # 3.执行my_moudle
    # 4.将这个模块所在的命名空间建立一个和my_moudle之间的引用关系

# 模块的重命名
import my_moudle as m   #重命名之后，就不能再用原来的名字进行引用了
print(m.name)

# 导入多个模块
import os,sys

# python开发规范PEP8要求不允许放在一行导入
# 并且所有的模块都应该放在文件开头
# 先导入内置模块，再导入三方模块，最后导入自定义模块