##引用赋值
# lst1 = ["金毛狮王", "紫衫龙王", "白眉鹰王", "青衣服往"]
# lst2 = lst1  # 列表, 进行赋值操作. 实际上是引用内存地址的赋值. 内存中此时只有一个列表. 两个变量指向一个列表(硬链接)
#
# lst2.append("杨左使")
# print(lst2)
# print(lst1)
#
# print(id(lst1), id(lst2))

# 浅拷贝 copy 创建新对象
# lst1 = ["赵本山", "刘能", "赵四"]
# lst2 = lst1.copy()
# #lst2 = lst1[:]  #这也是浅拷贝的一种方法
# print(id(lst1), id(lst2))       #lst2和lst1不是一个对象了2172908102280 2172908102344
# lst1.append("谢大脚")
# print(lst1, lst2)

# 深拷贝 copy.deepcopy()
# lst1 = ["超人", "七龙珠", "葫芦娃", "山中小猎人", ["金城武", "王力宏", "渣渣辉"]]
# lst2 = lst1.copy()
#
# lst1[4].append("大秧歌")     #两个lst的结果还是一致的
# print(lst1, lst2)

import copy
lst1 = ["超人", "七龙珠", "葫芦娃", "山中小猎人", ["金城武", "王力宏", "渣渣辉"]]
lst2 = copy.deepcopy(lst1)  #把lst1扔进去进行深度拷贝 , 包括内部的所有内容进行拷贝
lst1[4].append("大秧歌")
print(lst1, lst2)

# 为什么要有深浅拷贝
# 拷贝比创建对象的过程要快(做作业和抄作业)