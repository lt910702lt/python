'''
#1、首字母大写
s = "alex and wusir and taibai"

s.capitalize()
print(s)
print(s.capitalize())

#2、所有字母小写、大写
s = "Alex is not a good Man"
print(s.upper())    ***，忽略大小写判断的都可以用到
print(s.lower())
while True:
    content = input("请喷:")
    if content.upper() == 'Q':
        break
    print("你喷了:" + content)

#3、大小写互换
s = "Alex is not a good Man"
print(s.swapcase())

#4、每个被特殊字符隔开的字母首字母大写（中文也算特殊字符）
s = "Alex i马化腾s not a good Man"
print(s.title())

#5、居中
s = "麻花腾"
print(s.center(9,"*"))

#6、去空格(对于用户输入的内容，最好左右去掉空格)
# 也可以去掉指定内容（去掉左右两端，不对中间生效）
# 去两边：s.strip()
# 去左：s.lstrip
# 去右：s.rstrip
num = int(input("请输入一个数字:").strip())
print(num)
s = "aaaah呵aaa呵呵aaaaa"
print(s.strip("a"))

#7、字符串的替换 *****
s = "alex wusir alex sb taibai"
print(s.replace("alex", "小雪"))
#只替换一个
print(s.replace("alex", "小雪", 1))
#去掉str里面中的所有空格
print(s.replace(" ", ""))


#8、字符串的切割****
#切完的内容是列表，列表里面的是字符串['alex', 'wuse', 'taibai', 'bubai']
s = "alex_wuse_taibai_bubai"
print(s.split("_"))


######9、字符串格式化输出#########
s = "我叫{}，我今年{}岁了，我喜欢{}".format("sylar", 18, "周杰伦的老婆")
print(s)
s = "我叫{1}，我今年{2}岁了，我喜欢{0}".format("sylar", 18, "周杰伦的老婆")   #指定位置
print(s)
s = "我叫{name}，我今年{age}岁了，我喜欢{who}".format(name="sylar", age=18, who="周杰伦的老婆")   #指定参数
print(s)



################ 查 找 #################
s = "汪峰的老婆不爱汪峰"

#1、以。。。开头
print(s.startswith("汪峰"))   #True
#2、以。。。结尾
print(s.endswith("爱妃"))     #False
#3、统计计数,计算xxx出现的次数
print(s.count("的"))          #1
#4、查找
print(s.find("老婆"))         #3，计算xxx字符串在原字符串中出现的位置，如果没有则返回“-1”
#5、查找+切片
print(s.find("汪峰", 3))      #7
#6、索引的位置
print(s.index("汪峰"))        #0  index中的内容如果不存在，则返回“报错”

################ 判 断 #################
s = '123'
print(s.isdigit())      #判断是否由数字组成
print(s.isalpha())      #判断是否由字母组成
print(s.isalnum())      #判断是否由字母和数字组成
s = "1423574609"
print(s.isnumeric())    #判断是否为数字
s = "一二壹二五"
print(s.isnumeric())    #判断是否为数字（汉字也能判断，但是不能判断“两”）
'''

################ 字符串长度 #################
s = "你今天喝酒了吗"
print(len(s))

#把字符串从头到尾进行遍历
s = "你今天喝酒了吗"
#方法1
count = 0
while count < len(s):
    print(s[count])
    count += 1
#方法2。优势：简单    劣势：没有索引
for c in s:
    print(c)
