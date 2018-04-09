import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.basicConfig(filename='mulog.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
def factorial(n):
    logging.debug('start of factorial({})'.format(n))
    total =1
    for i in range(1,n+1):
        total *=i
        logging.debug('i is {},total is {}'.format(i,total))
    logging.debug('end of factorial({})'.format(n))
    return total
print(factorial(5))