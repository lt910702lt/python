def func():
    print("我是周杰伦")
    yield "昆凌"  #函数中包含了yield，当前这个函数就不再是普通的函数了，是生成器函数
    print("我是王力宏")
    yield "力宏"  #函数中包含了yield，当前这个函数就不再是普通的函数了，是生成器函数
    print("我是迪科尔基")
    yield "迪科尔"  #函数中包含了yield，当前这个函数就不再是普通的函数了，是生成器函数
g = func()  #通过函数func()来创建一个生成器
print(g.__next__())
print(g.__next__())

#return 直接返回结果，结束函数的调用
#yield 返回结果，可以让函数分段执行