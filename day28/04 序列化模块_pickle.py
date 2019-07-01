# pickle
import pickle
# dump的结果是bytes，dump用f文件句柄需要以"wb"形式打开，load所用的f是"rb"模式
# 几乎支持所有对象的序列化
# 对于对象的序列化需要这个对象的类在内存中
# 对于多次dump和load做了良好的处理


# dic = {1:(12,3,4),('a','b'):4}
#
# pic_dic = pickle.dumps(dic)
# print(pic_dic)      #bytes类型：b'\x80\x03}q\x00(K\x01K\x0cK\x03K\x04\x87q\x01X\x01\x00\x00\x00aq\x02X\x01\x00\x00\x00bq\x03\x86q\x04K\x04u.'
# new_pic = pickle.loads(pic_dic)
# print(new_pic)      #{1: (12, 3, 4), ('a', 'b'): 4}

# pickle支持几乎所有对象
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s = Student('alex',22)
# pic_s = pickle.dumps(s)
# print(pic_s)        #b'\x80\x03c__main__\nStudent\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00nameq\x03X\x04\x00\x00\x00alexq\x04X\x03\x00\x00\x00ageq\x05K\x16ub.'

# # 来一个游戏的存档和读档
# class Student:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# #初始化对象
# s = Student('alex',45,'None')
#
# #对象存档,存完档后注释
# # with open('pickle_dump',mode='wb') as f:
# #     pickle.dump(s,f)
#
# #从文件中读档
# with open('pickle_dump',mode='rb') as f:
#     旺财 = pickle.load(f)
# print(旺财.name,旺财.age,旺财.sex)

#--------------------------------------------

# pickle可以多次dump，并且也可以load出来
# with open('pickle_dump','wb') as f:
#     pickle.dump({'k1':'v1'}, f)
#     pickle.dump({'k11':'v1'}, f)
#     pickle.dump({'k11':'v1'}, f)
#     pickle.dump({'k12':[1,2,3]}, f)
#     pickle.dump(['k1','v1','l1'], f)

with open('pickle_dump',mode='rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break