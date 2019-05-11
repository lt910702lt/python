class Person:
    animal = '高级动物'
    soul = '有灵魂'
    language = '语言'

    def __init__(self, country, name, sex, age, height):
        self.country = country
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height

    def eat(self):
        print('吃饭')

    def work(self):
        print('工作')

    def sleep(self):
        print('睡觉')


p1 = Person('菲律宾', 'alex', '未知', 42, 175)
print(p1.animal)


# class A:
#     def func(self):
#         print('in A')
#
#     def use(self, new):
#         self.new = new
#
#
# class B:
#     def func1(self):
#         print('in B')
#
#
# a1 = A()
# b1 = B()
# a1.use(b1)
# a1.new.func1()
