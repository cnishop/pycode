def outer(x):
    def inner(y):
        return x+y
    return inner

f=outer(5)
print(f(20))
