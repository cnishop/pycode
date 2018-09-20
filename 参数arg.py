def buggy(arg,result=[]):
    'aaaaaaaa'
    result.append(arg)
    print(result)

def works(arg):
    result=[]
    result.append(arg)
    return result

def print_more(r1,r2,*args):
    print('1-----',r1)
    print('2-----',r2)
    print('all the rest:',args)

def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)

buggy(123,[1,2])

