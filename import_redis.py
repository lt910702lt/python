import sys

import redis


# 迁移hash
def moveHash(cursor):
    cursor, data = r.hscan(key, cursor)
    for eachKey in data:
        rNew.hset(key, eachKey, data[eachKey])
    print(key, "---处理了---", len(data), '个')
    if cursor != 0:
        print(cursor, "批处理")
        moveHash(cursor)
    else:
        print(cursor, "处理完成了")


# 迁移list
def moveList():
    length = r.llen(key)
    if length == 0:
        print(key, "---list迁移结束---剩余长度", length)
    else:
        # 每次迁移一千个
        start = length - 1000;
        if start < 0:
            start = 0
        data = r.lrange(key, start, -1)
        pl = r.pipeline();
        for eachI in data:
            setAdd = r.sadd("ordernokey_move", eachI);
            if setAdd == 1:
                pl.rpush("aaaaaaa", eachI)
            else:
                print("迁移的key的值重复了", eachI)
        pl.execute()
        if start == 0:
            # 清空
            r.ltrim(key, 1, 0)
        r.ltrim(key, 0, start - 1)
        moveList()


############################


key = sys.argv[1]

print('输入的key是：' + key)
# ip = '47.254.149.109'
# password = 'Kikuu2018'

ip1 = '192.168.1.78'
# password1 = 'kikuu2018'

ip2 = '192.168.1.129'
# password2 = 'kikuu2018'

# 连接redis
r = redis.Redis(host=ip1, password=password1, port=6379, db=0,
                decode_responses=True)
r = redis.Redis

# 连接redis  带接收的库
rNew = redis.Redis(host=ip2, password=password2, port=6379, db=0,
                   decode_responses=True)

keyType = r.type(key)

if keyType == 'string':
    rNew.set(key, r.get(key))
    print("key=" + key + "迁移到新库")

if keyType == 'hash':
    cursor = r.hlen(key)
    print(" key值长度是 + ", cursor)
    moveHash(0)

if keyType == 'list':
    moveList()