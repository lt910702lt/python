# dic = {'jay': '周杰伦', 'jj': '林俊杰'}
# print(dic)

#字典的相关操作
# # 1、增加
# dic = {'昆凌': '周杰伦的老婆'}
# dic['国际章'] = "汪峰的老婆"    #新增
#
# dic.setdefault("马蓉", "王宝强前老婆")
# dic.setdefault("马蓉", "宋哲的现任老婆")     #如果已有了key，则不再重新赋值
# dic['国际章'] = '雄壮的老外'                 #如何key重复了，会替换以前的key
# print(dic)

# 2、删除
# dic = {'jay': '周杰伦', 'jj': '林俊杰'}
# ret = dic.pop("jay")    #删除一个元素，返回这个元素的值
# del dic["jay"]
# ret = dic.popitem()     #随机删
# dic.clear()             #清空字典

# 3、修改
# dic1 = {"李晨": "范冰冰", "邓超": "孙俪", "王祖蓝": "李亚男"}
# dic2 = {"李晨": "张馨予", "郑凯": "baby", "王宝强": "马蓉"}
# dic1.update(dic2)   #  把dic2中的内容更新到 dic1 , 如果存在了key. 替换. 如果不存在,添加
# print(dic1)
# print(dic2)

# 4、查询
dic = {"及时雨": "宋江", "小李广": "花荣", "黑旋风": "李逵", "易大师": "剑圣"}

dic["大宝剑"] = "盖伦"       # 新增
dic["及时雨"] = "天老爷"     # 修改

print(dic["易大师"])               #如果key不存在，报错
print(dic.get("易大师脑残", "小宝"))           #如果key不存在，返回None；还可以指定默认值

#get()
# 可以通过key来获取value的值. 那么如果key不存在. 返回None.
# 可以给出一个默认值. 当key不存在的时候返回默认值

# dic = {"及时雨":"宋江", "易大师":"剑圣"}
# dic.setdefault("及时雨", "诺克萨斯")    # 可以帮我们添加
# print(dic)
# ret = dic.setdefault("及时雨123", "hello")
# print(ret)
# print(dic)

# 1. 首先判断原来的字典中有没有这个key . 如果没有. 执行新增
# 2. 用这个key去字典中查询, 返回查到的结果
# dic = {"及时雨":"宋江", "易大师":"剑圣"}
# ret = dic.setdefault("及时雨", "西门庆")
# print(dic)
# print(ret)

