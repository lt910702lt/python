# f = open("歌姬", mode="r", encoding="utf-8")
# s = f.read()
# f.close()  # 关闭句柄
# print(s)

# 路径有两种:
#    1. 相对路径    相对于你当前程序所在的文件夹
#    2. 绝对路径    1.从磁盘根目录寻找; 2.互联网上的一个绝对路径
# f = open("file/wuse", mode="r", encoding="utf8")
# s = f.read()
# f.close()
# print(s)

f = open("吃的", mode="r", encoding="utf-8")
for line in f:      # 每次读取一行,赋值给前面的line变量
    print(line)

s = f.readline()    #会面
ss = f.readlines()  #['会面\n', '炸鸡\n', '小米粥\n', '红烧菜\n', '红焖菜\n', '梅菜扣菜\n', '主题菜']
f.close()
