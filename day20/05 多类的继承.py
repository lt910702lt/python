'''
多类的继承：
    1、LB的深度[B,D,F,H]
    2、LC的深度[C,E,G,H]
    3、LD的深度[D,F,H]
    4、LA的广度[B,C,D]

    首部和尾部：
        1、提取第一个的首部，如果其他的尾部没有这个首部值，那么直接提取出这个首部值
        2、如果有这个首部值，那么获取那个L的首部，再按1来计算
过程如下：
第一步：[B,D,F,H]  [C,E,G,H] [D,F,H] [B,C,D]        #获取深度和广度
第二步：[D,F,H] [C,E,G,H] [D,F,H]  [C,D]            #提取出[B]
第三步：[D,F,H] [E,G,H] [D,F,H]  [D]                #提取出[B，C]
第四步：[F,H] [E,G,H] [F,H]  []                     #提取出[B，C，D]
第五步：[H] [E,G,H] [H]  []                         #提取出[B，C，D，F]
第六步：[H] [G,H] [H]  []                           #提取出[B，C，D，F，E]
第七步：[H] [H] [H]  []                             #提取出[B，C，D，F，E，G]
第八步：[] [] []  []                                #提取出[B，C，D，F，E，G，H]     --最终结果
'''



class H:
    def func(self):
        print("in H")


class G(H):
    def func(self):
        print("in G")


class F(H):
    def func(self):
        print("in F")


class E(G):
    def func(self):
        print("in E")


class D(F):
    def func(self):
        print("in D")


class C(E):
    def func(self):
        print("in C")


class B(D):
    def func(self):
        print("in B")


class A(B, C, D):
    def func(self):
        print("in A")

a = A()
print(A.mro())

#[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class '__main__.E'>, <class '__main__.G'>, <class '__main__.H'>, <class 'object'>]
#A B C D F E G H O