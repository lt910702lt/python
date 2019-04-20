'''
#例1：循环8次
count = 1
while count <= 8:
    print("第" + str(count) + "次喷！！")
    print("你是alex么?")
    print("你全家都是太白")
    count = count + 1


#例2：break和continue的用法
while True:
    s = input("请开始你的喷:")
    if s == 'q':
        break       #停止当前的循环

    #过滤掉马化腾
    if '马化腾' in s:
        print("你输入的内容含有屏蔽语言！！")
        continue    #停止当前本次循环，开始下一次循环

    print("喷的内容是:" + s)

#例3：累加求和
#1+2+3+4+...+100
count = 1
total = 0
while count <= 100:
    #print(count)
    total = total + count   #把total中的值（上一次的求和）和count的值累加
    count = count + 1

print(total)


#例4：输出1-100所有的奇数
count = 1
while count <= 100:
    if count % 2 != 0:
        print(count)
    count = count + 1
'''


