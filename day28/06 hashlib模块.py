# 摘要算法模块
import hashlib

# 能够把一个 字符串、数字的变量， 转换成一个定长的 密文的 字符串，字符串里的每一个字符都是十六进制数字
# 'alex3714'

# 字符串 -> 密文
# 密文 -> 字符串     不可逆的
# 对于同一个字符串，用相同的算法，相同的手段取进行摘要，获得的值总是相等的
# 对于同一个字符串，不管这个字符串有多长，只要它是相同的，那么不管在什么环境下，执行多少次，任何语言中
# 使用相同的算法\相同的手段得到的结果永远是相同的
# 只要不是相同的字符串，得到的结果一定不同

# md5是一个算法
# 1、得到一个32位的字符串
# 2、每个字符都是一个十六进制
# 3、算法相对sha1简单，速度快
# hashlib.md5()
# update和hexdigest  --  tab没有提示，要手动写出
s = 'liut520'
## 直接用md5加密，不太安全，虽然本身比较安全，但挡不住有撞库的风险，因此需要加盐
# md5_obj = hashlib.md5()
# md5_obj.update(s.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res)  #8ea1651952e92e9dc6a8eb3eed529ee2
# print(res,len(res),type(res))   #8ea1651952e92e9dc6a8eb3eed529ee2 32 <class 'str'>

## 加盐
# 一、静态加盐，也有一定的风险（注册N多账号，用简单的密码生成md5码，去和数据库匹配）
# md5_obj = hashlib.md5('任意字符的盐'.encode('utf-8'))
# md5_obj.update(s.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res)
# print(res,len(res),type(res))   #ecfeef2f056d8dd3dba2915aea3c1e5f 32 <class 'str'>

# 二、动态加盐
# 用用户名来加盐，用户名不允许重复
# username = input('username:')
# passwd = input('password:')
# md5_obj = hashlib.md5(username.encode('utf-8'))
# md5_obj.update(passwd.encode('utf-8'))
# print(md5_obj.hexdigest())      # 每个用户密码的结果都不相同

#-------------------------------

# sha1也是一个算法
# 1、得到一个40位的字符串
# 2、每个字符都是一个十六进制
# 3、算法相对md5复杂，速度慢
# hashlib.sha1()
# sha1_obj = hashlib.sha1()
# sha1_obj.update(s.encode('utf-8'))
# res1 = sha1_obj.hexdigest()
# print(res1)
# print(res,len(res1),type(res1))     #8ea1651952e92e9dc6a8eb3eed529ee2 40 <class 'str'>


###---------------------------------------------------
# 文件一致性校验
md5_obj = hashlib.md5()
with open('05 序列化模块_shelve.py','rb') as f:
    md5_obj.update(f.read())
    ret1 = md5_obj.hexdigest()


md5_obj = hashlib.md5()     #注意要重新实例化md5
with open('05 序列化模块_shelve.bak.py','rb') as f:
    md5_obj.update(f.read())
    ret2 = md5_obj.hexdigest()

print(ret1,ret2)

# 读取一个超大文件（一个字符，一次性读完，和分开读再合并，结果是一样的）
# 将大文件，按照指定大小循环读取

# 写成一个函数
# 1、参数：文件1的路径，文件2的路径，默认参数
# 计算着两个文件的md5值
# 返回它们的一致性结果 T/F

