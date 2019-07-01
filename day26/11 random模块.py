import random

#随机小数
# print(random.random())  # 0-1之内的随机小数
# print(random.uniform(1,5))  #取一个1-5之内的小数

#随机整数
# print(random.randint(1,2))  #[1,2],包含2在内的范围内随机取整数
# print(random.randrange(1,2))    #[1,2)，不包含2在内的范围内随机取整数
# print(random.randrange(1,10,2)) #[1,10)，不包含10在内的范围内随机取奇数

#随机抽取
# lst = [1,2,3,'aaa',('wahaha','qqxing')]
#1、随机抽取一个值
# ret = random.choice(lst)
# print(ret)

#2、随机抽取多个值
# ret = random.sample(lst,2)
# print(ret)

#3、打乱顺序 --  在原列表的基础上做乱序
# random.shuffle(lst)
# print(lst)


# 生成随机验证码

#1、4位数字的
import random
# 0-9

#基础版：
# code = ''
# for i in range(4):
#     num = random.randint(0,9)
#     code += str(num)
# print(code)

#函数版
# def rand_code(n=4):
#     code = ''
#     for i in range(n):
#         num = random.randint(0,9)
#         code += str(num)
#     return code
# print(rand_code(6))

#1、6位数字+字母的
# print(chr(97))  #a
# print(chr(122)) #z
# print(chr(65))  #A
# print(chr(90))  #Z

# 方法一：这种方法数字的几率太高
# def rand_code(n=6):
#     code = ''
#     for i in range(n):
#         rand_num = str(random.randint(0,9))
#         rand_alph_lower = chr(random.randint(97,122))
#         rand_alph_upper = chr(random.randint(65,90))
#         yzm = random.choice([rand_num,rand_alph_lower,rand_alph_upper])
#         code += yzm
#     return code
# print(rand_code(6))

def rand_code(n=6,alph_flag = True):
    code = ''
    for i in range(n):
        rand_num = str(random.randint(0,9))
        if alph_flag:
            rand_alph_lower = chr(random.randint(97,122))
            rand_alph_upper = chr(random.randint(65,90))
            rand_num = random.choice([rand_alph_lower,rand_alph_upper,rand_num])
        code += rand_num
    return code
print(rand_code(n=10))


# 数字/数字+字母
# def rand_code(n=6 , alph_flag = True):
#     code = ''
#     for i in range(n):
#         rand_num = str(random.randint(0,9))
#         if alph_flag:
#             rand_alph = chr(random.randint(97,122))
#             rand_alph_upper = chr(random.randint(65,90))
#             rand_num = random.choice([rand_num,rand_alph,rand_alph_upper])
#         code += rand_num
#     return code
#
# ret = rand_code(n = 4)
# print(ret)