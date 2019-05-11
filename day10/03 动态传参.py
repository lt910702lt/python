# def chi(good_food, bad_food):
#     print("我要吃", good_food, bad_food)
#
#
# chi("盖饭", "辣条")
# 位置参数 > *动态参数 > 默认值参数


# def chi( *food, a, b): # 可以传入任意的位置参数
#     print("我要吃", food)  # 动态参数接收到的是tuple类型的数据
#
# chi("盖浇饭", "辣条", "面条")
# def func(a, b, c, *args, d = 5):
#     print(a, b, c, d, args)
#
# func(1,2,3)
# func(1,2,3,4,5,6,7, d ="马大哈")

#写函数，给函数传递任意个整数，返回这些数的和
# def func(*n):
#     sum = 0
#     for e in n:
#         sum += e
#     return sum
# print(func(5))

# 动态接收关键字参数
# *位置参数
# **关键字参数
def func(**food):   #** food动态接收关键字参数
    print(food)     #接收到的是字典
func(good_food = "盖浇饭",bad_food="辣条",dirnk="雪碧")
