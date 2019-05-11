###第一题: 老男孩还好声音选秀大赛评委在打分的时候,可以进行输入.假设,老男孩有10个评委,将10个评委打分,要求:分数必须大于5分,小于10分.
# for i in range(1, 11):
#     fen = input("请%d号评委打分:" % i)
#     if int(fen) > 5 and int(fen) < 10:
#         print("OK的分数")
#     else:
#         print("不在有效范围内")

###第二题: 电影打分. 程序先给出一个目前在上映的电影列表,由用户给每一个电影打分,最终,将改用户打分信息公布出来.
# lst = ['金瓶梅','解救吴先生','美国往事','西西里的美丽传说']
# 结果:{'金瓶梅':99,'解救吴先生':88,'美国往事':23,'西西里的美丽传说':78}

# 我写的程序
# lst = ['金瓶梅', '解救吴先生', '美国往事', '西西里的美丽传说']
# print("有如下几部电影:")
# for n in range(len(lst)):
#     print(str((n + 1)) + ": " + lst[n])
#
# dic = {}
# for n in range(len(lst)):
#     print("请为 %d 号电影打分:" % (n+1))
#     fen = input("请输入分数:")
#     dic.setdefault(lst[n], fen)
# print(dic)

# #老师的程序
# lst = ['金瓶梅', '解救吾先生', '美国往事', '西西里的美丽传说']
# dic = {}
# for el in lst:
#     fen = input("请给%s电影进行打分:" % el)
#     dic[el] = fen
# print(dic)

###第三题: 念数字. 给出一个字典,在字典中标志出每个数字的发音,包括相关符号.然后由用户输入一个数字,让程序读出相对应的发音(打出即可)
# dic = {
#     "-": "fu",
#     "1": "yi",
#     "2": "er",
#     "3": "san",
#     "4": "si",
#     "5": "wu",
#     "6": "liu",
#     "7": "qi",
#     "8": "ba",
#     "9": "jiu",
#     "0": "ling",
#     ".": "dian"
# }
# content = input("请输入一个数:")  # 127
# for c in content:
#     print(dic[c], end=" ")
# else:
#     print()
# print("你好啊")

###第四题: 干掉主播. 现由如下主播收益信息,按照要求,完成相应操作
zhubo = {"卢本伟": 999999, "冯提莫": 14000000, "陈一发儿": 15000000, "金老板": 4500}
# 1. 计算平均收益
# sum = 0
# for value in zhubo.values():
#     sum = sum + value
# ave = sum / len(zhubo)
# print(ave)

# 2. 干掉收益小于平均值的主播
##我的程序
# dic = {}
# for k,v in zhubo.items():
#     if v > ave:
#         dic[k] = v
# print(dic)
##老师的程序
# lst = []
# for k,v in zhubo.items():
#     if v < ave:
#         lst.append(k)
# for el in lst:
#     zhubo.pop(el)

# 3. 干掉卢本伟
zhubo.pop("卢本伟")
print(zhubo)
