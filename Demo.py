print ("Hello, World")
print ("ハロー, 地球")
print ("你好，世界")
print ("Kamusta, Mundo")

x=1
y=2

if x==1 and y ==2:
    print("- mrseahorse")

# Integers
myint = 7
print ("Integers are whole numbers") 
print (myint)

# Floating Point 
print ("Floats are decimals")
myfloat = 7.0
print (myfloat)
myfloat = float(7)
print (myfloat)

# Strings
mystring = "Don't worry about apostrophes if using double quotes"
print (mystring)

# Simple Operators
x = 3
y = 5
z = x + y
print(z)

elf = "Elf"
dwarf = "Dwarven"
mix = dwarf + " " + elf
print (mix)

# Simultaneous Assigment
x, y = 5, 6
print (y,x)

# Operators between numbers and strings is not supported
# e.g. print (x + y + mix)


# Exercise
mystring = dwarf
myfloat = 10.0
myint = 20

print ("String: %s" % mystring)
print ("Integer: %d" % myint)
print ("Float: %f" % myfloat)

# Lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print (x)

# List Exercise
numbers = []
strings = []
names = ["Jack", "Bear", "Rose"]

numbers.append([1,2,3])
strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
