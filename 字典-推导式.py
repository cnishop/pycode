city_code ={"suzhou":"0512","tangshan":"0315","hangzhou":"0571"}
aa="suzhou is a beautifual city,its code is {suzhou}".format(**city_code)
print(aa)
b=city_code
c=city_code.copy()
b["suzhou"]="0513"
print(city_code)
print(b)
print(c)
print('1--------------')
x ={"name":"guo","lang":["python","java","c"]}
y=x.copy()
y["lang"].remove("c")
y["lang"].append("d")
print(x)
print(y)



word ='letters'
letter_count = {letter:word.count(letter) for letter in word}
print(letter_count)

print('2--------------')

#print(set(word))

ss= set(word)
letter_count = {letter:word.count(letter) for letter in ss}
print(letter_count)

