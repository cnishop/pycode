import re
r1=r"\d{3,4}-?\d{8}"
p_tel = re.compile(r1)

p_tel.findall("010-12345678")

csvt=re.compile(r'csvt',re.I)
csvt.findall('CSVT')
csvt.findall('csvt')
x= csvt.match('csvt hello')  #匹配开头位置\
x.group()
csvt.search('csvt hello') 

x= csvt.finditer('csvt hello csvt ')

s="hello csvt"
s.replace('csvt','python')

