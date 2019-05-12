'''
# isinstance()  判断对象所属类型，包括继承关系
# issubclass()  判断两个类是否为为子类、父类
'''


# class A:pass
# class B(A):pass
# b = B()
# isinstance(b,B) #object,type
# print(isinstance(b,B))      #判断对象是否为后面的type的类型，返回bool
# print(isinstance(b,A))      #True

## type 和isinstance的区别
# type：不包含继承关系，只判断一层
# isinstance：包含所有的继承关系
# == 值相等        值运算
# is 内存地址相等     身份运算
# is 要求更苛刻，不仅要求值相等，还要求内存地址相同
# class Mystr(str): pass
#
#
# ms = Mystr('alex')
# print(ms)
# print(type(ms) is str)  # False
# print(isinstance('alex', str))  # True

##issubclass
class A:pass
class B(A):pass
print(issubclass(A,B))
print(issubclass(B,A))