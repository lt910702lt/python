'''
1.谈谈你对面向对象的理解？
    对象 = 数据 + 方法
2.Python面向对象中的继承有什么特点？
    多继承

3.面向对象的深度优先和广度优先是什么？
4.面向对象中super的作用？
    在子类中执行父类的方法
5.列举面向对象中的特殊成员（带双下划线的特殊方法,如：__new__、__init__、__call__等）
    __new__(): 开辟空间，创建对象
    __init__(): 初始化对象，对象属性赋值
    __call__(): 对象()直接执行的代码
    __str__(): print(对象)时执行的
    __repr__(): 解释器环境下直接输入对象展示的内容
    __len__(): len()
    __hash__():
    __eq__();
    __setitem__():
    __getitem__():
6.静态方法和类方法的区别？

'''


class Person(object):
    name = "黄袍怪！"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def yongshou():
        print("不可调用。。。")

    @classmethod
    def haiyongshou(cls):
        '''
        修改静态属性
        cls.name = "嘤嘤"
        :return:
        '''
        print("再次不可描述。。。")
        cls.name = "嘤嘤"
        print(cls.name)
    @property
    def age(self):
        return "本是同根生，相煎何太急！"

p1 = Person("CC")
# Person.yongshou()
# Person.haiyongshou()
p1.yongshou()
p1.haiyongshou()
print(p1.age)

