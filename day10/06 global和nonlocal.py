# a = 10
# def func():
#     # a = 20  #这是一个全新的变量a
#     # a = a + 10  #报错，a还没有初始化
#     global a    #把全局的a拽进来
#     a = a + 10
#     print(a)
# func()
# print(a)

# def func1():
#     a = 10
#
#     def func2():
#         nonlocal a  # 找局部作用域中，离他最近的那个变量引入进来
#         a = 20
#         print(a)
#
#     func2()
#     print(a)
#
#
# func1()

a = 1
def fun_1():
    a = 2
    def fun_2():
         def fun_3():
             nonlocal a
             a =  4
             print(a)
         print(a)
         fun_3()
         print(a)
    print(a)
    fun_2()
    print(a)
print(a)
fun_1()
print(a)

1
2
2
4
4
4
1