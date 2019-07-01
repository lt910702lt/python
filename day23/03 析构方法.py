# 构造方法  申请一个空间
# 析构方法  释放一个空间
# 某对象借用了操作系统的资源,还要通过析构方法归还回去 : 文件资源  网络资源

# 垃圾回收机制
# class A:
#     # 析构方法 del A的对象，会自动触发这个方法
#     def __del__(self):
#         print('执行我了')
#
# a = A()
# # del a   #对象的删除
# print(a)

#在什么时候用
class File:
    #处理文件
    def __init__(self,file_path):
        self.f = open(file_path)
    def read(self):
        self.f.read(1024)
    #析构函数，是去归还/释放一些在创建对象的时候借用的一些资源
    def __del__(self):
        # del对象的时候
        # python解释器的垃圾回收机制，回收这个对象所占的内存的时候
        self.f.close()
f = File('文件名')
f.read()
# 不管是主动还是被动,这个f对象总会被清理掉,被清理掉就触发__del__方法,触发这个方法就会归还操作系统的文件资源

# python解释器在内部就能搞定的事
# 申请一块空间 操作系统分配给你的
# 在这一块空间之内的所有事，归你的python解释器来管理

f = open('wenjian') #python --> 操作系统 --> 硬盘里的文件 --> 文件操作符

