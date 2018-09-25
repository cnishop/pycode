#必选参数、默认参数、可变参数、关键字参数和命名关键字参数

def printse_series(d,*dtup):
    print('必须参数:',d)
    if len(dtup)!=0:
        print('元祖参数:',end=' ')
        for i in dtup:
            print(i,end=' ')
num0=(1,2,3)
printse_series(111,*num0)

print('-----')

#关键字参数
num=[2,3,4]
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

print(calc(1,2,3))
list1=[1,2,3]
print(calc(*list1))



#命名关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

#print(person('guo',30))
#print(person('guo',30,city='beijing'))
#print(person('Adam', 45, gender='M', job='Engineer'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('guo',30,**extra))

#限定参数
def person1(name, age, *, city, job):
    print(name, age, city, job)
print(person1('guo',30,city='beijing',job='it'))

def person2(name, age, *args, city, job):
    print(name, age, args, city, job)
person2('Jack', 24,1,2, city='Beijing', job='Engineer')
