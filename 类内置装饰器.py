from decimal import Decimal

class Fees(object):
    def __init__(self):
        self.__fee=None

    @property
    def fee(self):
        return self.__fee

    @fee.setter
    def fee(self,value):
        if isinstance(value,str):
            self.__fee=Decimal(value)
        elif isinstance(value,Decimal):
            self.__fee=value

if __name__=="__main__":
    f=Fees()
    f.fee = "10"
    print(f.fee)
