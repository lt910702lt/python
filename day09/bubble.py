lst = [1, 8, 16, 2, 5, 7]
# 通过交换的方式,把列表中最大的值移动到最右端

for abc in range(len(lst)):  # 控制内部移动的次数
    n = 0
    while n < len(lst) - 1:         #判断两个元素的大小,大的往后移动
        if lst[n] > lst[n + 1]:
            lst[n], lst[n + 1] = lst[n + 1], lst[n]
        n += 1
print(lst)
