#闭包特点1：可以让变量常驻内存
# def func():
#     name = "alex"
#     def inner():
#         print(name)     #闭包：内层函数对外层函数的一个引用，可以让一个局部变量常驻内存
#     return inner
# ret = func()
# ret()
# ret()
# ret()

# 2. 防止其他程序改变变量
# def func():
#     name = "alex"
#     def inner():
#         print("name")
#     def inner2():
#         nonlocal name
#         name = "wusir"
#     return inner
# ret = func


# 闭包的好处
from urllib.request import urlopen
def but():
    content = urlopen("http://www.h3c.com/cn/").read()
    def inner():
        #print("你好啊")
         return content # 在函数内部使用了外部的变量 . 闭包
    print(inner.__closure__)    # 查看inner是否是闭包, 如果有东西就是闭包, 没东西就不是闭包
    return inner
print("加载中........")
fn = but()  # 这个时候就开始加载校花100 的内容
# 后⾯需要⽤到这⾥⾯的内容就不需要在执⾏⾮常耗时的⽹络连接操作了
content = fn()   # 获取内容
print(content)
content2 = fn()  # 重新获取内容
print(content2)
