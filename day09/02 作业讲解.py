###第一题: 有如下文件,里面的内容如下,分别完成以下功能:
'''
老男孩是一个培训机构
为学生服务,
为学生未来,
都是骗人的,哈哈
'''
## 1.1. 将原文件全部读出来并打印
# f = open("oldboy", mode="r", encoding="utf-8")
# s = f.read()
# f.flush()
# f.close()
# print(s)

# 1.2. 在原文件后面追加一行内容:信不信由你,反正我信了
# f = open("oldboy", mode="a", encoding="utf-8")
# f.write("\n信不信由你.反正我信了")
# f.flush()
# f.close()

# 1.3. 将原文件全部读出来,并在后面添加一行内容:信不信由你,反正我信了
# f = open("oldboy", mode="r+", encoding="utf-8")
# f.read()
# f.write("\n信不信由你.反正我信了")
# f.flush()
# f.close()

# 1.4. 将源文件全部清空,换成下面内容
# f = open("oldboy", mode="w+", encoding="utf-8")
# f.write('''每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。
# ''')
# f.flush()
# f.close()

# 1.5. 将源文件内容全部读出来,并在"都是骗人的,哈哈"这一行前面加入"你们九信吧",将更改之后的新内容,写入到一个新的文件a1.txt
# import os
#
# with open("oldboy", mode="r", encoding="utf-8") as f1, open("oldboy_new", mode="w", encoding="utf-8") as f2:
#     s = f1.read()
#     ss = s.replace("都是骗人的,哈哈", "你们就信吧!\n都是骗人的,哈哈")
#     f2.write(ss)
# os.remove("oldboy")
# os.rename("oldboy_new", "oldboy")

###第二题: 有文件内容如下,通过代码,将其构建成这种数据类型
# 序号  部门  人数  平均年龄    备注
# 1    Python   30    26         单身狗
# 2    Linux    26    30         没对象
# 3    运营部   20    24         女生多

# [{'序号': '1', '部门': 'Python', '人数': '30', "平均年龄": '26', '备注': '单身狗'}]
# ......

f = open("a6", mode="r", encoding='utf-8')
line = f.readline()
lst = line.split()  # 第一行切割完成,基础数据就完成了

result = []  # 定义一个结果列表
for lin in f:
    ll = lin.split()  # 每一行的数据
    dic = {}  # 将每一行切割后的结果放入到不同的字典里
    for i in range(len(ll)):
        dic[lst[i]] = ll[i]
    result.append(dic)  # 将字典添加到结果列表里
print(result)