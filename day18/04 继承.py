# 面向对象的三大特性: 继承，多态，封装

# # 继承
# class Animal:
#     breath = '会呼吸'
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("进食")
#
#
# class Person(Animal):  # 括号里面的 父类，基类，超类，括号外面的 子类，派生类
#     pass
#
#
# class Cat:
#     pass
#
#
# class Dog:
#     pass
#
#
# # 初始继承：子类以及子类实例化的对象，可以访问父类的任何方法或变量
# # 类名可以访问父类所有的内容
# # print(Person.breath)
# # Person.eat(111)
# # 子类实例化的对象也可以访问父类所有的内容
# p1 = Person('alex', 'ladboy', 1000)
# print(p1.breath)
# p1.eat()


# #  写三个类: 狗,猫,鸡, 每个类中都有 吃 喝  自己的方法  最后定义一个Animal类,
# class Animal:
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self, argv):
#         print("%s 吃 %s" % (self.name, argv))
#
#     def drink(self):
#         print("%s 喝东西" % self.name)
#
#
# class Dog(Animal):
#     def call(self):
#         print("汪汪叫")
#
#
# class Cat(Animal):
#     def call(self):
#         print("喵喵叫")
#
#
# class Bird(Animal):
#     def __init__(self, name, sex, age, wing):
#         # Animal.__init__(self, name, sex, age)
#         super().__init__(name, sex, age)
#         self.wing = wing
#
#     def call(self):
#         print("咕咕叫")
#
#     def eat(self, food):
#         super().eat(food)
#         print("吃虫子")
#
#
# b = Bird('小鸭', '母', 1, '鸡翅膀')
# d = Dog('旺财', '雄', 3)
# c = Cat('猫二娃', '雄', 13)
#
# b.call()
# d.call()
# c.call()
#
# b.drink()
# #d.eat()
# c.drink()
# b.eat('金蚕')
#
# print(b.wing)
# 只执行父类的方法，子类中不要定义与父类同名的方法
# 只执行子类的方法，在子类创建这个方法
# 既要执行子类的方法，又要执行父类的方法，有两种解决方法：
# 1.    def __init__(self, name, sex, age, wing):
#         Animal.__init__(self, name, sex, age) --实际工作中不太会用这种方法，而是用方法2
# 2.    super().__init__(name, sex, age)


# 继承的进阶
# 继承：单继承、多继承

# 类：经点类、新式类
# 新式类：凡是继承object类都是新式类，在python3中所有的类都是新式类
# class A(object):
#     pass

# 经点类：凡是不继承object类都是新式类，python2x(既有新式类，又有经典类)所有的类默认都不继承object类，所有的类默认都是经典类。可以让其继承object类
# class A:
#     pass

# 单继承：新式类、经点类查询顺序一样
# class A:
#     def func(self):
#         print('IN A')
#
#
# class B(A):
#     def func(self):
#         print('IN B')
#
#
# class C(B):
#     pass
#     def func(self):
#         print('IN C')
# c1 = C()
# c1.func()   #IN C。如果C为空，则执行B，如果B也为空，则执行A

# 多继承：
# 多继承-新式类：遵循广度优先
#广度优先：每个节点有且只走一次（沿着一条路往上走，除非有一条路汇合，则走其他路）
class A:
    def func(self):
        print('IN A')


class B(A):
    def func(self):
        print('IN B')


class C(A):
    pass

    def func(self):
        print('IN C')


class D(B):
    pass

    def func(self):
        print('IN D')


class E(C):
    pass

    def func(self):
        print('IN E')


class F(D, E):
    pass

    def func(self):
        print('IN F')

f1 = F()
f1.func()   # F>B>E>C>A
print(F.mro())  #查询广度链路[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# 多继承-经典类：遵循深度优先（python2，了解即可）
# 深度优先：一条路走到底
