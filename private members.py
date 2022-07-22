class base:
    def __init__(self):
        self._a = "hello"
       # self.__c = "hello"

class derived(base):
    def __init__(self):
        base.__init__(self)
       # print("calling private member", self.__c)


obj1 = base()
print( obj1._a)
#print(obj1.__c)
