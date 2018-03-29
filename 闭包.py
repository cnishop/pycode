def outer(x):
    def inner(y):
        return x+y
    return inner

f=outer(5)
print(f(20))

print("---------")

def hello_conf(prefix):
    def hello(name):
        print(prefix,name)
    return hello

a=hello_conf('Good Moring!')
a('milo')
