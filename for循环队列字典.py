dl=['a','b','c','d','e']
for d in dl:
    print(d)

ac={'room':'a','wapon':'b','person':'col'}
for key in ac:   #or ac.keys
    print(key)

for k in ac.keys():
    print('keys:', k,ac[k])

for value  in ac.values():
    print(value)

for item in ac.items():
    print(item)

for name,contents in ac.items():
    print('name:',name,'contents:',contents)


money = 500000
rate=0.05
for i in range(10):
    print(i)
    money = money + money* rate
print("money: " ,money)

