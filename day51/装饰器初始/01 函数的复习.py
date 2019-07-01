'''
函数的复习
'''


def func():
    print('哈哈哈')


# func()    函数的调用
print(func)  # 函数的内存地址
# 2. 函数可以像变量一样用来赋值
yingying = func
yingying()


# 3. 函数名可以像普通变量一样放到容器（列表、字典、元组）中
def f1():
    print('f1')


def f2():
    print('f2')


list1 = [f1, f2]
for i in list1:
    i()


# 4.函数可以当成参数传到别的函数中
def f3(arg):
    arg()


f3(func)
print('-------------------------')


# 5. 函数可以作为返回值
def f4():
    def f5():
        print('iphone Xs MAX太贵了！')

    return f5


f4()()
