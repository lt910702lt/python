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
