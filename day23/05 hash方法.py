# hash方法
# 底层数据结构基于hash值殉职的优化操作
# hash是一个算法
# 能够某一个要存在内存里的值通过一系列的计算，
# 保证不同的值hash结果是不一样的
# 对同一个值在多次执行python代码的时候hash值是不同的
# 但是对同一个值，在同一次执行python代码的时候hash值永远不变
print(hash('abc'))  #6432891076546742161
print(hash('abc'))
print(hash('abc'))
print(hash('abc'))

# 字典的寻址 - hash算法
# d = {'key':'value'}
# hash - 内置函数

# set集合
se = {1,2,2,3,4,5,'a','b','d','f','f'}
print(se)
# 数据存入原理：
# 1、hash的结果找到一块内存地址
# 2、只要这块地址上没有数据，就说明之前没有重复数据
# 3、如果这块地址上有一个数据存在了，才判断这个值和要存的值是一样
# 4、如果一样，覆盖去重
# 5、如果不一样，二次寻址给这个值换个地方存

# hash(obj) # obj内部必须实现了hash算法