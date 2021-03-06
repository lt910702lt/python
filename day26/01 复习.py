# 正则表达式
# 作用: 一种匹配字符串的规则
# 应用: 登陆注册的表单验证、爬虫、自动化开发、日志分析

# 元字符
    # [] [^]    个性化的定制
        # [1-9]下面这一组无法描述的一般用上面字符组的形式
        # [\d\s]一个特殊元字符无法表述一个字符内出现的内容
    # \d \D \w \W \s \S \t \n
    # .         匹配除了换行符之外的所有字符
    # ^ $
    # | ()

# 量词
    # *     0-n
    # +     1-n
    # ？    0-1
    # {n},{n,},{n,m}

#其他知识：
    # 贪婪匹配 - 回溯算法
    # 量词?    - 惰性匹配