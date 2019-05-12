'''
类方法：
    通过类名调用的方法，类方法中第一个参数约定俗称cls，python自动将类名（类空间）传给cls
    对象也可以调用
    应用场景：
        1、类中有些方法是不需要传入对象，不要对象的一切东西
        2、对类中的静态变量进行改变，要用类方法
        3、继承中，父类得到子类的空间
静态方法：
    1、代码块
    2、复用性
'''


# 类方法
# class A:
#     def func(self):     # 普通方法
#         print(self)
#
#     @classmethod
#     def func1(cls):     # 类方法
#         print(cls)
#
# a1 = A()
# # a1.func1()   #打印出a1的地址
# # a1.func()
# # A.func(a1)
#
# A.func1()       #类直接调用类方法，不需要传参数，默认为cls，值为类空间值
# a1.func1()

# 2、对类中的静态变量进行改变，要用类方法
# class A:
#     name = 'alex'
#     count = 1
#
#     @classmethod
#     def func(cls):
#         return cls.name + str(cls.count)
# a1 = A
# print(a1.func())

# 3、继承中，父类得到子类的空间
# class A:
#     name = 'alex'
#     count = 1
#     age = 12
#
#     @classmethod
#     def func1(cls):
#         print(cls)
#         #对B类的所有内容进行修改
#         print(cls.age)
#
#
# class B(A):
#     age = 22
#
#
# B.func1()       #子类通过类名去执行父类的一个方法，并且将子类的空间传递给父类 <class '__main__.B'>

##不通过类方法，想让父类的某个方法得到子类空间里面的任意值
# class A:
#     age = 12
#
#     def func(self):
#         print(self.age)  # self子类的对象，能得到子类空间的任意值
#
#
# class B(A):
#     age = 22
#
#
# b1 = B()
# b1.func()

# 静态方法(几乎不太用)
class A:

    @staticmethod
    def func():
        print(666)
A.func()    #静态方法的所有内容都加载在类空间，因此必须使用类来调用
