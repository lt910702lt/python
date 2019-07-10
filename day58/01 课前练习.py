# ------------------------------------------------------------------
# 字符串的切割
s = "Alex SB 哈哈\r\nx:1\r\ny:2\r\nz:3\r\n\r\n自行车"

# 问题1：如何取到["Alex SB 哈哈 \r\nx:1\r\ny:2\r\nz:3","自行车"]
ret1 = s.split('\r\n\r\n')
print(ret1)

# 问题2：如何在上面结果基础上拿到["Alex","SB","哈哈"]
ret2 = ret1[0].split("\r\n")
ret3 = ret2[0].split(" ")
print(ret3)

# 问题3：如何在上面的结果基础上拿到SB
ret4 = ret3[1]
print(ret4)
# -------------------------------------------------------------
# 列表的操作
# 有一个列表，他的内部是一些元祖，元祖的第一个元素是姓名，第二个元素是爱好。
# 现在我给你一个姓名，如"Egon",如果有这个姓名，就打印出他的爱好，没有就打印查无此人。

list1 = [
    ("Alex", "烫头"),
    ("Egon", "街舞"),
    ("Yuan", "喝茶")
]

name = input('请输入一个人名:')

for i in list1:
    if name == i[0]:
        print("%s's hobby is %s" % (name, i[1]))
        break
else:
    print("%s not fond" % name)

# ---------------------------------------------------------------
# 文件的操作
# 我有一个HTML文件"login.html"
# 问题1：我如何读取它的内容保存到变量html_s？
f = open('login.html', mode='r', encoding='utf8')
html_s = f.read()
print(html_s)
f.close()

# 问题2：我如何读取它的二进制内容保存到变量html_b？
f = open('login.html', mode='rb')
html_b = f.read()
print(html_b)
f.close()

# ------------------------------------------------------------------------------------------
# 字符串的操作
s2 = "Alex 花了一百万买了辆电动车，真@@xx@@。"

# 问题1：如何把上面的s2转变成"Alex 花了一百万买了辆电动车，真SB。"
ret5 = s2.replace("@@xx@@", "SB")
print(ret5)
