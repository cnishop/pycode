'''
Heroes beta-0.2-1
'''
import os
welcome = 'welcome to Heroes world!'

i=0
while True:
    if os.path.isfile('locked.log'):
        print('has been locked')
        break
    
    username =input('login:')
    password =input('password:')

    i+=1
    if username=='milo' and password =='123':
        pass
    else:
        if i==3:
           # print('locked')
           open('locked.log','w').write(username)
           print('locked by %s' %username)
           break
        continue
    print(welcome)
