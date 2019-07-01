import time

# 时间戳时间，float数据类型，格林威治时间
    # 英国伦敦 1970.1.1 0:0:0
    # 北京时间 1970.1.1 8:0:0
    # 1558493359.7192008
# 结构化时间，时间对象
    # 时间对象，能够通过属性名来获取对象中的值
# 格式化时间，str数据类型，字符串时间
    # 可以根据你想要的格式来显示时间


# print(time.time())      # 时间戳时间
# print(time.strftime('%Y-%m-%d %H:%M:%M'))   # 格式化时间 str format time
# # print(time.localtime())
# time_obj = time.localtime()     # 结构化时间
# print(time_obj)     #tm_isdst=0 夏令时，夏天拨快2小时，冬天拨慢2小时
# print(time_obj.tm_year)
# print(time.strftime('%c'))

# 时间的相互转换   --  不能直接从时间戳转格式化，要通过结构化中转
'''
时间戳->结构化：localtime、gmtime
结构化->时间戳：mktime

格式化->结构化：strptime
结构化->格式化：strftime
'''
# #时间戳->结构化：localtime、gmtime
# time_obj = time.localtime(1558494565)   #2019-05-22 11:09:25
#
# #结构化->格式化：strftime
# print(time.strftime('%Y-%m-%d %H:%M:%S',time_obj))
#
# #格式化->结构化：strptime
# struct_time = time.strptime('2019-05-22 11:09:25','%Y-%m-%d %H:%M:%S')
# print(time.strptime('2019-05-22 11:09:25','%Y-%m-%d %H:%M:%S'))
#
# #结构化->时间戳：mktime
# print(time.mktime(struct_time))


# 练习：获取本月1号的时间戳时间 1号0时0分0秒
# 1、结构化时间
local_time = time.localtime()
year = local_time.tm_year
month = local_time.tm_mon
struct_time = time.strptime('%s-%s-1'%(year,month),'%Y-%m-%d')
print(time.mktime(struct_time))

# 2、格式化时间
# ret = time.strftime('%Y-%m-1')
# struct_time = time.strptime(ret,'%Y-%m-%d')
# print(time.mktime(struct_time))


# # 1、获取当前时间
# year = time.localtime().tm_year
# mounth = time.localtime().tm_mon
# print(year,mounth)
# s = ''
# print(s)
# # 2、拼接一个结构化的时间
# # struct_time = time.strptime('','%Y-%m-%d %H:%M:%S')
# # stamp =





