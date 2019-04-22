names = ['Michael', 'Bob', 'Tracy']
names.append('aaaa')
print(names)
d=dict.fromkeys(names,"aaa")
print(d)

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
if 95 in d :
    print("aa")
if ('Bob',75) in d:
    print("bob")

i=d.items()
print(i)
print(d.get('Bob',100))
print(d["Bob"])

s = set([1, 1, 2, 2, 3, 3])
s.add(4)
print(s)

