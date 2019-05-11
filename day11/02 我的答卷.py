# 一、选择题
# 1~5: BADBC  6~10: DBCAB
# 11.AB 12.BD 13.ABC 14.BD 15.CD

# 二、填空题
# 1. False
# 2. len(),append()
# 3. tuple(ll)
# 4. [3,4,5]
# 5. 9
# 6. dic.pop(key),dic.popitems()
# 7. "",tuple(),(,),{},0

# 三、解答题

# 四、编程题
# 1.
# s = "k:1|k1:2|k2:3|k3:4"
# lst = s.split("|")
# i = 0
# dict = {}
# while i < len(lst):
#     k, v = lst[i].split(":")[0], lst[i].split(":")[1]
#     dict[k] = int(v)
#     i += 1
# print(dict)

# 2.
# dic = {'最终计算结果:': None}
# content = input("请输入内容：").strip()  # 5+8+7
# lst = content.split("+")
# sum = 0
# for el in lst:
#     sum = sum + int(el.strip())
# dic['最终计算结果:'] = sum
# print(dic)

# 4.
# def func(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         new_lst.append(lst[i] + str[i])
#     return new_lst
# print(func(['1','2'])

# 5.
# result = []
# with open("t1.txt",encoding="UTF-8") as f:
#     # 读取每一行数据
#     for line in f:
#         dic = {}
#         lst = line.split(",")
#         dic['id'] = lst[0].strip()
#         dic['name'] = lst[1].strip()
#         dic['age'] = lst[2].strip()
#         dic['phone'] = lst[3].strip()
#         dic['job'] = lst[4].strip()
#         result.append(dic)
# print(result)

# 6.
# li = [11,22,33,44,55,66,77,88,99,90]
# result = {}
# for row in li:
#     if row > 66:
#         result.setdefault("k1",[]).append(row)
#     else:
#         result.setdefault("k2",[]).append(row)
# print(result)

# 7.
# user_list = [{"name": "alex", "hobby": "抽烟"},
#              {"name": "alex", "hobby": "喝酒"},
#              {"name": "alex", "hobby": "汤头"},
#              {"name": "wusir", "hobby": "喊麦"},
#              {"name": "wusir", "hobby": "街舞"},
#              ]

