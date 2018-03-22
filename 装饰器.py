def decorator(f):
    def new_f(x,y):
        print('参数1 为 %d,参数2为%d' % (x,y))
        return f(x,y)
    return new_f

@decorator
def add(x,y):
    return x+y
print(add(2,3))
