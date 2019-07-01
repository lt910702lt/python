import sys

sys.path
sys.modules
# print(sys.platform)
# sys.exit()  # 结束程序

print(sys.argv)
# 返回的是一个列表，第一个元素是执行这个文件的时候，执行python命令的第一个值，例如：
# python D:/学习/05-python/python/day27/sys模块.py
# 之后的元素，再执行python的启动的时候可以写多个值，都会被依次添加到列表中
# python D:/学习/05-python/python/day27/sys模块.py 123
# python D:/学习/05-python/python/day27/sys模块.py 123 abc

# 有什么用？怎么用？
# name = sys.argv[1]
# pwd = sys.argv[2]
# if name == 'alex' and pwd == '123456':
#     print('登陆成功')
# else:
#     exit()