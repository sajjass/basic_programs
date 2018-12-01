class Myclass(object):

    # Weak private variable ( With single Underscore)
    _singleUnderscoreVariable=0

    # Strong private Variable (With Double Underscore)
    __doubleUnderscoreVariable=0

    # Constructor
    def __init__(self):
       Myclass._singleUnderscoreVariable += 1
       Myclass.__doubleUnderscoreVariable +=1

    def printData(self):
       print "Single underscore: %d" % Myclass._singleUnderscoreVariable
       print "Instance variable: %d" % Myclass.__doubleUnderscoreVariable

if __name__ =="__main__":

   # Object 1 Created
   m_object = Myclass()

   # print data
   m_object.printData();

   # single underscore variable can be accessed
   # But it can't be imported
   print m_object._singleUnderscoreVariable