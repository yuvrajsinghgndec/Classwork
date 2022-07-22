class base:
    def __init__(self):
        self._a = 2   # protected member of a class


class derived(base):
    def __init__(self):
        base.__init__(self)
        print("calling protected member", self._a)
        self._a=3
        print("modified value =",self._a)


obj1 = derived()
obj2 = base()
print("accessing protected member of base class", obj1._a)
print("accessing changed value of base class", obj2._a)

