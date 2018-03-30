##import csv
##villains=[
##    ['Doctor','No'],
##    ['Rosa','Klebb'],
##    ['Mister','Big'],
##    ['Auric','GoldFinger'],
##    ['Ernst','Blofeld'],
##    ]
##
##with open ('villains.txt','wt') as fout:
##    csvout =csv.writer(fout)
##    csvout.writerows(villains)
##
##
##
##with open ('villains.txt','rt') as fin:
##    cin =csv.reader(fin)
##    vv=[row for row in cin]
##    print(vv)
##
##with open ('villains.txt','rt') as fin:
##    cin=csv.DictReader(fin,fieldnames=['first','last'])
##    villains=[row for row in cin]
##    print(villains)


import csv
villains=[
    {'first':'Doctor','last':'No'},
    {'first':'Rosa','last':'Klebb'},
    {'first':'Mister','last':'Big'},
    {'first':'Auric','last':'GoldFinger'},
    {'first':'Ernst','last':'Blofeld'},
    ]

with open ('villains.txt','wt') as fout:
    cout =csv.DictWriter(fout,['first','last'])
    cout.writeheader()
    cout.writerows(villains)

with open ('villains.txt','rt') as fin:
    cin =csv.DictReader(fin)
    vv=[row for row in cin]
    print(vv)






