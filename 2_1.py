class MetaClass(type):
    def __init__(self, name, type):
        self.type = type
        self.name = name
        type.__name = type.name 
   
    @staticmethod
    def pretty_func():
        print('Some useful message')

    @classmethod
    def do_things(self):
        print(self.var)

class A(MetaClass):
    __var = 10
    def __init__(self, x):
        self.x = x

a=A(10)
print(a.var)
