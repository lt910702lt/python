'''
#字符串转换成数字
s = "128"
i = int(s)
print(type(i))  #int

ss = str(i)
print(type(ss)) #str

#综上，想转换成什么，就用什么把目标括起来

#bool类型转为数字，True:1、False:0
b = True
c = int(b)
print(c)    #1

#int类型转为bool，0：False，非0: True
a = 100
print(bool(a))  #True
'''
#空字符串表示False，非空表示True
ss = "哈哈"
if ss:
    print("哈哈")
else:
    print("呵呵")

#真理：空的东西都是False，非空的东西都是True