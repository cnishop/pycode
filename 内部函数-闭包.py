def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)

def knight(saying):
    def inner(quote):
        return "we are the knights innner say :%s" % quote
    return inner(saying)    

def knight2(saying):
    def inner2():
        return "we are the knights innner say :%s" % saying
    return inner2    
