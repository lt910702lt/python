# python面向对象三大特征之一:
# 多态：python处处是多态

# python不管什么类型，传入函数，封装到对象中都可以

# python没有多态？他有什么？他有鸭子类型
# 鸭子类型：看着像鸭子，它就是鸭子

# 具有相同方法的类(例如下面的类都有init方法)，他们互相称之为鸭子
# 统一化设计的思想
class Str:
    def init(self):
        pass


class List:
    def init(self):
        pass


class Tuple:
    def init(self):
        pass
