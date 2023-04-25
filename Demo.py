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
myfloat = float(7.065)
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
names = ["Jack", "Bear", "Rose"]  # You forgot to add quotations to each name on the list note1.a

numbers.append([1,2,3])
strings.append("hello")
strings.append("world")

second_name = names[1] # That is why this code came up as error note1.b

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# Arithmetic Operators

number = 8 + 2 * 7 / 7.0
print (number)

# modulo operator %
remainder = 11 % 3
print (remainder)

# power relationship, use double multiply symbol

squared = 55**2
cubed = 55**3
print (squared, cubed)

# Concatenate Strings

mystring1 = "Concatenate"
mystring2 = "String"

print(mystring1 + " " + mystring2)

# Multiplying Strings

multiplegreen = "green " * 12
print (multiplegreen)

# Operators with Lists

even_numbers = (2, 4, 6, 8)
odd_numbers = (1,3,5,7,)
all_numbers = ( odd_numbers + even_numbers)
print (all_numbers)

print ([1,2,3,"Go"]*5)

# Exercise

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10           #your first atry is wrong x_list = ("x" *10)
y_list = [y] * 10
big_list = x_list + y_list

## parentheses ( ) are mainly used for function calls and expression grouping, while square brackets [ ] are used for list creation, indexing, and slicing.

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


