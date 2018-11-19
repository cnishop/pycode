class Duck():
    def __init__(self,input_name):
        print('init')
        self.hidden_name=input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self,input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name=property(get_name,set_name)

class Duck2(): #用装饰器实现
    def __init__(self,input_name):
        print('init')
        self.hidden_name=input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.hidden_name = input_name

class Duck3(): #用装饰器实现  _name  aa._Duck3__name
    def __init__(self,input_name):
        print('init')
        self.__name=input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.__name = input_name

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_socre(self):
        print('%s:%s' % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

bart = Student('Bart Simpson', 59)
bart.get_name()
bart.print_socre()
bart.__name="ggg"    #注意不能这样写，相当月创建了一个新的变量
bart.print_socre()
print(bart._Student__name)
print(bart.__name)


class MyObject():
    def __init__(self):
        self.x=0
    def power(self):
        return self.x*self.x

obj = MyObject()
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
setattr(obj, 'y', 19)
print(getattr(obj, 'y') )
print(getattr(obj,'y') )

##实例属性和类属性
class Student(object):
    name = 'Student'
    __slots__ = ('score', 'age')  # 用tuple定义允许绑定的属性名称 __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
s = Student() # 创建实例s
s.score = 90  #动态绑定属性
print(s.score)
print(s.name)
print(Student.name) # 打印类的name属性
s.name = 'Michael' # 给实例绑定name属性
print(s.name)
print(Student.name) # 打印类的name属性
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(24)
print(s.age)
Student.set_age = set_age
s2=Student()
s2.set_age(99)