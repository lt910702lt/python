'''
#__名字__
    * 类中的特殊方法
    * 双下方法
    * 魔术方法 magic method
# 类中的每一个双下方法都有它自己的特殊意义


# __call__  相当于 对象()
# __new__   特别重要，开辟内存空间，类的构造方法(写一个单例类)
# __len__   len(obj)
# __str__   str(obj) '%s' % obj,print(obj)
# __repr__

#所有的双下方法，没有需要你在外部直接调用的
#而是总有一些

'''
# class A:
#     def __call__(self, *args, **kwargs):
#         print('执行call方法了')
# class B:
#     def __init__(self,cls):
#         self.a = cls()
#         self.a()
# a = A()
# # a()     #相当于调用__call__方法
# # A()()   #和上面结果一样，先实例化得到一个对象，再对对象(),相当于调用__call__方法
#
# B(A)

###__len__
# 内置函数和类的内置方法是相关的len()、__len__()
# len(dict)
# len(typle) str list set
# __iter__
# __next__
# iter(obj)
# next
# class Mylist:
#     def __init__(self):
#         self.lst = [1,2,3,4,5,6]
#         self.name = 'alex'
#         self.age = 83
#     def __len__(self):
#         print('执行__len__了')
#         return len(self.__dict__)
# lst = Mylist()
# print(len(lst))
# len(obj)相当于调用了这个obj的__len__方法
# __len__方法return的值就是len函数的返回值
# 如果一个obj对象没有__len__方法，那么len函数会报错
# #练习实现：类 self.s = '' 类的长度就是str的长度
# class Str:
#     def __init__(self,s):
#         self.s = s
#     def __len__(self):
#         return len(self.s)
# s = Str('abc')
# print(len(s))

### __new__  #==> 构造方法
### __init__ #==> 初始化方法
# class Single:
#     def __new__(cls, *args, **kwargs):
#         print('在new方法里')
#         return object.__new__(cls)
#
#     def __init__(self):
#         print('在init方法里')
# 1.开辟一个内存空间，属于对象
# 2.把对象的空间传给self，执行init
# 3.将这个对象空间返回给调用者
# obj = Single()


#单例
#如果一个类 从头到尾只能有一个实例，那么这个类就是一个实例类
#单例类
# class Single:
#     __isinstance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__isinstance:
#             cls.__isinstance = object.__new__(cls)
#         return cls.__isinstance
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = Single('alex',10)
# s2 = Single('taibai',100)
# print(s1.name)
# print(s2.name)
# print(s1,s2)        #空间地址值是一样的

### __str__
#打印对象的时候，输出__str__定义的内容
# l = [1,2,3]
# print(l)
class Student:
    def __str__(self):
        return '姓名：%s ,年龄：%s ,性别： %s' % (self.name,self.age,self.sex)
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
a = Student('hezewei',18,'男')
print(a)