# class Person:
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def __init__(self, country, name, sex, age, height):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.height = height
#
#     def eat(self):
#         print("%s正在吃饭" % self.name)
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
#
# p1 = Person('中国', 'alex', '未知', 42, 175)
# print(p1.animal)

# 计算一个类，实例化多少对象
# class Count:
#     count = 0
#
#     def __init__(self):
#         Count.count += 1
#
#
# obj1 = Count()
# obj1 = Count()
# obj1 = Count()
# obj1 = Count()
# print(Count.count)

class Count:
    count = 0

    def __init__(self):
        pass
#通过类名可以更改类中的静态变量
# Count.count = 6
# print(Count.__dict__)
#但是通过对象，不能改变只能引用类中的静态变量,因为会在对象空间中添加
obj1 = Count()
# print(obj1.count)
obj1.count = 6
print(obj1.count)
print(Count.__dict__)
print(obj1.__dict__)