# 面向对象
    # 你写代码的时候，什么时候用面向对象？
        # 代码量大、功能多的时候
        # 处理比较复杂的角色之间的关系
            # QQ：好友、陌生人、群、组
            # 复杂的电商程序
            # 公司的人事管理系统
        # 我的代码清晰度更高了
            # 可读性
            # 扩展性
            # 复用性
            # 规范性
    # python当中一切皆对象 基础数据类型 都是对象
    # 类型和类的关系   类型和类是一个东西
        # type(obj) obj是一个对象，那么它的type就是它的类型
    # 创建一个对象
        # 类名() 实例化
        # __new__() 创造了一个对象空间，一些简单的初始化
    # 创建一个类
        # class 类名  语法级别的   python解释器读到这句话的时候
        # 类也是被创建出来的，type创建类
        # class A(metaclass=type)
        # type(cls) = type
        # type就是这个类的元类
    # type(obj) 的结果就是这个对象的所属类
    # type(类)的结果就是创建这个类的元类，大多数情况是type，除非你制定metaclass

# 类 class Leiming
    # 类是在什么时候加载的？类名是什么时候生效的？
        #答：1、运行时，直接执行类里面的流程（不会执行方法）；2、加载完以后才会指向Person
    # 静态属性/静态字段/静态变量
    # 动态属性/方法
    # 类里面的方法地址和对象里面的方法地址不一样
        #对象里面的方法地址是类方法地址的一个引用，类似于一个索引
# class Person:
#     ROLE = 'CHINA'
#     print('ROLE')   #打印结果 ROLE
#     def func(self):
#         pass
# a = Person()
# print(Person.func)
# print(a.func)       #这两个值不一样。Person.func是实际的内存地址，而a.func是Person.func地址的一个引用

# 对象
    # 类创造的过程就是实例化的过程：构造new，初始化init
    # 可以通过指针找到类的空间中的内容
    # 对象本身内部也存储了一些只属于对象的属性

# 组合
    # 对象与对象之间: 什么有什么的关系（人有武器、班级有学生）
    # 一个类的对象作为另一个类对象的属性

# 继承
    # 什么是什么的关系（狗是动物）
    # 子类 和 父类
        # 减少代码的重复性（节省代码）
    # 单继承、多继承
        # 单继承:
            # 如果子类的对象调用某个方法
                # 子类有: 调用子类
                    # 子类有，但想调用父类
                        # super: 不用自己传self super(子类,self).方法名(除了self之外的参数)
                        # 父类名: 父类名.方法名(self,...)
                # 子类没有: 找父类
                # 父类没有: 报错
            # 注意: 在任何类中调用的方法，都要自行分辨一下这个self到底是谁的对象
# class Foo:
#     def __init__(self):
#         self.func()
#     def func(self):
#         print('Foo.func')
# class Son(Foo):
#     def func(self):
#         print('Son.func')
# s = Son()   #打印的结果是什么？ ---Son.func
        # 多继承
            # 新式类: 广度优先 - C3算法
                # mro方法查看继承顺序
                #python3 默认继承object 都是新式类
                    # super().func() 遵循mro算法，不用传子类名和self
                #python2 需要主动继承object
                    # super(子类名,self).func() 遵循mro算法，不传子类名会报错
            # 经典类: 深度优先
                # 没有mro
                #python2 不继承object,默认都是经典类
                # super()

    # 经典类、新式类: 是否继承object

    # 抽象类和接口类
        # 不能被实例化
        # 规范子类当中必须实现某个方法
        # 有原生的实现抽象类的方法，但是没有原生实现接口类的方法

        # 了解即可：
            # 抽象类: 抽象类中的方法是可以实现的，只能单继承
            # 接口类: 可以多继承，但是这个类的所有方法都不应该实现
    # java
        # java 只支持类的单继承 抽象类 父类的方法可以实现
        # 接口 interface 支持多继承的规范 接口中的所有方法 只能写pass
    # 抽象类

    # 接口类

# 多态
    # 一种类型的多种形态 多个子类去继承父类，那么每个子类都是父类的一种形态，这就是多态
# class Animal:pass
# class Tiger(Animal):pass
# class Frog(Animal):pass
    # java中多态的应用
        #将不确定的对象，让他们都去继承一个父类，而这个父类什么也不用做，只为保证传参
# def func(Animal tiger_or_frog):
#     tiger_or_frog.eat()

    # 鸭子类型  规范 全凭自觉

# 封装
    # 广义的封装: 把方法和属性都封装在一个类里，定义一个规范来描述一类事物。
    # 狭义的封装: 私有化，只能在类的内部访问
    # __静态变量，私有方法，私有的对象属性，私有的类方法，私有的静态方法
    # 在内存中的存储 __类名__ 名字
    # 为什么在类的内部可以使用双__防范：在类的内部使用，你就知道你在哪个类中
    # 在子类中可以访问父类的私有变量吗？不行
    # 私有: 不能再类的外部使用，也不能被继承


# property  这是一个装饰器、内置函数，帮助你将类中的方法伪装成属性，特性
    # 调用方法的时候不需要主动加括号
    # 让程序的逻辑性更合理
    # @方法名.setter   装饰器，修改被property装饰的属性的时候会调用这个装饰器的方法，除了self之外有一个参数：被修改的值
    # @方法名.deleter  装饰器，当要删除被property装饰的属性的时候会调用这个装饰器的方法--非常不常用
##只用property的示例（最喜欢用的）
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     @property
#     def area(self):
#         return 3.14*self.r**2   #这个方法计算结果本身就是一个属性，但是这个属性会随着这个类/对象的一些基础变量的变化而变化

# 偏其他语言的使用，property私有的 这个时候更多的也会用到setter和deleter
# class A:
#     @property
#     def name(self):
#         return 'alex'
#     @name.deleter
#     def name(self):
#         print('delete name')
# a =  A()
# del a.name      #仅仅是一个语法，类里面的方法并不会真正被删除，感觉类似alias
# print(a.name)

##来制造一个deleter的假象
# class A:
#     def __init__(self,name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name
#
#     @name.deleter
#     def name(self):
#         del self.__name
# a = A('alex')
# print(a.name)
# del a.name
# print(a.name)

# classmethod   类方法的装饰器 内置函数
    # 使用类名调用，默认传类名作为第一个参数
    # 不用对象命名空间的内容，而用到了类命名空间中的变量（静态属性），或者类方法和静态方法

#商场的程序
# class Goods:
#     __diccount = 0.8
#     def __init__(self,price):
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price * Goods.__diccount
#     @classmethod
#     def change__discount(cls,num):
#         cls.__diccount = num
#
# apple = Goods(10)
# banana = Goods(15)
# print(apple.price,banana.price)
# Goods.change__discount(1)
# print(apple.price,banana.price)

# staticmethod（不知道，可以略吧）
    # 如果一个类里面的方法，既不需要用到self中的资源，也不用cls中的资源
    # 相当于一个普通的函数
    # 但是由于某种原因，还要把这个方法放在类中，这个时候，就将这个方法变成一个静态方法
    # 某种原因：
        # 你完全想用面向对象编程，所有的函数都必须写到类里
        # 某个功能确确实实是这个类的方法，但是确确实实没有用到和这个类有关系的资源

# 抽象类和接口类

# 反射
    # 从某个指定的命名空间中，用字符串类型的变量名来获取变量的值
    # 类名反射：可以反射静态属性、类方法、静态方法
    # 对象反射：可以反射对象属性、方法
    # 模块：模块中的方法
    # 自己模块中
# import sys
# mymodule = sys.modules['__main__']
# getattr(mymodule,'变量名')

# hasattr/getattr/setattr/delattr
# 参数
    #(命名空间,'变量名')
    #setattr(命名空间,'变量名','新的值')
# 变量名 你只能拿到一个字符串的版本
    # 从文件里拿
    # 交互拿：input/网络传输


# 进阶
    # 内置方法/魔术方法/双下方法
    # __名字__不是被直接调用的
    # 间接调用：内置函数触发/面向对象特殊语法/python是提供的语法糖
    # __str__：str(obj)，要求必须实现了__str__，要求这个方法的返回值必须是字符串str类型
        #print %s str
    # __call__： 对象() 用类写装饰器
    # __len__：len()，要求obj必须实现__len__，要求这个函数的返回值必须是数字int型
    # __new__：在实例化的过程中，最先执行的方法，在init之前，用来创造一个对象，构造方法
        # 单例类
    # __init__：在实例化的过程中，在new执行之后，自动触发一个初始化方法

#一个加法的语法糖
# x = 5
# y = 6
# print(x.__add__(y))
# class MyType:
#     def __init__(self,str):
#         self.str = str
#     def __add__(self, other):
#         return self.str.count('*') + other.str.count('*')
# obj1 = MyType('sd***sdadas**')
# obj2 = MyType('sd***sdadas*')
# print(obj1.__add__(obj2))   #打印结果是9