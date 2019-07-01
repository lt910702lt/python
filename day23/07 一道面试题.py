# 一个类
# 对象的属性 : 姓名 性别 年龄 部门
# 员工管理系统
# 内部转岗 python开发 - go开发
# 姓名 性别 年龄 新的部门
# alex None 83 python
# alex None 85 luffy

# 1000个员工
# 如果几个员工对象的姓名和性别相同,这是一个人
# 请对这1000个员工做去重
class Employment:
    def __init__(self,name,sex,age,department):
        self.name = name
        self.sex = sex
        self.age = age
        self.department = department
    def __hash__(self):
        return hash('%s%s' %(self.name,self.sex))
    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
Employment_lst = []
for i in range(100):
    Employment_lst.append(Employment('alex','boy',i,'python'))
for i in range(100):
    Employment_lst.append(Employment('wusir','boy',i,'python'))
for i in range(100):
    Employment_lst.append(Employment('nvshen','girl',i,'python'))
# print(Employment_lst)
s = set(Employment_lst)
for e in s:
    print(e.__dict__)