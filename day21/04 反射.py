'''
什么是反射？
    答：用字符串数据类型的变量名来访问这个变量的值
反射的方法：
    getattr
    hasattr
    setattr
    delattr

1、类   静态属性  类方法 静态方法
    * getattr(类,'名字')
2、对象
    * getattr(对象,'名字')
3、模块
    * import 模块
    * getattr(模块,'名字')
4、反射自己模块中的内容
    * import sys
    * getattr(sys.modules['__main__'],'名字')
'''


# 引子
# class Student:
#     def __init__(self):pass
#     def check_course(self):
#         print('check_course')
#     def choose_course(self):
#         print('choose_course')
#     def choosed_course(self):
#         print('查看已选的课程')
# stu = Student()
# num = input('>>>')
# if num == 'check_course':
#     stu.check_course()
# elif num == 'choose_course':
#     stu.choose_course()
# elif num == 'choosed_course':
#     stu.choosed_course()

# 类反射
# class Student:
#     ROLE = 'STUDENT'
#
#     @classmethod
#     def check_course(cls):
#         print('查看课程了')
#
#     @staticmethod
#     def login():
#         print('登录')


# # 查看反射属性
# print(Student.ROLE)
# print(getattr(Student, 'ROLE'))
# print(Student.__dict__)
# # 反射调用方法
# print(getattr(Student, 'check_course'))
# getattr(Student, 'check_course')()  # 类方法
# getattr(Student, 'login')()         # 静态方法

# hasattr() 输入的字符串能否在函数的命名空间里面找到
# num = input('>>>')
# # hasattr(Student,num)
# # getattr(Student,num)()
# if hasattr(Student,num):
#     getattr(Student,num)()


# 使用对象去调用反射
# 方法，对象属性
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def func(self):
#         print('in func')
#
#
# a = A('alex')
# print(a.name)
# print(getattr(a, 'name'))
# getattr(a, 'func')()

###setaddr
# class A:
#     def __init__(self,name):
#         self.name = name
# a = A('alex')
# setattr(a,'name','alex_SB')
# print(a.name)

###delattr
# class A:
#     def __init__(self, name):
#         self.name = name
#
#
# a = A('alex')
# print(a.__dict__)
# delattr(a, 'name')
# print(a.__dict__)
