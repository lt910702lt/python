##内置函数--作用域相关 locals() globals()
# def func():
#     a = 10
#     print("测试数据")
#     print(locals())     #当前作用域的内容
#     print(globals())    #全局作用域的内容
# func()

##内置函数--迭代器/生成器相关 range() next() iter()
# for i in range(20, 5, -3):
#     print(i)

# lst = ["大阳哥", "喜欢", "私密的徒步"]
# it = iter(lst)          # __iter__()
# print(it.__next__())
# print(next(it))     # __next__()

##其他--输入输出input() print()
# print("李嘉诚", "黄花菜", "马云", sep="*", end="大阳哥")  # sep 分隔符，默认为空格" "
# input("提示语")

##内存操作--hash() id()。hash表，用空间换时间，比较耗费内存
# hash算法，目的是唯一性

##模块操作--__import__
# 让用户输入一个要导入的模块
import os

# name = input("请输入你要导入的模块:")
# __import__(name)        #动态导入一个模块

# print(bin(10))      #二进制
# print(oct(10))      #八进制
# print(hex(10))      #十六进制

## callable，判断是否能被调用
# a = 10
# print(callable(a))
# def func():
#     print("马化腾")
# print(callable(func))     #函数是可以被调用的


# s = input("请输入a+b：")
# print(eval(s))  #可以动态的执行代码，代码必须要有返回值

# s = "for i in range(10):print(i)"
# a = exec(s) #exec执行代码不返回任何内容
# print(a)

# exec("""
# def func():
#     print("我是周杰伦")
# func()
# """)

# code1 = "for i in range(10):print(i)"
# com = compile(code1, "", mode="exec")  # compile并不会执行代码，只是编译
# exec(com)  # 执行之后的结果
#
# code2 = "5+6+7"
# com2 = compile(code2, "", mode="eval")
# print(eval(com2))
#
# code3 = "name = input('请输入大阳哥的名字:')"
# com3 = compile(code3, "", mode="exec")
# exec(com3)
# print(name)


# a = -2
# print(abs(a))   #求绝对值

# print(divmod(30, 3))  # 求商和余数，结果为元组

# print(round(4.6))   #五舍六入

# print(pow(10, 3))  # 两个参数，求次幂   1000
# print(pow(10, 2, 3))  # 三个参数，求次幂和余数     1

# print(sum([1, 2, 3, 4, 5, 6]))  #求和

# #lst = ['猴哥', '八戒', '师弟']
# lst = "你好啊"
# it = reversed(lst)  # 不会改变原列表，返回一个迭代器，设计上的一个规则
# print(list(it))

# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst[1:3:1])
# s = slice(1, 3, 1)
# print(lst[s])

# name = "你好，\n我叫%s周润发" % "刘德华"
# print(repr(name))   #原样输出，会过滤到转义字符\t,\r,\n，不管百分号

# print(ord('a'))  # 返回字母a在编码表中的码位  97
# print(ord('中'))  # 20013
#
# print(chr(65))  # 已知码位求字符  A
# print(chr(20013))  # 中

# for i in range(65536):
#     print(chr(i), end=" ")

# print(ascii('a'))   #判断字符是否在ascii表里，存在返回本身
# print(ascii('中'))

# s = "我是中国人"
# a = s.encode("UTF-8")
# print(a)
# print(a.decode("UTF-8"))

# bs = bytes("大阳哥今天很厉害", encoding="utf-8")    #吧字符串转换为byte类型
# print(bs)

# ret = bytearray('alex', encoding='utf-8')
# print(ret[0])
# ret[0] = 65
# print(str(ret))

# s = memoryview("马化腾".encode("UTF-8"))   #查看byte内存，并无卵用
# print(s)    #<memory at 0x00000247D77EC408>