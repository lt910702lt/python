'''
## 一、列表的增加
lst = ["周杰伦", "王力宏", "周润发"]
lst.append("伍佰")    # 向列表中添加一个元素, 元素放在末尾. 把一个元素追加到列表的末尾
print(lst)
lst.insert(1, "马化腾")    # 把元素插入到指定位置. 元素的移动
print(lst)

lst = []
while 1:
    name = input("请输入学生的名字:")
    if name.upper() == "Q":
        break
    else:
        lst.append(name)
print(lst)


## 二、列表的删除
lst = ["盖伦", "大白梨", "提莫", "人妖王"]

#2.1、pop()
e = lst.pop()   # 返回删除的元素, 删除最后一个
print(e)
print(lst)
e = lst.pop(1)  # 根据给出的索引进行删除
print(e)
print(lst)

#2.2、remove元素
lst = ["盖伦", "大白梨", "提莫", "大白梨"]
lst.remove("大白梨")   # 只会删除匹配到的第一个元素
print(lst)

#2.3、切片删除
lst = ["盖伦", "大白梨", "提莫", "大白梨"]
del lst[1:]
print(lst)


#2.4 clear 清空
lst = ["盖伦", "大白梨", "提莫", "大白梨"]
lst.clear()
print(lst)

## 三、修改
# 3.1、索引修改
lst = ["太白", "五色", "银王", "日天"]
lst[0] = "太黑"
print(lst)
# 3.2 、切片修改
lst[1:3] = "马化腾"    #迭代修改
print(lst)             #['太黑', '马', '化', '腾', '日天']


## 四、查询
lst = ["舒克贝塔", "黑猫警长", "熊大熊二", "葫芦娃", "吴佩琪"]
for el in lst:
    print(el)
'''

############常用操作###############
# 计算长度
lst = ["王尼玛", "我记着你", "伟哥", "放学天台见", "王尼玛", "王尼玛"]
print(len(lst))
print(lst.count("王尼玛"))

#排序（不要去排序字符串）
lst = [1, 9, 18, 2, 34, 88, 7, 9]
lst = ["2王尼玛", "马化腾", "1马云", "马云云", "阿里巴巴", "1王尼玛"]
lst.sort()  #升序
print(lst)
lst.sort(reverse=True)  # 倒序
print(lst)