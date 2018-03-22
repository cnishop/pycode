def printse_series(d,*dtup):
    print('必须参数:',d)
    if len(dtup)!=0:
        print('元祖参数:',end=' ')
        for i in dtup:
            print(i,end=' ')
