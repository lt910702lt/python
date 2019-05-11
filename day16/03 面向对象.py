# s1 = 'fdsajkf'
# count = 0
# for i in s1:
#     count += 1
# print(count)
#
# l1 = [1, 2, 3]
# count = 0
# for i in l1:
#     count += 1
# print(count)
#
#
# def my_len(argv):
#     count = 0
#     for i in argv:
#         count += 1
#     return count

# 文件：1,'alex','未知',13666666666,IT
# 1,'alex','未知',1356666666,IT

# def add(name,sex,phone,job):
#     '''100行代码,'''
#     pass
#
# def remove(name,sex,phone,job):
#     '''100行代码,'''
#     pass
#
# def update(name,sex,phone,job):
#     '''100行代码,'''
#     pass
#
# def find(name,sex,phone,job):
#     '''100行代码,'''
#     pass
# add('alex','未知',1356666666,'IT')
# remove('alex','未知',1356666666,'IT')

# class file:
#     def __init__(self,name,sex,phone,job):
#         self.name = name
#         self.sex = sex
#         self.phone = phone
#         self.job = job
#
#     def add(self):
#         '''100行代码,'''
#         pass
#
#     def remove(self):
#         '''100行代码,'''
#         pass
#
#     def update(self):
#         '''100行代码,'''
#         pass
#
#     def find(self):
#         '''100行代码,'''
#         pass
# f1 = file('alex','未知',1356666666,'IT')
# f1.add()
# f1.remove()

# 类: 具有相同属性和技能的一类事物
# 人类:
# 对象: 具体的类的表现.具体的实实在在的一个实例
# 人是一类，刘德华是一个对象
# 狗是一类，旺财是一个对象

# 建类的时候，首字母大写
# class Persion:
#     '''类体：两部分：变量部分，方法(函数)部分'''
#     mind = '有思想'  # 变量，静态变量，静态字段
#     animal = '高级动物'
#     faith = '有信仰'
#
#     def __init__(self):
#         print(self)
#         print(666)
#
#     # def __init__(self,name,age,sex,hobby):
#     #     print(666)
#
#     def work(self):  #方法，函数，动态变量
#         print('人类都会工作')
#
#     def shopp(self):
#         print('人类都会消费')

# 类名的角度
# 类中的静态变量
# 方法1：Persion.__dict__查询类中的所有内容，无法进行增、删、改操作
# print(Persion.__dict__)
# print(Persion.__dict__['faith'])
# Persion.__dict__['mind'] = '无脑'     #报错，无法进行增、删、改操作
# print(Persion.__dict__['mind'])

# 方法2：万能的 . 对类中的单个的变量进行增删改查
# print(Persion.mind)
# print(Persion.animal)       #查
# Persion.money = '运用货币'  #增
# Persion.mind = '无脑的'     #改
# del Persion.mind            #删
# print(Persion.__dict__)

# 操作类中的方法，（工作中基本不用）
# Persion.work(111)


class Persion:
    '''类体：两部分：变量部分，方法(函数)部分'''
    mind = '有思想'  # 变量，静态变量，静态字段
    animal = '高级动物'
    faith = '有信仰'

    def __init__(self, name, age, hobby):
        self.name = name  # 相当于给对象增加了一个变量
        self.age = age
        self.hobby = hobby

    def work(self):  # 方法，函数，动态变量
        print('%s都会工作' % self.name)

    def shopp(self):
        print(self)
        print('人类都会消费')


ret = Persion('alex', 1000, 'oldwomen')  # 类名+() 的这个过程：实例化的过程（创建对象的过程），实例化对象，实例，对象
# print(ret.__dict__)
# 1. 类名+() 产生一个对象(实例，对象空间)
# 2. 自动执行类中的__init__方法，并将对象空间传给__init__的self参数
# 3. 给对象封装相应的属性


# 对象的角度
# 操作对象中的静态变量
# 1. __dict__ 查询对象中所有的内容
# 2. 万能的 .
# print(ret.name)     #查询
# ret.high = 175      #增加
# del ret.name        #删除
# ret.age = 73        #修改
# print(ret.__dict__)
# 操对象作类中的静态变量，只能查询
# print(ret.mind)

# 对象调用类中的方法(工作中通过对象执行类中的方法，而不是通过类名)
ret.shopp()

bigsum = Persion('大阳哥', 39, '非男')
india_ning = Persion('印度阿宁', 19, '女')
bigsum.work()
india_ning.work()