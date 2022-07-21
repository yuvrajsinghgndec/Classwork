
#types of inheritance 
# single inheritance
# multiple inheritance
# multilevel inheritance 
# herirchical inheritance
# hybrid inheritance 


# single inheritance

class Parent:
def func1(self):
print("This function is in parent class.")


class Child(Parent):
def func2(self):
print("This function is in child class.")


object = Child()
object.func1()
object.func2()

# multiple inheritance

class Mother:
mothername = ""

def mother(self):
print(self.mothername)

class Father:
fathername = ""

def father(self):
print(self.fathername)

class Son(Mother, Father):
def parents(self):
print("Father :", self.fathername)
print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

# multilevel inheritance
class Grandfather:

def __init__(self, grandfathername):
self.grandfathername = grandfathername

class Father(Grandfather):
def __init__(self, fathername, grandfathername):
self.fathername = fathername
		
Grandfather.__init__(self, grandfathername)

class Son(Father):
def __init__(self, sonname, fathername, grandfathername):
self.sonname = sonname
	
Father.__init__(self, fathername, grandfathername)

def print_name(self):
print('Grandfather name :', self.grandfathername)
print("Father name :", self.fathername)
print("Son name :", self.sonname)


s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()


# Hierarchical inheritance

class Parent:
def func1(self):
print("This function is in parent class.")

class Child1(Parent):
def func2(self):
print("This function is in child 1.")

class Child2(Parent):
def func3(self):
print("This function is in child 2.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# hybrid inheritance


class School:
def func1(self):
print("This function is in school.")

class Student1(School):
def func2(self):
print("This function is in student 1. ")

class Student2(School):
def func3(self):
print("This function is in student 2.")

class Student3(Student1, School):
def func4(self):
print("This function is in student 3.")
object = Student3()
object.func1()
object.func2()
