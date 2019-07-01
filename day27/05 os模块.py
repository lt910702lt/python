'''

os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息

os.system("bash command")  运行shell命令，直接显示
os.popen("bash command).read()  运行shell命令，获取执行结果
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd

os.path
os.path.abspath(path) 返回path规范化的绝对路径
os.path.split(path) 将path分割成目录和文件名二元组返回
os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path) 返回path的大小
'''

import os

# print(os.getcwd())  #执行文件时，所在的路径
# print(__file__)     #这个才是获取文件所在的路径！！

# 创建文件夹
# os.mkdir('dir')
# os.makedirs('dir1/dir2',exist_ok=True)

# 删除文件夹
# os.rmdir('dir')   # 没有这个目录会报错，慎用！！！
# os.removedirs('dir1/dir2')  #删空文件夹，如果有其他文件，就停止

# print(os.listdir('D:/学习/05-python/python'))

# os.stat()

# 操作系统的分隔符
# print(os.sep)   # \

# 行终止符
# print([os.linesep]) # windows 为'\r\n'，Linux为'\n'

# 文件路径的分隔符
# print(os.pathsep)   # windows ';' Linux ':' 联系环境变量

# print(os.name)

# os.system('dir')      # 查看路径下的内容，无返回值
# ret = os.popen('dir') # 有返回值
# print(ret.read())

# print([os.path.abspath('D:\学习\05-python\python\day27\01 内容回顾.py')])
print(os.path.split('D:/学习/05-python/python/day27/05 os模块.py'))
print(os.path.dirname('D:/学习/05-python/python/day27/05 os模块.py'))
print(os.path.basename('D:/学习/05-python/python/day27/05 os模块.py'))
print(os.path.exists('D:/学习/05-python/python/day27/05 os模块.py'))
print(os.path.isfile('D:/学习/05-python/python/day27/05 os模块.py'))
print(os.path.isdir('D:/学习/05-python/python/day27/05 os模块.py'))
print(os.path.isdir('D:/学习/05-python/python/day27'))

print(os.path.join('D:\soft\Python37','bbb','ccc'))

print(os.path.getsize(r'D:/学习/05-python/python/day27/05 os模块.py'))

#统计文件夹中所有文件的总的size

# 获取工作路径
print(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))   # 再上一层
