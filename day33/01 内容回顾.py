# 解决黏包问题
    # 首先只有在TCP协议种才会出现黏包现象
    # 是因为tcp协议是面向流的协议
    # 在发送数据传输的过程种，还有缓存机制来避免数据丢失
    # 因此，在连续发送小数据的时候，以及接收大小不符的时候都容易出现黏包现象
    # 本质还是因为我们在接收数据的时候不知道发送数据的长短
# 解决黏包问题
    # 本质上是在传输大量数据之前，先告诉接收端发送数据的大小
    # 想更漂亮的问题，可以通过struct模块来定制协议

# strcut模块
    # pack unpack
    # 模式：'i'
    # pack之后的长度：4个字节
    # unpack之后拿到的是一个元组，元组的第一个元素才是pack的值
