###第一题: 判断一个数是否是水仙花数. 水仙花数是一个三位数,三位数的每一位的三次方的和还等于这个数,那这个数就是一个水仙花数.
# 例如: 152 = 1**3+5**3+3**3
# #我的代码
# count = input("请输入一个三位数:")
# sum = 0
# for n in count:
#     sum = sum + int(n)**3
# if sum == int(count):
#     print("是")
# else:
#     print("不是")
# #老师的代码
# n = input("请输入一个三位数:")  # 156
# s = int(n[0])**3 + int(n[1])**3 + int(n[2]) ** 3
# if int(n) == s:
#     print("是水仙花")
# else:
#     print("不是")

###第二题: 给出一个纯数字列表,请对列表进行排序(升级题)
# 1. 交换
# 2. 移动
# 3. 重复
# 思路: 1.完成a和b的数据交换.例如a=10,b=24 交换后 a=24,b=10; 2. 循环列表,判断a[i]和a[i+1]的大小关系,如果a[i]比a[i+1]大,
# 则进行互换. 循环结束的时候,当前列表中最大的数据就会被移动到最右端;
# lst = [22, 33, 11, 6, 9, 98, 123]
# for a in range(len(lst)):   #记录内部排序的次数
#     i = 0
#     while i < len(lst)-1:       #把最大值移动到右端
#         if lst[i] > lst[i + 1]:  # 前面比后面大,互换
#             lst[i], lst[i + 1] = lst[i + 1], lst[i]
#         i += 1
# print(lst)

###第三题: 完成彩票36选7的功能. 从36个数中随机产生7个数,最终获取到7个不重复的数据作为最终的开奖结果
# 随机数
from random import randint

randint(0, 20)  # 0-20的随机数
s = set()
while len(s) < 7:
    s.add(randint(1, 36))
print(s)

