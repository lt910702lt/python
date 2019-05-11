# 递归函数，自己调用自己
# 查看递归的深度
# def func(count):        #996后报错！说明深度996？？最大是1000，但是无法达到
#     print("我是谁，我在那里" + str(count))
#     func(count + 1)
#
#
# func(1)

# 修改递归的深度
# import sys
# sys.setrecursionlimit(10000)    #设置递归的深度，但是不一定能跑到，可能几千就停止

##递归最大的作用：遍历树形结构
# 遍历树的伪代码
# def func(genjiedian):
#     left = genjiedian.leftNode()
#     right = genjiedian.rightnode()
#     func(left)
#     func(right)

# 遍历一个树形结构文件夹的内容
import os

filePath = "D:\学习\\05-python\python"  # 在05前面要\转移，否则格式报错


def read(filePath, n):
    it = os.listdir(filePath)
    for el in it:
        # 拿到路径
        fp = os.path.join(filePath, el)
        if os.path.isdir(fp):   #判断是否文件夹
            print('\t' * n, el)
            read(fp, n + 1)  # 又是文件夹，继续去读内容
        else:
            print('\t' * n, el) #递归的出口


read(filePath, 0)
