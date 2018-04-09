import os
os.chdir('d:\\python')
f=open('test.txt')
poem=f.read()
print(poem)
print(f.closed)
f.close()

# with open('test.txt',mode='a') as fin:
#     fin.write('\n from f\n')
# print(fin.closed)

with open('test.txt',mode='r') as fin:
    print(fin.read())
