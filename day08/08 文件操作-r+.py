# f = open("老师点名", mode="r+", encoding="utf-8")   #r+模式,默认情况下光标在文件的开头,必须先读,后写
# f.write("周润发")
# s = f.read()
# f.flush()
# f.close()
# print(s)

f = open("精品", mode="r+", encoding="utf-8")
f.write("哈哈")  # 1.在没有任何操作之前进行写,在开头写  2. 如果读取了一些内容,再写,写入的是最后
# f.seek(0)  # 移动到开头
# f.seek(0, 2)  # 移动到末尾
