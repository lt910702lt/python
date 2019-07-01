class Student:
    OPERATE_DIC = [
        ('查看课程信息', 'check_course'),
        ('选择课程', 'choose_course'),
        ('查看已选课程', 'choosed_course')
    ]

    def __init__(self, name):
        self.name = name

    def check_course(self):
        print('查看课程信息')

    def choose_course(self):
        print('选择课程')

    def choosed_course(self):
        print('查看已选课程')
