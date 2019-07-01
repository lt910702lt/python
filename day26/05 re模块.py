import re

# 字符串
# 匹配
# findall   *****
# ret = re.findall('\d+','19874asdsda01231')
# print(ret)  #参数 返回值类型: 列表 返回值个数: 1 返回值内容: 所有匹配上的项

# search    *****
# ret2 = re.search('\d+','19874asdsda01231')
# print(ret2) #返回值类型: 正则匹配结果的对象 返回值个数: 1 返回值内容: 1、如果匹配上了就返回对象；2、如果没有匹配上，返回None
# print(ret2.group()) #返回的对象通过group来获取匹配到的第一个结果

# match     **
# ret3 = re.match('\d+','19874asdsda01231')
# print(ret3)
# print(ret3.group())


# 替换方法
# sub       ***
# ret = re.sub('\d+','H','replace123')
# print(ret)  #参数 返回值类型: 字符串 返回值个数: 1 返回值内容: 替换后的内容   -- replaceH

#subn       ***
# ret2 = re.subn('\d+','H','replace123')
# print(ret2)  #返回值类型: 元组 返回值个数: 1 返回值内容: (替换后的内容,替换的次数)   -- ('replaceH', 1)



# 切割方法
# split     ***
# ret = re.split('\d+','re22placd43ase123')
# print(ret)  #返回值类型: 列表 返回值个数: 1 返回值内容: 被分隔符切割都的内容   -- ['re', 'placd', 'ase', '']

# 进阶方法
# compile   *****  节省时间
# 将一个比较长的正则写到一个变量里
# re.findall('-0\.\d+|-[1-9]+(\.\d+)?','alex83egon20taibai40')
# ret = re.compile('-0\.\d+|-[1-9]+(\.\d+)?')
# res = ret.search('-0.3alex83egon20taibai40')
# print(res)
# print(res.group())

# findtier  *** 节省空间
# print(re.findall('\d','sjkhkdy982ufejwsh02yu93jfpwcmc'))
# ret = re.finditer('\d','sjkhkdy982ufejwsh02yu93jfpwcmc')
# for r in ret:
#     print(r.group())
