# try/except
# try/except/else
# try/except/else/finally
# try/finally

# 什么是异常，异常和错误的区别
# 异常发生后是什么效果
# 如果查看报错信息
# 最简单的异常处理
# 多分支异常处理
# 异常处理的其他机制
# 自定义异常
# 断言
# 使用异常处理的注意事项
# -----------------------------------------------------------------
# 什么是异常，异常和错误的区别
    # ERROR 错误  比较明显的错误，在编译代码阶段就能检测出来
    # StopIteration 异常  在执行代码的过程中引发的异常

# 异常发生后是什么效果
    # 一旦在程序中发生异常，程序就不再执行了

# 如果查看报错信息
    #

# 最简单的异常处理
# l = ['登陆','登出','退出']
# for i in enumerate(l,1):
#     print(i[0],i[1])
# try:
#     num = int(input('num:'))
#     print(l[num-1])
# except ValueError:
#     print('请输入一个数字')

# # 和else、finally一起使用
# try:
#     a = 1
#     name
#     [][3]
# except NameError:
#     print('name error')
# else:     # try中的代码正常执行，没有异常的时候会执行else中的代码
#     print('执行else了')
# finally:          # 无论任何都会执行，操作系统资源归还工作
#     print('执行finally了')   #

# 多分支异常处理
# l = ['登陆','登出','退出']
# for i in enumerate(l,1):
#     print(i[0],i[1])
# try:
#     num = int(input('num:'))
#     print(l[num-1])
# except ValueError:
#     print('请输入一个数字')
# except IndexError:
#     print('请输入数字0-3')

# 万能异常
# try:
#     name
#     dic = {}
#     dic['key']
# except Exception as e:
#     print(type(e),e,e.__traceback__.tb_lineno)  #<class 'NameError'> name 'name' is not defined 45

# 主动抛异常
# raise TimeoutError
try:
    name = int(input('>>>'))
except ValueError:
    print('在异常出现之前做点什么，然后再抛异常')
    raise  # 抛出原来try的异常，也可以自定义

# 异常处理的其他机制


# 自定义异常
    # 继承Exception类
    # 实现init方法，传一个msg进来
    # 用的时候raise
class LiutError(Exception):
    def __init__(self,msg):
        self.msg = msg
raise LiutError('这是一个什么操作，有什么问题')


# 断言
# 使用异常处理的注意事项
