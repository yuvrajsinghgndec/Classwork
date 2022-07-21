numbers = [3, 98, 7, 5, 67, 1]
print(numbers)
# this changes the original lists
numbers.append(6)
print(numbers)
numbers.remove(98)
print(numbers)
numbers.pop()
print(numbers)
numbers.insert(1, 60)
print(numbers)
numbers.extend([8, 17])  # to add a new list to a old list
print(numbers)
print(numbers[:5])  # slice operation
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(min(numbers))
list2 = [46, 76]
print(numbers+list2)
# tuples
print("print our tuple functions")
mytuple = (4, 8, 3, 9)
print(mytuple)
# print(mytuple.append(0))
# it will show an error
tp = (1)
print(tp)  # this will not give a tuple
# to get tuple of one element we will take ,after 1
tp1 = (4,)
print(tp1)  # this will give us tuple
# to swap two numbers
a = 12
b = 56
a, b = b, a
print(a, b)
