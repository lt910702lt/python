class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
a = A('alex',83)
aa = A('alex',83)
aaa = A('alex',83)
print(a,aa)
print(a == aa == aaa)   # ==这个语法，是完全和__eq__

