class Person():
    def __init__(self,name):
        self.name= name

class MDPerson(Person):
    def __init__(self,name):
        self.name= name

class JDPerson(Person):
    def __init__(self,name):
        self.name= name

ss=JDPerson('aaa')
print(ss.name)