# 为什么要用？有什么用？用了什么？

# 你访问百度http://www.baidu.com?username = 'xxx',password = 'xxx'

# 检测一下客户端是否合法
# 不依靠登陆认证

# 借助模块hmac
# import hmac
# h = hmac.new()  # secret_key，你想进行加密的bytes
# h.digest()  # 密文的内容
# hmac.compare_digest()   #对比 密文和另外一个密文

import os
print(os.urandom(32))   #随机生成一个32位的字节