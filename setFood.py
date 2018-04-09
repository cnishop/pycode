allGuest={ 'zhangsan':{'apples':5,'banala':6},
            'lisi':{'pear':3,'banala':5},
            'wangwu':{'cups':3,'apples':6,'chicken':10}
}
def totalBrought(guests,item):
    numBrought=0
    for v in guests.values():
        numBrought +=v.get(item,0)
    return numBrought

foodSet =set()
#print(totalBrought(allGuest,'apples'))
for v in allGuest.values():
    foodSet|= set(v)
print("Number of things being brought:\n")
# print(foodSet)
for food in foodSet:
    print("-{:20}       {}".format(food,totalBrought(allGuest,food)))
