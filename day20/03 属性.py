# 什么是属性？properties
# 如果配置一个properties：在class方法上面添加@properties
# 调用区别：
#   方法：p1.mbi()
#   属性：p1.mbi
# 作用：
#   * 将一个方法伪装成一个属性，在代码的级别上没有本质的提升，但是让其看起来更合理
'''
例一：BMI指数（bmi）是计算类，但很明显它听起来像是一个属性而非方法，如果将其做成一个属性，更便于理解
承认的BMI值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖：高于32
    体质指数（BMI）=体重（kg）* 身高^2(m)
    EX：70（kg）%（1.75*1.75）= 22.86
'''


# class Bmi:
#     def __init__(self,weight,height):
#         self.weight = weight
#         self.height = height
#
#     def mbi(self):
#         mbi = self.weight / (self.height**2)
#         print(mbi)
#         if mbi < 18.5:
#             print("过轻")
#         elif 18.5 <= mbi <23.9:
#             print("正常")
#         elif 24 <= mbi < 27:
#             print("过重")
#         elif 28 <= mbi < 32:
#             print("肥胖")
#         else:
#             print("非常肥胖")
#         return mbi
# p1 = Bmi(75,1.78)
# p1.mbi()
# class Person:
#     def __init__(self, name, height, weight):
#         self.name = name
#         self.__height = height
#         self.__weight = weight
#
#     @property       #属性
#     def bmi(self):
#         return '%s 的bmi值为：%s' % (self.name, self.__weight / self.__height ** 2)
#
#
# p1 = Person('涛帅', 1.78, 78)
# # print(p1.bmi())
# # print(p1.bmi)
#
# p1.name = 'alex'
# print(p1.name)
# # p1.bmi = 'alex'       #错误，不能去修改属性的值AttributeError: can't set attribute
# # print(p1.bmi)

##属性的更改
class Person:
    def __init__(self, name, age):
        self.name = name
        if type(age) is int:
            self.__age = age
        else:
            print("你输入的参数有误，请重新输入")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,a1):
        if type(a1) is int:
            self.__age = a1
        else:
            print("你输入的参数有误，请重新输入")

    @age.deleter
    def age(self):
        print(666)

p1 = Person('帅哥', 18)
p1.age = 20
print(p1.age)
del p1.age
# properties: 类似于bmi，area，周长....  ***
# age.setter    **
# age.deleter   *
# 都是通过指定来触发函数

