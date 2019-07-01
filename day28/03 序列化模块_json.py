import json

# 一、json格式的限制1,json格式的key必须时字符串数据类型
# 如果数字为key，那么dump之后会强行转成字符串数据类型
# dic = {1:2,3:4}
# str_dic = json.dumps(dic)
# print(str_dic)      #{"1": 2, "3": 4}
# new_dic = json.loads(str_dic)
# print(new_dic)      #{'1': 2, '3': 4}

# 二、json是否支持元组,对元组做value的字典会把元组强制转换为列表
# dic = {'abc':(1,2,3)}
# str_dic = json.dumps(dic)
# print(str_dic)      #{"abc": [1, 2, 3]}
# new_dic = json.loads(str_dic)
# print(new_dic)      #{'abc': [1, 2, 3]}

# 三、json是否支持元组做key，不支持！！
# dic = {(1,2,3):'abc'}
# str_dic = json.dumps(dic)   #报错，keys must be str, int, float, bool or None, not tuple

# 四、对列表的dump，dump到文件的内容必须是双引号"" ,如果被修改为单引号，则无法被load出来

# lst = ['aaa',123,'bbb',12.456]
# with open('json_dump',mode='w') as f:
#     json.dump(lst,f)

# with open('json_dump') as f:
#     new_lst = json.load(f)
#     print(new_lst)

# 五、能不能多次dump数据到文件里，可以多次dump，但是无法load出来
# dic = {'abc':(1,2,3)}
# lst = ['aaa',123,'bbb',12.456]
# with open('json_dump',mode='w') as f:
#     json.dump(dic,f)
#     json.dump(lst,f)      #文件内容：{"abc": [1, 2, 3]}["aaa", 123, "bbb", 12.456]

# with open('json_dump') as f:
#     ret = json.load(f)
#     print(ret)  #报错：json.decoder.JSONDecodeError

# 想要dumo多个数据进入文件，用dumps!
# dic = {'abc':(1,2,3)}
# lst = ['aaa',123,'bbb',12.456]
# with open('json_dump',mode='w') as f:
#     str_lst = json.dumps(lst)
#     str_dic = json.dumps(dic)
#     f.write(str_lst+'\n')
#     f.write(str_dic+'\n')

# with open('json_dump') as f:
#     for line in f:
#         ret = json.loads(line)
#         print(ret)

# 六、中文格式的,ensure_ascii = False
# dic = {'abc':(1,2,3),'country':'中国'}
# # ret = json.dumps(dic,ensure_ascii=False)
# # print(ret)
# # dic_new = json.loads(ret)
# # print(dic_new)
# with open('json_dump',mode='w',encoding='utf-8') as f:
#     json.dump(dic,f,ensure_ascii=False)

#七、其他参数，整理输出的格式（更好看，但是浪费空间），如果是存文件，不要这样做
data = {'username':['李华','二愣子'],'sex':'male','age':16}
json_dic2 = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)
print(json_dic2)

# set不能被dump/dumps