# 正则表达式
    # 基础知识
        # 什么是正则
        # 应用领域
    # 正则表达式的语法
        # 元字符
            # 字符组 [] [^] | ()
                # |的用法 [1-9]\d{16}[0-9X]|[1-9]\d{14}  身份证号
                # ()的用法 [1-9]\d{14}(\d{2}[1-9X])? 身份证号
                         # \d+(\.\d+)?  小数或者整数
            # \w \d \s(\n,\t, )  \W \D \S
            # ^ $
            # .
        # 量词
            # ? + *
            # {n},{n,},{n,m}
        # 特殊的用法和现象
            # ?的使用
                # 1. 在量词的后面跟了一个 ? 取消贪婪匹配 非贪婪(惰性)模式
                    # ?? \ *? \+? \ {n}?
                    # 李.{1,3}?和 李莲英和  惰性匹配 回溯算法
                    # 最常用  .*?x 匹配任意字符直到找到一个x
                # 2.

#匹配15位和18位的身份证
#[1-9]|\d{16}[0-9X]|[1-9]\d{14}
#[1-9]\d{14}(\d{2}[0-9X])?

#匹配小数或者整数
#\d+(\.\d*)?

# 总结
    # 元字符
    # 元字符量词   默认贪婪匹配
    # 元字符量词?  表示惰性匹配



# re模块
# 在python中使用正则表达式
    # 转义符：在正则中的转义符 \ 在python中的转义符
    # re模块
        # findall search match
        # sub subn split
        # compile finditer
    # python中的正则表达式
        # findall 会优先显示分组中的内容
        # split 遇到分组，会保留分组内被切掉的内容
        # search 如果search有分组的话，通过group(n)就能拿到group中匹配的内容

# 正则表达式进阶
    # 分组命名
        #(?P<name>正则表达式)表示给分组起名字
        #(?P=name)表示使用这个分组，这里匹配到的分组内容应该和分组中的内容完全相同
    # 通过索引使用分组
        # \1 表示使用第一组，匹配到的内容必须和第一个组中的内容完全相同











