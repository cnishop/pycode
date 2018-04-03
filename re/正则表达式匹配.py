import re
source = 'Young Frankenstein'
m=re.match('You',source)
if m:
    print(m.group())

m=re.search('Frank',source)
if m:
    print(m.group())

m=re.findall('n',source)
print('Found',len(m),'matches')

m=re.findall('n.',source)
print(m)
m=re.findall('n.?',source)
print(m)

m=re.split('n',source)
print(m)

m=re.sub('n','?',source)
print(m)

