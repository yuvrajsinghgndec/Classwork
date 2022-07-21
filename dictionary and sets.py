dict = {"rakesh": "burger", "vicky": "soup", "rohan": "chicken"}
print(dict)
dict.update({"abhay": "mutton"})
print(dict)
del dict["abhay"]
print(dict)
dict["honey"] = "dal"
print(dict)
del dict["honey"]
print(dict)
dict1 = dict.copy()
print(dict1)
print(dict.keys())
print(dict.items())  # keys with items
# print(dict.popitem())  # return and removes key value pair
# print(dict.values())
print(dict.pop("rakesh"))
print(dict)
print(dict.clear())  # clears our dictionary
#  sets
print("operations on sets")
my_set = {13, 53, 78, 15, 6}
print(my_set)
# set of mixed data types
# my_set2 = {"hello", (2, 4, 1, 9), 5.8 }
# print(my_set2)
my_set3 ={3, 4, 3, 6, 2, 4}
print(my_set3)  # set cannot have duplicates
my_set.add(92)
print(my_set)
my_set.remove(92)
print(my_set)
""" my_set.pop()
print(my_set)"""  # multiline comments
print(type(my_set))
my_set.update([8, 78])
print(my_set)
my_set.discard(8)
print(my_set)
# print(my_set-my_set3)  # set difference
print(my_set.isdisjoint(my_set3))
my_set4 = frozenset([4, 5, 2, 9])
print(my_set4)
# my_set4.add(1) shows error as we cannot change value in frozen set
# print(my_set4)
