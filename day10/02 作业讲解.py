# 1. 整理函数相关的知识点,写博客

# 2. 写函数,检查获取传入列表活元组对象的所有奇数位索引对应的元素,并将其作为新列表返回给调用者
# def rel(ls):
#     lst = []
#     for i in range(len(ls)):
#         if i % 2 == 1:
#             lst.append(ls[i])
#     return lst
#
#
# lst = ['a', "b", "c", "d", "e", "f"]
# print(rel(lst))

# 3. 写函数,判断用户传入的对象(字符串,列表,元组)长度是否大于5
# def length(s):
#     if len(s) > 5:
#         return True
#     else:
#         return False
#
#
# s = "12345678"
# s1 = "1234"
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# lst1 = [1, 2, 3, 4]
# print(length(s), length(s1), length(lst), length(lst1))

# 4. 写函数,检查传入列表的长度,如果大于2,将列表的前两项内容返回给调用者
# def fun(list):
#     if len(list) > 2:
#         return list[:2]
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# print(fun(lst))

# 5. 写函数,计算传入函数的字符串中,数字,字母,空格以及其他内容的个数,并返回结果
# def func(s=""):
#     shuzi = 0
#     zimu = 0
#     kongge = 0
#     qita = 0
#     for c in s:         #循环字符串,拿到每个字符
#         if c.isdigit():
#             shuzi += 1
#         elif c.isalpha():
#             zimu += 1
#         elif c == " ":
#             kongge += 1
#         else:
#             qita += 1
#     return shuzi, zimu, kongge, qita
#
# s = "123 45 67 as df vg@@"
# print(func(s))

# 6. 写函数,接收两个数字参数,返回比较大的那个数字
# def func(n1, n2):
#     if n1 > n2:       # c = a if a>b else b
#         return n1
#     else:
#         return n2
#
#
# print(func(3, -4))

# 7. 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 	dic = {"k1":"v1", "k2":[11,22,33,44]}
# 	dic = {"k1":"v1", "k2":[11,22]}
# 	PS:字典中的value只能是字符串或列表
# dic = {"k1": "v1", "k2": [11, 22, 33, 44]}
# def func(dic={}):
#     dic_new = {}
#     for k, v in dic.items():
#         if len(v) > 2:
#             dic_new[k] = v[0:2]
#         else:
#             dic_new[k] = v
#     return dic_new
# print(func(dic))

# 8. 写函数,接列表,返回字典,字典对应的内容为列表的index:value
# lst = ['a', 'b', 'c']
#
#
# def func(lst=[]):
#     dic = {}
#     for n in range(len(lst)):
#         dic[n] = lst[n]
#     return dic
#
#
# print(func(lst))

# 9. 写函数,接收四个参数:姓名,性别,年龄,学历,并追加到student_msg文件中

# 我的程序
# def func(name, age, sex, edu):
#     with open("student_msg", mode="a", encoding="utf-8") as f:
#         f.write(name+"_"+age+"_"+sex+"_"+edu)
# func("张三","18","女","中专")

# 老师的程序
# def func(name, age,edu,sex ="男"):
#     f = open("student.msg", mode="a", encoding="utf-8")
#     f.write(name+"_"+str(age)+"_"+sex+"_"+edu+"\n")
#     f.flush()
#     f.close()
#
#
# while 1:
#     content = input("请问. 是否要录入学生信息, 输入q退出:")
#     if content.upper() == "Q":
#         break
#     n = input("请输入名字:")
#     a = input("请输入年龄:")
#     s = input("请输入性别:")
#     e = input("请输入学历:")
#     if s == "":
#         func(n,a,e)
#     else:
#         func(n,a,e,s)

# 10. 写函数,用户传入修改文件名,和要修改的内容,执行函数,完成整个文件的批量操作
# import os
#
#
# def func(filename, old, new):
#     with open(filename, mode="r", encoding="utf-8") as f1, \
#             open(filename + "_副本", mode="w", encoding="utf-8") as f2:
#         for line in f1:
#             s = line.replace(old, new)
#             f2.write(s)
#     os.remove(filename)
#     os.rename(filename + "_副本", filename)
#
#
# func("student_msg", "中", "大")
