class Quote():
    def __init__(self,person,words):
        self.person=person
        self.words=words
    def who(self):
        return self.person
    def says(self):
        return self.words+'.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter =Quote('aaa',"I am one")
print( hunter.who() , 'says:' , hunter.says() )

hunted1=Quote('bbb',"I am tow")
print( hunted1.who() , 'says:' , hunted1.says() )


hunted2=Quote('ccc',"I am three")
print( hunted2.who() , 'says:' , hunted2.says() )

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook =BabblingBrook()

def who_says(obj):
    print(obj.who(),'--says--', obj.says() )

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)
