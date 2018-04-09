import random
numList = []
for i in range(5):
    numList.append(random.randrange(1,9))
print(numList)
# numList.sort()
# print(numList)

# numList.reverse()
# print(numList)

# numList.insert(4,10)
# print(numList)
# numList.remove(4)
# print(numList)
print(sorted(numList))
print(numList)
print(numList[1])