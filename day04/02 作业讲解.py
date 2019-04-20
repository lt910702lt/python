'''
name = " aleX leNB "
#1、请输出name变量对应的值中“e”所在索引的位置？
#print(name.find("e", 0, len(name)))
count = 0
while count < len(name):
    if name[count] == 'e':
        print(count)
    count += 1
#将首个字母的小a替换为A
print(name.replace('a', 'A', 1))

##第二题：有字符串s = "123a4b5c"
1）通过对s切片形成新的字符串s1,s1 = "123"    #s1 = s[0:3]
2）通过对s切片形成新的字符串s2,s2="a4b"      #s2 = s[3:6]
3）通过对s切片形成新的字符串s3,s3="1345"     #s3 = s[::2]
4）通过对s切片形成字符串s4,s4="2ab"          #s4 = s[1:6:2]
5）通过对s切片形成字符串s5,s5="c"            #s5 = s[-1]
6）通过对s切片形成字符串s6,s6="ba2"          #s6 = s[-3::-2]

##第三题：用while和for循环分别打印字符串s = "asdfer"中的每个元素
s = "asdfer"
#for c in s:
#    print(c)
count = 0
while count < len(s):
    print(s[count])
    count += 1

##第四题: 用for循环对s = "321"进行循环，打印的内容一次是:"倒计时3秒"，"倒计时2秒"，"倒计时1秒"
s = "321"
for c in s:
    print("倒计时{second}秒".format(second=c))
    print("倒计时% s秒" % c)
else:
    print("出发")

##第五题：遍历字符串s = "23123dsda2das255dasdas566sadas"，统计数字的个数
s = "23123dsda2das255dasdas566sadas"
count = 0
sum = 0
while count < len(s):
    if s[count].isdigit():
        sum += 1
    count += 1
print(sum)

##第六题：1-2+3-4...+99的总和，并且去掉88
count = 0
sum = 0
while count < 100:
    if count == 88:
        count += 1
        continue
    if count % 2 == 0:
        sum -= count
    else:
        sum += count
    count += 1
print(sum)

##第七题：判断一个字符出串是否回文
s = "上海自来水来自海上"
s = input("请输入字符串: ").strip()
if s == s[::-1]:
    print("是回文")
else:
    print("不是回文")
'''
##第八题：输入一个字符串，判断大写、小写、数字、其他字符出现的次数，并输出结果
s = input("请输入一个字符串: ")
digit_num = 0
upper_c_num = 0
lower_c_num = 0
other_num = 0
for c in s:
    if c.isdigit():
        digit_num += 1
    elif c.isupper():
        upper_c_num += 1
    elif c.islower():
        lower_c_num += 1
    else:
        other_num += 1
print("数字有{digit_num}个，大写字母有{upper_c_num}个，小写字母有{lower_c_num}个，其他{other_num}个".format(digit_num=digit_num,upper_c_num=upper_c_num,lower_c_num=lower_c_num,other_num=other_num))