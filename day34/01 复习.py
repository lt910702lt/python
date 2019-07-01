# 网络编程
# 互联网协议 -- 七层：osi协议
# 五层
# 应用层   python
# 传输层   tcp/udp
# 网络层   ip
# 数据链路层 arp
# 物理层
# 交换机：广播、单播、组播
# ip协议：规定了ip地址的格式
    # ip地址 一台机器在一个网络内唯一的标识
    # 子网掩码 ip地址与子网掩码做按位与运算，得到的结果是网段
    # 网关ip 局域网内的机器访问公网ip，就通过网关访问
# tcp 面向流的，可靠   全双工 三次握手、四次挥手 -- 黏包
# udp 面向数据包 不可靠

# 黏包
# 什么是黏包？
# 怎么解决？
    # 在发送信息之前，先告诉对方要发的数据有多大
    # struct模块将要发送的数据的大小固定化，无论如何就发4个字节
    # 自定义协议的概念

# 处理并发问题
# socketserver

# 验证客户端的合法性 hmac

# 并发编程