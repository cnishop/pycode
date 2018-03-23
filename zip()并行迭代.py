days=['Monday','Tuesday','Wednesday']
fruits=['banana','orange','peach']
drinks=['coffee','tea','beer']
desserts=['tiramisu','ice cream','pie','pudding']

for day,fruit,drink,dessert in  zip(days,fruits,drinks,desserts):
    print(day,fruit,drink,dessert)

print('------------')
aa=list(zip(days,fruits))
print(aa)

bb=dict(zip(days,fruits))
print(bb)

print('------------')
aa=list(range(2,-1,-1) )
print(aa)
