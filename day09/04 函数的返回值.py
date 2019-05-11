# def yue():
#     print("约会")
#     print("不约")
#     return "大妈"     #函数返回时,给调用方一个结果
#
# ret = yue()
# print(ret)

# 只要函数执行到Return,han
# 1. 每个函数,如果在函数中不写return,默认返回None
# 2. 可以只写一个return,也是返回None,停止函数的执行
# 3. return 一个返回值 你在调用方能接收到一个返回值
# 4. return 多个返回值 多个值需要用逗号","隔开
# def yue():
#     print("约会")
#     return
#     print("不约")
#
# ret = yue()
# print(ret)

def yue():
    print("大阳哥出马")
    return ("大妈", "萝莉", "御姐")


ret = yue()
print(ret)  # ('大妈', '萝莉', '御姐')

a, b, c = yue()
print(a)
print(b)
print(c)
