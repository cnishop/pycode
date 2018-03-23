dl=['a','b','c','d','e']
for d in dl:
    print(d)

ac={'room':'a','wapon':'b','person':'col'}
for key in ac:   #or ac.keys
    print(key)

for value  in ac.values():
    print(value)

for item in ac.items():
    print(item)

for name,contents in ac.items():
    print('name:',name,'contents:',contents)
