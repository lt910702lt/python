def fun(fn):
    def inner():
        print("1")
        ret = fn()
        return ret

    return inner


@fun
def hello():
    print("hello world")


hello()


# def fun(fn):
#     def inner(*args, **kwargs):
#         print('开始前')
#         ret = fn(*args, **kwargs)
#         print('开始后')
#         return ret
#
#     return inner
#
#
# @fun
# def yue(tools):
#     print('使用%s约一约' % tools)
#     return '成功了！'
#
#
# print(yue('陌陌'))
