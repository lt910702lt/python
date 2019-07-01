# time
    # 时间的格式：时间戳、结构化、格式化
    # 时间戳：time.time()
        # -> 结构化：
    # 结构化：time.localtime()
        # -> 时间戳：mktime
    # 格式化：time.strftime()
        # ->结构化：strptime
# sys
    # path
    # argv
    # modules   #system.modules[__main__] , 反射自己的内容
    # exit()

# os
    # mkdir/rmdir/makedirs/removedirs/listdir
    # remove/rename
    # path: join/split/basename/dirname/abspath/isdir/isfile
    # system popen  #执行操作系统的命令

# 序列化
    # 把其他格式的数据转化成字符串
    # 网络传输、写文件
    # json  字典、字符串、字典、列表
        # 能处理的类型：有限、限制比较多
        # 能使用的语言：所有语言
        # 方法：dump/load、dumps/loads