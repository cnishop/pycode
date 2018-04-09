a_list = ["abc","def","hello","world"]
print(" ".join(a_list))
print("-".join(a_list))

str=input("conver to acronym:")
str=str.upper()
listOfWords = str.split()
for word in listOfWords:
    print(word[0],end='')

