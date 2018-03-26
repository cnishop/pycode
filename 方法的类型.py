class A():
    count=0  #会累加
    def __init__(self):
        A.count +=1
    def exclaim(self):
        print('I am A')
    @classmethod
    def kids(cls):
        print("A has:",cls.count," little Objects")
    def kidss():
        print("A has new:", A.count," objs")

    @staticmethod
    def statichaha():
        print("static method")    
a =A()
b =A()
c =A()

A.kids()
A.kidss()
A.statichaha()
