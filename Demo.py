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


# String Formatting

# This prints out "Howdy, Jack!"
name = "Jack"
print("Howdy, %s!" % name)

# This prints out "Jack is 123 years old."
name = "Jack"
age = (123)
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

## Exercise

data = ("Jack", "Miyamoto", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# Basic String Operations

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))
print(astring.index ("o"))
print(astring.count("l"))

print(astring[4:7])
print(astring[:7])
print(astring[7:])
print(astring[-2])
print(astring[1:3:2]) #extended slice syntax. The general form is [start:stop:step]
print(astring[::-1])
print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print(afewwords)

# Exercise

x = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(x))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % x.index("a"))

# Number of a's should be 2
print("a occurs %d times" % x.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % x[:5]) # Start to 5
print("The next five characters are '%s'" % x[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % x[12]) # Just number 12
print("The characters with odd index are '%s'" %x[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % x[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % x.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % x.lower())

# Check how a string starts
if x.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if x.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % x.split(" "))