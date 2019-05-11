f = open("小护士模特", mode="wb")    #读取的内容直接就是字节
f.write("你好啊".encode("utf-8"))
f.close()
