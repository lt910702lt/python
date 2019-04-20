'''
gender = input("你是男的还是女的？")


#if语句，==表示判断
if gender == '男的':
    print("滚蛋！")
print("吓死我了")


if gender == '女的':
    print("请进，欢迎光临！")
else:
    print("滚蛋！")


if gender == '女的':
    age = input("你多大了啊？")  #年龄大于30就不开门了
    if int(age) < 30:
	    print("请进！")
    else:
	    print("大妈，您去隔壁看金老板")
else:
    print("滚蛋！")



#输入你兜里的钱
#如果你的钱大于500块，喝啤酒吃炸鸡，生活美滋滋
#如果你兜里的钱小于500，大于300，吃个盖浇饭，生活乐无边
#如果你兜里的钱小于300，大于50，吃个方便面，开心
#如果你兜里的钱小于50，今天减肥。

money = input("请输入你兜里的钱：")
money = int(money)
if money > 500:
	print("喝啤酒吃炸鸡，生活美滋滋!")
else:
	if money > 300:
		print("吃个盖浇饭，生活乐无边")
	else:
		if money > 50:
			print("吃个方便面，开心")
		else:
			print("今天减肥")


money = int(input("请输入你兜里的钱："))
if money > 500:
	print("喝啤酒吃炸鸡，生活美滋滋!")
elif money > 300:
	print("吃个盖浇饭，生活乐无边!")
elif money > 50:
	print("吃个方便面，开心")
else:
	print("今天减肥")
'''