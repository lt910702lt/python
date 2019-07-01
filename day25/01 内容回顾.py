# 模块
    # import 模块
    # from 模块名 import 名字
    # __name__ == '__main__',当前文件被导入，name是自己的模块名
    # sys.path
        # 一个模块能不能被导入，就看sys.path中是否有这个模块所在的路径
        # 导入不成功：
            # 1. 修改sys.path
            # 2. 修改import语句
    # 不能循环导入

# 包 #导入的包的开始的包也必须在sys.path路径中
    # 从包里导入模块
        # 1. import 包.包...模块
        # 2. from import    包.包...模块
    # 直接导入包
        # 相当于执行了__init__.py
        # __init__.py文件中做一些导入设置，才能保证导入包的时候使用这些包的模块

