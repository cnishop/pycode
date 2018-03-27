def decorator(f):
    def new_f(x,y):
        print('参数1 为 %d,参数2为%d' % (x,y))
        return f(x,y)
    return new_f

@decorator
def add(x,y):
    return x+y
print(add(2,3))


import time

def deco(func):
    def wrapper():
        stratT= time.time()
        func()
        endT=time.time()
        msecs =(endT-stratT)*1000
        print("is's %f ms " % msecs)
    return wrapper

@deco
def myfunc():
    print('myfunc start....')
    time.sleep(2)
    print('myfunc end......')

print("myfunc is ",myfunc.__name__)
#myfunc= deco(myfunc)
print('#'*50)
print("myfunc is ",myfunc.__name__)
myfunc()


