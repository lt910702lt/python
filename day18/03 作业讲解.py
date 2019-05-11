'''
day15天作业及默写
1，暴力摩托程序（完成下列需求）：
1.1
创建三个游戏人物，分别是：
•    苍井井，女，18，攻击力ad为20，血量200
•    东尼木木，男，20，攻击力ad为30，血量150
•    波多多，女，19，攻击力ad为50，血量80
1.2
创建三个游戏武器，分别是：
•    平底锅，ad为20
•    斧子，ad为50
•    双节棍，ad为65

1.3
创建三个游戏摩托车，分别是：

•    小踏板，速度60迈
•    雅马哈，速度80迈
•    宝马，速度120迈。

完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：

（1）苍井井骑着小踏板开着60迈的车行驶在赛道上。
（2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
（3）波多多骑着雅马哈开着80迈的车行驶在赛道上。


（4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
（5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。

（6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
（7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。


（8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。
（9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。
'''


# 第一题：暴力摩托
# 定义一个游戏角色类，初始化姓名，性别，年龄，攻击力，血量
# class Game_Role:
#
#     def __init__(self, name, sex, age, ad, hp):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.ad = ad
#         self.hp = hp
#
#     def arms(self, a):
#         self.a = a
#
#     def drive(self, m):
#         self.m = m
#         print('%s 骑着 %s 开着 %s 迈的车行驶在赛道上' % (self.name, m.name, m.speed))
#
#     # 空手打人
#     def attach(self, p):
#         self.p = p
#         p.hp = p.hp - self.ad
#         print('%s 赤手空拳打了 %s %s滴血，%s还剩 %s 血' % (self.name, p.name, self.ad, p.name, p.hp))
#
#     # 带武器打人
#     def fight(self, w, p):
#         self.w = w
#         self.p = p
#         p.hp = p.hp - (self.ad + w.ad)
#         print('%s 利用 %s 打了 %s 一 %s, %s 还剩 %s 血。' % (self.name, w.name, p.name, w.name, p.name, p.hp))
#
#
# # 定义一个武器类，初始化武器名，攻击力
# class Arms:
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#
# # 定义一个摩托车类,初始化摩托车名，速度
# class Motorcycle:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#
# # 创建三个人物
# p1 = Game_Role('苍井空', '女', 18, 20, 200)
# p2 = Game_Role('东尼木木', '男', 20, 30, 150)
# p3 = Game_Role('波多多', '女', 19, 50, 80)
#
# # 创建三个武器
# a1 = Arms('平底锅', 20)
# a2 = Arms('斧子', 50)
# a3 = Arms('双截棍', 65)
#
# # 创建三个摩托车
# m1 = Motorcycle('小踏板', 60)
# m2 = Motorcycle('雅马哈', 80)
# m3 = Motorcycle('宝马', 120)
#
# # p1.drive(m1)
# # p2.drive(m3)
# # p3.drive(m2)
# #
# # p1.attach(p2)
# # p2.attach(p1)
#
# p3.fight(a1, p1)
# p3.fight(a2, p2)

# # 2. 定义一个圆，计算周长和面积
# from math import pi
#
#
# class Cricle:
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return round(self.r ** 2 * pi, 2)
#
#     def perimeter(self):
#         return round(self.r * 2 * pi, 2)
#
#
# c1 = Cricle(3)
# print(c1.area())
# print(c1.perimeter())


# 3，定义一个圆环类，计算圆环的周长和面积（升级题）。
from math import pi
class Ring:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def area(self):
        return round(self.r1 ** 2 * pi - self.r2 ** 2 * pi, 2)

    def perimeter(self):
        return round(self.r1 * 2 * pi + self.r2 * 2 * pi, 2)


r1 = Ring(5, 3)
print(r1.area())
print(r1.perimeter())
