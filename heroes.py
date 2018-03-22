'''
Heros beta-0.1
2018-03-17
'''
hp=100
print('welcome heros world!')
print('input your name:')
name = input()
if not name:
    name='player01'
usermsg=[name,hp]
print("your hero's name is:",usermsg[0],'Hp is:',usermsg[1])
print("and now you are here:*#### | 'a'for left,'d' fro right |")

userinput= input()
if userinput=='d':
    print("you are here #*###")
if userinput=='a':
    print("you are here *####")
 
