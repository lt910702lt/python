# 定义主程序方法
def main():
    # 登陆之后，选择操作(使用反射)
    start_l = [('登陆',), ('注册',), ('退出',)]
    # 用上一个枚举
    for index, item in enumerate(start_l):
        print(index, item[0])
    while True:
        try:
            num = int(input('>>>'))
            func_str = start_l[num-1][1]
        except:
            print('你输入的信息有误')
            #字符串数据类型的方法 login register quit
