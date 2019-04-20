'''
#1、判断下列逻辑语句的True，False
    1) 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6    #True
        False or True or False or False
    2) not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6   #False
        False  or False or Fasle
print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

2、求出下列逻辑语句的值
    1) 8 or 3 and 4 or 2 and 0 or 9 and 7   #8
        8 or 4 or 0 or 7
    2) 0 or 2 and 3 and 4 or 6 and 0 or 3   #4
        0 or 4 or 0 or 3

print(8 or 3 and 4 or 2 and 0 or 9 and 7)
print(0 or 2 and 3 and 4 or 6 and 0 or 3)

3、下列结果是什么？
    1) 6 or 2 > 1   #6
    2) 3 or 2 > 1   #3
    3) 0 or 5 < 4   #False
    4) 5 < 4 or 3   #3
    5) 2 > 1 or 6   #True
    6) 3 and 2 > 1  #True
    7) 0 and 3 > 1  #0
    8) 2 > 1 and 3  #3
    9) 3 > 1 and 0  #0
    10) 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2   #2
        2 or 4 or True

print(6 or 2 > 1)
print(3 or 2 > 1)
print(0 or 5 < 4)
print(5 < 4 or 3)
print(2 > 1 or 6)
print(3 and 2 > 1)
print(0 and 3 > 1)
print(2 > 1 and 3)
print(3 > 1 and 0)
print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)

4、while循环语句的基本结构
    while 循环体：
        代码块
        if 条件判断:
            代码块
            break
            cuntinue
    else:
        代码块
5、利用while语句写出猜大小的游戏：
    设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了；
只有等于66，显示猜测结果正确，然后退出循环。

target = 66
while True:
    count = int(input("请输入一个数字:"))
    if count > target:
        print("你输入的数字大了，请重新输入！")
        continue
    elif count < target:
        print("你输入的数字小了，请重新输入！")
    else:
        print("恭喜你，猜中了！")
        break

6、在5题的基础上进行升级：
    给用户三次猜测机会，如果三次之类猜测对了，则显示猜测正确，退出循环，如果三次之类没有猜测正确，则自动退出循环，
并显示“太笨了你。。。”

target = 66
cishu = 3
while cishu > 0:
    count = int(input("请输入一个数字:"))
    if count > target:
        print("你输入的数字大了，请重新输入！")
    elif count < target:
        print("你输入的数字小了，请重新输入！")
    else:
        print("恭喜你，猜中了！")
        break
    print ("还剩%d次了" % cishu)
    cishu -= 1
else:
    print("你太笨了~~")

7、使用while循环输出1 2 3 4 5 6 8 9 10

count = 1
while count <= 10:
    if count == 7:
        count += 1
        continue
    else:
        print(count)
    count += 1

8、求1-100的所有数的和

count = 1
sum = 0
while count <= 100:
    sum += count
    count += 1
print(sum)


9、输出1-100内的所有奇数

count = 1
while count <= 100:
    if count % 2 == 1:
        print(count)
    count += 1

10、输出1-100内的所有偶数

count = 1
while count <= 100:
    if count % 2 == 0:
        print(count)
    count += 1

11、求1-2+3-4+5...99的所有数的和

a = -1
count = 1
sum = 0
while count <= 99:
    mi = (count % 2 + 1)
    sum += (count*(a**mi))
    count += 1
print(sum)

#老师的代码
#1+3+5+...+99-(2+4+...+98)
sum = 0
count = 1
while count < 100:
    if count % 2 == 0:
        sum = sum - count
    else:
        sum = sum + count
    count += 1
print(sum)

12、用户登陆（三次输错机会），且每次输错误时显示剩余输错次数（提示：使用字符串格式化）

username = "alex"
password = "sb"
count = 1
while count <= 3:
    un = input("请输入用户名:")
    pw = input("请输入密码:")
    if un == username and pw == password:
        print("登陆成功")
        break
    else:
        print("登陆失败")
    print("还剩余 %d 次登陆机会" % (3-count))
    count += 1
else:
    print("机会已用完，你的账户被锁定！")

13、用户输入一个数，判断这个数是否为质数（升级题）
14、输入一个广告标语，判断这个广告是否合法，根据最新的广告法来判断。广告法内容过多，我们就判断是否包含'最'，'第一'，'稀缺'，
'国家级'等字样，如果包含，提示:广告不合法
'''
ad = input("请输入你的广告标语:")
if "最" in ad or '国家级' in ad or '第一' in ad or '稀缺' in ad:
    print("不合法")
else:
    print("合法")
'''
15、输入一个数，判断这个数是几位数（用算法实现）（升级题）
'''