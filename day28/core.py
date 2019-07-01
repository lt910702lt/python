import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    #datefmt='%a, %d %b %Y %H:%M:%S',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='test.log',
                    filemode='w')
class Manager:
    def __init__(self,name):
        self.name = name
    def create_student(self):
        stu_name = input('Student_name:')
        '''输入一系列事件，创造了一个学生'''
        logging.info('%s create student %s' %(self.name,stu_name))

alex = Manager('alex')
alex.create_student()
