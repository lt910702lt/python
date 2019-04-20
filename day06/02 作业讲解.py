###第一题：有如下变量（tu是个元组），请实现要求的功能
# tu = ("alex", [11, 22, {"k1": "v1", "k2": ["age", "name"], "k3":(11, 22, 33)}, 44])
# # 1）、讲述元组的特性
# # 2）、请问tu变量中的第一个元素“alex”是否可以被修改
# # 3）、请问tu变量中的“k2”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# tu[1][2]["k2"].append("Seven")
# print(tu)
# # 4）、请问tu变量中的“k3”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# #不可以

###第二题：字典dic,dic = {"k1":"v1","k2":"v2","k3":[11,22,33]}
# dic = {"k1": "v1", "k2": "v2", "k3": [11, 22, 33]}
# 1)、请循环输出所有的key
# for k in dic.keys():
#     print(k)

# 2)、请循环输出所有的value
# for v in dic.values():
#     print(v)

# 3)、请循环输出所有的key和value
# for k, v in dic.items():
#     print(k)
#     print(v)

# 4)、请在字典中添加一个键值对，"k4":"v4"，输出添加后的字典
# dic["k4"] = "v4"
# dic.setdefault("k4", "v4")
# # print(dic)

# 5)、请修改字典中"k1"对应的值为"alex"，输出修改后的字典
# dic["k1"] = "alex"
# print(dic)

# 6）、请在k3对应的值中添加一个元素44，输出修改后的字典
# dic["k3"].append("44")
# # print(dic)

# 7）、请在k3对应的值的第一个位置插入个元素18，输出修改后的字典
# dic["k3"].insert(0, 18)
# print(dic)

###第三题：
av_catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
        "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "x-art.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}

# 1）、给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个  元素：'量很大'。
# av_catalog["欧美"]["www.youporn.com"].insert(1,"量很大")
# print(av_catalog)

# 2）、将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog["欧美"]["x-art.com"].remove("全部收费,屌丝请绕过")
# print(av_catalog)

# 3）、在此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表中添加"金老板最喜欢这个"
# av_catalog["欧美"]["x-art.com"].append("金老板最喜欢这个")
# print(av_catalog)

# 4）、将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
# print(av_catalog)

# 5）、给'大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog["大陆"]["1048"] = ['一天就封了']
# print(av_catalog)

# 6）、删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
# av_catalog["欧美"].pop("letmedothistoyou.com")
# del av_catalog["欧美"]["letmedothistoyou.com"]
# print(av_catalog)

# 7）、给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog["大陆"]["1024"][0] = av_catalog["大陆"]["1024"][0] + '可以爬下来'
# print(av_catalog)

###第四题：有字符串"k:1|k1:2|k2:3|k3:4"处理成字典{'k':1,'k1':2...}
# s = "k:1|k1:2|k2:3|k3:4"
# lst = s.split("|")
# dic = {}
# for el in s.split("|"):
#     k, v = el.split(":")
#     #dic.setdefault(k, v)
#     dic[k] = v
# print(dic)

###第五题：
# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，
# 将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {'k1': [], 'k2': []}
# for el in li:
#     if el < 66:
#         dic['k1'].append(el)
#     else:
#         dic['k2'].append(el)
# print(dic)

# li= [11,22,33,44,55,66,77,88,99,90]
# dic = {}
# for el in li:
#     if el > 66:
#         dic.setdefault("k1", []).append(el) # 1. 新增, 2. 查询
#     else:
#         dic.setdefault("k2", []).append(el)  # 1. 新增, 2. 查询
# print(dic)

###第六题：输出商品列表，用户输入序号，显示用户选中的商品。
# 要求：
##  1、页面显示 序号+商品名称+商品价格，如：
# goods = [{"name": "电脑", "price": 1999},
#          {"name": "鼠标", "price": 10},
#          {"name": "游艇", "price": 20},
#          {"name": "美女", "price": 998}]
##  2、用户输入选择的商品序号，然后打印商品名称和商品价格
##  3、如果用户输入的商品序号有误，则提示输入有误，并重新输入
##  4、用户输入Q或者q，退出程序
goods = [{"序号": "1", "name": "电脑", "price": 1999},
         {"序号": "2", "name": "鼠标", "price": 10},
         {"序号": "3", "name": "游艇", "price": 20},
         {"序号": "4", "name": "美女", "price": 998}]

#我的代码
# while 1:
#     print(goods)
#     no = input("请输入商品的序号（1-4）: ").strip()
#     for n in range(len(goods)):
#         if no == str(n):
#             print("序号{number}的商品是: {name}，它的价格是: {price}".format(number=goods[n-1].get("序号"), name=goods[n-1].get("name"),
#                                                                  price=goods[n-1].get("price")))
#         break
#     else:
#         print("你的输入有误，请重新输入！")
#     # 请用户输入选择的商品序号
#     if no.upper() == 'Q':
#         break
#老师代码
for i in range(len(goods)):
    good = goods[i]
    print(i+1, good['name'], good['price'])

while 1:
    content = input("请输入你要买的商品:")
    if content.upper() == "Q":
        break
    index = int(content) - 1    # 索引
    if index > len(goods) - 1 or index < 0:  # 调试
        print("输入有误. 请重新输入:")
        continue
    print(goods[index]['name'], goods[index]['price'])

