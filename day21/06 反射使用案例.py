import sys


class Manager:
    OPERATE_DIC = [
        ('创建学生账号', 'create_student'),
        ('创建课程', 'create_course'),
        ('查看学生信息', 'check_student_info')
    ]

    def __init__(self, name):
        self.name = name

    def create_student(self):
        print('创建学生账号')

    def create_course(self):
        print('创建课程')

    def check_student_info(self):
        print('查看学生信息')


class Student:
    OPERATE_DIC = [
        ('查看课程信息', 'check_course'),
        ('选择课程', 'choose_course'),
        ('查看已选的课程', 'choosed_course')
    ]

    def __init__(self, name):
        self.name = name

    def check_course(self):
        print('查看课程信息')

    def choose_course(self):
        print('选择课程')

    def choosed_course(self):
        print('查看已选的课程')


def login():
    username = input('user : ')
    password = input('pwd : ')
    with open('userinfo', mode='r', encoding='utf-8') as f:
        for line in f:
            user, pwd, ident = line.strip().split('|')
            if user == username and pwd == password:
                print('登录成功')
                return username, ident


def main():
    usr, id = login()
    print('usr,id : ', usr, id)
    file = sys.modules['__main__']
    cls = getattr(file, id)
    obj = cls(usr)
    operate_dit = cls.OPERATE_DIC
    while True:
        for num, i in enumerate(operate_dit, 1):
            print(num, i[0])
        choice = int(input('num >>>'))
        choice_item = operate_dit[choice - 1]
        getattr(obj, choice_item[1])()


main()
