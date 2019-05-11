# 老师博客地址：https://www.cnblogs.com/jin-xin/articles/9157737.html
# 广义的封装：实例化一个对象，给对象空间封装一些属性
# 狭义的封装：私有制
# 私有成员：私有静态字段，私有动态方法，私有对象属性

#### 私有静态字段
class B:
    __money = 100000


class A(B):
    name = 'alex'
    __age = 1000  # 私有静态字段

    def func(self):
        print(self.__age)
        print(A.__age)  # 对于私有静态字段，在类的内部可以访问
        print('func...')

    def func1(self):
        print(self.__money)
        print(A.__money)


# a1 = A()
# print(a1.name)
# a1.func()
# print(a1.__age)  #私有静态字段，无法通过对象调用
# print(A.__age)    #类名也无法访问
# 对于私有静态字段，在类的外部无法访问
# a1.func()
# 对于私有静态字段，在类的内部可以访问
# a1.func1()  #报错，子类也无法访问到

# 总结：对于私有静态来说，只能在本类中内部访问，外部的类，派生类均不可访问

# __money私有静态字段，其实是在__money前面加了'_类名',结果是_B__money
# 骚操作：可以通过_B__money来访问（千万不要这么做）


###私有方法
# class B:
#     __money = 100000
#
#     def __f1(self):
#         print('B')
#
#
# class A(B):
#     name = 'alex'
#
#     def __func(self):
#         print('func...')
#
#     def func1(self):
#         self.__func()
#         self.__f1()
#
#
# a1 = A()
# # a1.__func() #类外部不能访问
#
# a1.func1()  # 类的内部可以访问


# a1.func1()  #类的派生类也无法访问

# 面试题
class Parent:
    def __func(self):
        print('in Parent func')

    def __init__(self):
        self.__func()


class Son(Parent):
    def __func(self):
        print('in Son func')


s1 = Son()
