sum=0
def func():
    global sum #gai xie
    print(sum)
    for i in range(5):
        sum+=1
    print(sum)


animal ='fruitbat'
def change_local():
    animal='wombat'
    print('locals:',locals())
