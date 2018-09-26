def outer(x):
    def inner(y):
        return x+y
    return inner

f=outer(5)
print(f(6))
#print(f(20))

print("---------")

def hello_conf(prefix):
    def hello(name):
        print(prefix,name)
    return hello

a=hello_conf('Good Moring!')
print(a.__name__)
print(id(a))
a('milo')
a('zouqixian')

b=hello_conf('Good Afternoon!')
print(b.__name__)
print(id(b))

print('---------')

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
        print(fs)
    return fs

f1,f2,f3 =  count()
print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
