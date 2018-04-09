import re
s='abc'
s=r'abc'
re.findall(s,"abcaaaaabacaaaaa")

m=re.search('^(\d{3})-(\d{3,8})$','021-81870936')
#print(m)
print(m.group())

