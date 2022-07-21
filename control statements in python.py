# if else statement
a = 14
b = 20
if a < b:
    print("a is smaller than b")
else:
    print("b is smaller than a")

# elif statement
c = 14
if b > c:
    print("b is greater than c")
elif a > c:
    print("a is greater than c")
elif b == c:
    print("b is equal to c")

# for loop
for x in range(5):
    print(x)

# nested for loop
for m in range(0, 4):
    for n in range(0, 4):
        print(m, n)

# while loop
h = 12
while h < 15:
    print(h)
    h += 1

# patterns
for x in range(0, 4):
    for y in range(0, 4):
        print("*"),
        
