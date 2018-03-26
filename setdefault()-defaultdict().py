p1={'a':1,'b':2}
print(p1)

p1_a=p1.setdefault('c',12)
print(p1)


print('----------')
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['a','a','b','a']:
    food_counter[food]+=1

for food,count in food_counter.items():
    print(food,count)
print(food_counter)
