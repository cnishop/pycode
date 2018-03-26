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
