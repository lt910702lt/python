'''
lst = [1, "花生", "山药"]
print(type(lst))
lst = (1, "花生", "山药")   #当元组里面的元素少于1个时，需要添加逗号！
print(type(lst))

tu = (1)
print(type(tu))
tu = ("哈哈")
print(type(tu))
tu = (1,)
print(type(tu))
tu = ("哈哈",)
print(type(tu))
#tu = (,)       #注意不能直接","，如果要写空元组，需要写成tu = tuple()
print(type(tu))
'''

# tu = ('DNF', "LOL", "CF", "斗地主", "消消乐")
# print(tu[2:])
# tu[2] = "王者荣耀"  # 尝试着修改 不能改, 会报错

# for el in tu:
#     print(el)

# tu = (1, "马化腾", ["胡辣汤", "疙瘩汤", "西红柿鸡蛋汤"])
#
# tu[2].append("粘包米") # 元组本身没有变. 变的是儿子中的内容
# print(tu)

# 元组的嵌套
tu = ("王昭君", "小泽老师", "夏川美里", "斯琴高娃", ("邱老师", ("刀削面", "炒饼", "盖浇饭"), "刘德华", "周星星", "渣渣辉"))
print(tu[4][1][2])