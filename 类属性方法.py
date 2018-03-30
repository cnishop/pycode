class Human:
    '''
    this is doc
    '''
    name='ren'
    gender ='male'
    age='25'
    __money = 8000

    def __init__(self,name,age):
        print("#"*50)
        self.name=name
        self.age=age
        print("#"*50)
        self.var2  ="实例的属性"
        self.__var3 ="实例的私有属性"

    #def __str__(self):
        print("string")
    def say(self):
        print("my name is %s i have %d " % (self.name,self.__monye))

    def __lie(self):
        print("i have 5000")

zhangsan =Human('guo',30)
print(zhangsan,__doc__)
print(Human.__doc__)
print(zhangsan.var2)
