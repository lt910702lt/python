# 正则模块
    # 转义符
        # 在小工具测试好之后再加 r' '
    # re模块
        #findall : 从头开始匹配
        #search : 从头到尾，只取第一个
        #match  : 从头开始匹配
        # sub subn split
        # compile finditer
    # 分组在re中的应用 取消分组的优先性（?:）
        # findall 优先显示分组中的内容
        # split 保留分组中的内容()
        # search 通过group(n)来按照分组的顺序来查看分组中匹配到的内容
    # 分组命名
        #（?P<分组名>正则表达式）
        # \m 通过转义数字m来获取m对应位置上的那个分组中的内容

# random
    # 随机小数
        # random
        # uniform
    # 随机整数
        # randint
        # randrange
    # 随机抽取
        # choice
        # sample
    # 打乱顺序
        # shuffle

# 验证码
# 发红包