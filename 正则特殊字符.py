import string
import re
printable = string.printable
len(printable)
print(printable)
m=re.findall('\d',printable)
print(m)

m=re.findall('\D',printable)
print(m)

m=re.findall('\s',printable)
print(m)

