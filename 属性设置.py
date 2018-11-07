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