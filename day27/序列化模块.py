# 归一化
# 实例化
# 初始化
# 序列化 -- 这个序列化只包含字符串
    # 列表、元组、字符串

# ......操作得到一个字符串的结果，这个过程就叫序列化
# 字典/ 列表 / 数字 / 对象 - 序列化 -> 字符串
# 为啥要序列化？
    # 1、要把内容写入文件      序列化
    # 2、网络传输数据          序列化

# 字符串 ->  字典/ 列表 / 数字 / 对象 - 反序列化


# json  -- 4个方法
# dumps: 直接操作变量
# dump: 操作变量和文件
import json
# dic = {'aaa':'bbb','ccc':'ddd'}
# str_dic = json.dumps(dic)       # 转换为json
# print(dic)
# print(str_dic,type(str_dic))    # 反转回dict
#
# ret = json.loads(str_dic)
# print(ret,type(ret))

#将dict序列化，并写入文件当中
dic = {'aaa':'bbb','ccc':'ddd'}
with open('json_dump','w') as f:
    json.dump(dic,f)

# 从文件中读出来
with open('json_dump','r') as f:
    print(json.load(f))


# pickle    -- 4个方法
# shelve    -- 1个方法