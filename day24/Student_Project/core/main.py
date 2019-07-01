import sys
from core import auth
from core import student
from core import manager


def entry_point():
    print('欢迎进入学生选课系统')
    usr, id = auth.login()
    print('usr,id : ', usr, id)

    file = sys.modules['__main__']
    cls = getattr(file, id)
    obj = cls(usr)
    operate_dic = cls.OPERATE_DIC

    while True:
        for num, i in enumerate(operate_dic, 1):
            print(num, i[0])
        choice = int(input('num >>>'))
        choice_item = operate_dic[choice - 1]
        getattr(obj, choice_item[1])()


if __name__ == '__main__':
    entry_point()
