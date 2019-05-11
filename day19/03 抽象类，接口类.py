# python 没有接口这个概念，因此抽象类和接口类是一回事
# 接口类，抽象类：制定一个规范

# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用支付宝支付了%s' % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用京东支付了%s' % self.money)
#
#
# a1 = Alipay(200)
# a1.pay()
#
# b1 = Jdpay(100)
# b1.pay()

# 第二版
# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用支付宝支付了%s' % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用京东支付了%s' % self.money)
#
#
# def pay(obj):
#     obj.pay()
#
#
# a1 = Alipay(200)
# j1 = Jdpay(100)
# pay(a1)  # 归一化接口设计
# pay(j1)

# 第三版，野生程序员来了，要增加一个微信支付功能
# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用支付宝支付了%s' % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print('使用京东支付了%s' % self.money)
#
#
# class Wechatpay:
#     def __init__(self, money):
#         self.money = money
#
#     def weixinpay(self):
#         print('使用微信支付了%s' % self.money)
#
# def pay(obj):
#     obj.pay()
#
# w1 = Wechatpay(300)
# w1.weixinpay()

# 第四版，发回去重新改，制定规则，抽象类、接口类
# 抽象类（接口类）,所有的子类里面都必须包含有pay方法，否则实例化对象的时候就会报错！
# 让子类强制执行接口类，需要使用一个abc方法

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):  # 接口类。强制制定一个规范。
    @abstractmethod
    def pay(self):
        pass


class Alipay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('使用支付宝支付了%s' % self.money)


class Jdpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('使用京东支付了%s' % self.money)


class Wechatpay(Payment):
    def __init__(self, money):
        self.money = money

    def weixinpay(self):
        print('使用微信支付了%s' % self.money)


a1 = Alipay(200)
#w1 = Wechatpay(100)
