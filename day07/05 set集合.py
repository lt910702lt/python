# s = {'a'}
# print(type(s))

# s = {"王者荣耀", "英雄联盟", "王者荣耀", 123, True, True}
# # print(s)
# # s = {123, {1,2,3}}    # 不合法
# # print(s)

# lst = ["张强", "李强", "王磊", "刘伟", "张伟", "张伟", "刘洋", "刘洋"]
# print(lst)
# s = set(lst)        #去重复
# print(s)

## 1. 增加
# s = {"关之琳"}
# s.add("郑裕玲")  # 添加
# print(s)
# s.add("郑裕玲")  # 重复的内容不会添加
# print(s)
#
# s.update("马化腾")  # 迭代更新
# print(s)
# s.update(["张曼玉", "李若彤", "李若彤"])
# print(s)

## 2. 删除
# s.pop() #随机弹出一个
# s.remove("el")  #删除元素
# s.clear()

## 3. 修改    -- 先删除,再添加
# s.remove("刘嘉玲")
# s.add("赵本山")

## 4. 查询
# for el in s:
#     print(el)

## 5. 常用操作
# s1 = {"刘能", "赵四", "皮常山"}
# s2 = {"刘科长", "赵四", "冯乡长"}
#
# ##交集
# # print(s1 & s2)
# # print(s1.intersection(s2))
#
# #并集
# print(s1 | s2)
#
# #差集
# print(s1 ^ s2)

# 冻结了的set集合. 可哈希的. 不可变
# s = frozenset([1, 3, 6, 6, 9, 8])   # 可以去重复. 也是set集合
# print(s)
#
# ss = {"a", s}
# print(ss)
