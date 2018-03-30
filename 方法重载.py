class MyList:
    __mylist=[]

    def __init__(self,*args):
        self.__mylist=[]
        for arg in args:
            self.__mylist.append(arg)

    def __add__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i]=self.__mylist[i] + x
        print(self.__mylist)

    def show(self):
        print(self.__mylist)

l=MyList(1,2,3,4,5)

print(l)
l.show()

l+10
        
