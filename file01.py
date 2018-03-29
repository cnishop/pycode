poem='''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

import os
os.chdir('d:\\python')
f=open('test.txt','wt')
f.write( poem)
print(len(poem))
f.close()



f=open('test.txt','rt')
bdate=f.read()
leng= len(bdate)
print(leng)
f.close()


fin=open('test.txt','rb')
fin.seek(254,0)
fin.tell()
