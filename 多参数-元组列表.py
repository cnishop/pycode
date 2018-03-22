l=[5,'巧克力']
x={'x':7,'y':'巧克力'}
def machine(x=5,y='奶油',*arg,**kv):
    print('制作一个 %d 元的 %s 味道的冰激凌'%(x,y))
    print('arg:',arg)
    print('kv:',kv)

#machine(*l)
#machine(**x)

machine(y=5,x=3,z=7)
