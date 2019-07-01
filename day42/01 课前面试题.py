# 去重，保持原来的顺序
l1 = [11, 2, 33, 7, 11, 8, 19, 1, 2]

# 通过集合去重
l2 = list(set(l1))
# print(l2)

# 保持顺序 按照原来的循序 排序 -> 索引
l2.sort(key=l1.index)
print(l2)

# ---------------------------------------
# 将l3中的元素按照age由小到大排序
l3 = [
    {"name": "sylar", "age": 88},
    {"name": "Gold", "age": 38},
    {"name": "Eva_J", "age": 18},
    {"name": "Alex", "age": 9000}
]

# 方法1：
ret = sorted(l3, key=lambda dic: dic['age'])
print(ret)

# 方法2：
l3.sort(key=lambda x: x['age'])
print(l3)

