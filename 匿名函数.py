from functools import reduce

def f(x,y):
    return x+y

a=reduce(f,[1,2,3,4,5])
print(a)

print('\n----------------')

ff=lambda x,y:x+y

b=reduce(lambda x,y:x+y,[1,2,3,4,5])
print(b)
