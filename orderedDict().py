quotes={
    'Moe':'A wise guy,huh',
    'Larry':'Ow',
    'Curly':'Nyuk nyuk',
    }
for stooge in quotes:
   print(stooge)


from collections import OrderedDict
quotes=OrderedDict([
    ('Moe','A wise guy,huh'),
    ('Larr,y','Ow'),
    ('Curly','Nyuk nyuk'),
    ])

for stooge in quotes:
   print(stooge)
