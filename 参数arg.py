#必选参数、默认参数、可变参数、关键字参数和命名关键字参数

#必选参数
def buggy(arg,result=[]):
    'aaaaaaaa'
    result.append(arg)
    print(result)
def works(arg):
    result=[]
    result.append(arg)
    return result
print('必选参数:', works(1111))

#默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print('默认参数:', power(4))


#可变参数
def printse_series(d,*dtup):
    print('必须参数:',d)
    if len(dtup)!=0:
        print('元祖参数:',end=' ')
        for i in dtup:
            print(i,end=' ')

num=[2,3,4]
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print('可变参数：',calc(*num))


#关键字参数
def person(name,age,**kw):
    print('关键字参数：name:',name,'age:',age,'other:',kw)
#print(person('guo',30))
#print(person('guo',30,city='beijing'))
#print(person('Adam', 45, gender='M', job='Engineer'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('guo',30,**extra)

#命名关键字参数 #限定参数
def person1(name, age, *, city, job):
    print('命名关键字参数缺省 name', age, city, job)
person1('guo',30,city='beijing',job='it')

def person2(name, age, *args, city, job):
    print('命名关键字参数有可变参数 name', age, args, city, job)
person2('Jack', 24,1,2, city='Beijing', job='Engineer')

#组合参数
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)