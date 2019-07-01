'''
不改变函数原来的调用方式 动态的给函数添加功能
'''
def create_people():
    print('抓泥巴，捏个人，吹口气，活了！')

# create_people()
# create_people()
# create_people()

# def koushui_create_people(reg):
#     print("加口唾沫！")
#     return reg

def koushui_create_people(arg):
    def inner():
        print("加口唾沫！")
        arg()
    return inner

# koushui_create_people()
# 开放封闭原则
# 1. 对添加新功能是开放的
# 2. 硬改已经存在的代码
create_people = koushui_create_people(create_people)
create_people()