def generator_even():
    for i in range(1,11):
        print('第%d 步' %i)
        yield i
g=generator_even()
print(g.__next__())
print(g.__next__())
print(g.__next__())
