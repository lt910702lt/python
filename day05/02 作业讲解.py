#######第一题：写代码，有如下列表，按照要求实现每一个功能
#li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# # 1）、计算列表的长度并输出
# print(len(li))

# # 2）、列表中追加元素“seven”,并输出添加后的列表
# li.append("seven")
# print(li)

# # 3）、请在列表的第一个位置插入元素“Tony”，并输出添加后的列表
# li.insert(0, "Tony")
# print(li)

# # 4）、请修改列表的第2个位置的元素为“Kelly”,并输出修改后的列表
# li[1] = li[1].replace("alex", "Kelly")
# print(li)

# # 5）、请将列表l2 = [1, "a", 3, 4, "heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加
# l2 = [1, "a", 3, 4, "heart"]
# li.extend(l2)
# print(li)

# # 6）、请将字符串s = "qwert" 的每个元素添加到列表li中，一行代码实现，不允许循环添加
# s = "qwert"
# li.extend(s)
# print(li)

# # 7）、请删除列表中的元素“alex”，并输出删除后的列表
# li.remove("alex")
# print(li)

# # 8）、请删除列表中的第二个元素，并输出删除的元素和删除元素后的列表
# e = li.pop(1)
# print(e)
# print(li)

# # 9）、请删除列表中的第2至第4个元素，并输出删除后的列表
# del li[1:4]
# print(li)

# # 10）、请将列表所有的元素反转，并输出反转后的列表
# li.reverse()
# print(li)

# # 11）、请计算出“alex”元素在列表中出现的次数，并输出该次数
# print(li.count("alex"))


# ######第二题：写代码，有如下列表，利用切片实现每一个功能
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# # 1）、通过对li列表切片形成新的列表l1,l1 = [1, 3, 2]
# print(li[:3])
# # 2）、通过对li列表切片形成新的列表l2,l2 = ["a", 4，"b"]
# print(li[3:6])
# # 3）、通过对li列表切片形成新的列表l3,l3 = [1, 2, 4, 5]
# print(li[::2])
# # 4）、通过对li列表切片形成新的列表l4,l4 = [3, 'a', 'b']
# print(li[1:6:2])
# # 5）、通过对li列表切片形成新的列表l5,l5 = ['c']
# print(li[-1:-2:-1])
# # 6）、通过对li列表切片形成新的列表l6,l6 = ["b", "a", 3]
# print(li[-3::-2])

# ######第三题：有如下列表，按照要求实现每一个功能
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# # 1）、将列表中的"tt"变成大写(用两种方式)
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# lis[3][2][1][0] = lis[3][2][1][0].replace('t', 'T')
# lis[3][2][1][0] = "TT"
#
# # 2）、将列表中的数字3变成字符串"100"(用两种方式)
# lis[3][2][1][1] = "100"
# lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
#
# # 3）、将列表中的字符串"1"变成数字101（用两种方式）
# lis[3][2][1][2] = 101
# lis[3][2][1][2] = int(lis[3][2][1][2] + "01")

# ######第四题：请用代码实现
# li = ["alex", "eric", "rain"]
# #利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# s = ""
# for el in li:
#     s = s + el + "_"
# print(s[:len(s)-1])

# ######第五题：利用for循环和range打印出下面列表的索引 ***
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou", ""]
# for i in range(len(li)):
#     print(i)

######第六题：利用for循环和range找出100以内所有的偶数，并将这些偶数插入到一个新的列表中
# li = []
# for n in range(100):
#     if n % 2 == 0:
#         li.append(n)
# print(li)

######第七题：利用for循环和range找出50以内能被3整除的数，并将这些偶数插入到一个新的列表中。
# li = []
# for n in range(50):
#     if n % 3 == 0:
#         li.append(n)
# print(li)

# ######第八题：利用for循环和rang从100~1,倒叙打印
# for n in range(100, 0, -1):
#     print(n)

######第九题：利用for循环和rang从100~10，倒叙将所有的偶数添加到一个新的列表中，然后对列表的元素进行筛选，将能被4整出的数留下
# li = []
# for n in range(100, 9, -1):
#     if n % 2 == 0:
#         li.append(n)
# new_li = []
# for el in li:
#     if el % 4 == 0:
#         new_li.append(el)
# print(new_li)

# ######第十题：利用for循环和range，将1~30的数字一次添加到一个列表中，并循环这个列表，将能被3整出的数改成*。
# li = []
# for n in range(1, 31):
#     li.append(n)
# new_li = []
# for el in li:
#     if el % 3 == 0:
#         new_li.append("*")
#     else:
#         new_li.append(el)
# print(new_li)

######第十一题：查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，添加到一个新的列表中，最后循环打印这个列表
# li = ["TaiBai ", "ale  xC", "AbC   ", "egon", " ri  TiAn", "WuSir", "  aqc"]
# lst = []
# for el in li:
#     el = el.replace(" ", "")
#     if (el.startswith("A") or el.startswith("a")) and el.endswith("c"):
#         lst.append(el)
# print(lst)

# ######第十二题：开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊字符，则将用户输入的内容中的敏感词汇替换成等长度的*。
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# content = input("请输入评论内容: ")
# for el in li:
#     if el in content:
#         content = content.replace(el, "*"*len(el))
# print("你输入的内容是：" + content)

######第十三题：有如下列表，循环打印列表的每个元素，遇到列表再循环打印出它里面的元素,并将大写变小写！
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for el in li:
#     if type(el) == list:    #判断数据类型
#         for ell in el:
#             if type(ell) == str:
#                 ell = ell.lower()
#                 print(ell)
#             else:
#                 print(ell)
#     else:
#         if type(el) == str:
#             el = el.lower()
#             print(el)
#         else:
#             print(el)

######第十四题：把班级学生数学考试成绩录入到一个表中，并求平均值。要求：录入的时候带着人名录入，例如：张三_44
# lst = []
# while 1:
#     stu = input("请输入学生的姓名和成绩（姓名_成绩），录入Q退出：")
#     if stu.upper() == "Q":
#         break
#     lst.append(stu)
# #求平均值
# sum = 0
# for el in lst:
#     li = el.split("_")
#     sum = sum + int(li[1])
# print(sum/len(lst))

