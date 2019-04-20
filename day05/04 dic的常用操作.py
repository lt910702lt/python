dic = {"及时雨": "宋江", "易大师": "剑圣", "维恩": "暗影猎手"}
# print(dic.keys())   #拿到所有的key，返回key的集合，像是列表，但是不是列表
# for key in dic.keys():
#     print(key)
#
# print(dic.values())
# for value in dic.values():
#     print(value)

# print(dic.items())
# for item in dic.items():
#     print(item[0])
#     print(item[1])

#解构，解包
# a, b = (1, 2)
# print(a)
# print(b)

for k, v in dic.items():
    print("人名：%s，外号：%s" % (v, k))
