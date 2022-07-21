class parent :
    def func1(self):
        print("This is a function")
class child(parent):
    def func2(self):
        super().func1()
        print("This is a function")
ob=child()
ob.func2()
