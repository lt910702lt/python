f = open("写读", mode="w+", encoding="utf-8")
f.write("烦得很")
s = f.read()
print(s)        # 默认w+ 模式读不出来,可以用f.seek(0)将光标移到开头(w+基本没什么用)
f.flush()
f.close()


