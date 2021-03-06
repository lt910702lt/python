# 用列表推倒式做如下题目
# 1. 过滤到长度小于3的字符串列表，并将剩下的转换成大写字母
# lst = ["aaaaa", "bb", "ccc", "ddddd"]
# lst_new = [e.upper() for e in lst if len(e) >= 3]
# print(lst_new)

# # 2. 求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元组列表
# lst = [(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y % 2 == 1]
# print(lst)

# 3. 求M中3,6,9组成的列表M = [[1,2,3,],[4,5,6],[7,8,9]]
# M = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]]
# print([i[2] for i in M])
# M = [3, 6, 9]
# print([[i - 2, i - 1, i] for i in M])

# 4. 求50以内能被3整除的数的平方
# print([n**2 for n in range(50) if n % 3 == 0])

# # 5. 构建一个列表:['python1期','python2期','python3期','python4期','python5期','python6期']
# print(["python%d期" % i for i in range(1, 7)])
#
# # 6. 构建一个列表：[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]
# print([(x, x + 1) for x in range(6)])

# # 7. 构建一个列表：[0,2,4,6,8,10,12,14,16,18]
# print([i for i in range(16) if i % 2 == 0])

# # 8. 有一个列表：l1 = ['alex', 'WuSir', '老男孩', '太白']，将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# print([l1[i] + str(i) for i in range(len(l1))])

# 9. 有以下数据类型，
x = {
    'name': 'alex',
    'Values': [{'timestamp': 1517991992.94, 'values': 100, },
               {'timestamp': 1517992000.94, 'values': 200, },
               {'timestamp': 1517992014.94, 'values': 300, },
               {'timestamp': 1517992744.94, 'values': 350},
               {'timestamp': 1517992800.94, 'values': 280}
               ], }
# 通过推倒式，变成下面的类型：[[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
print([[el['timestamp'], el['values']] for el in x['Values']])
