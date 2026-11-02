# Day 01: Introduction, Variables and Datatypes.


print("Hello World..") # first Basic Program in Every Programming Lang

print("Python", "is", "Easy", "to learn")
print(10 + 15)


# Varibales 

name = "Manjunath"
age = 22
prize = 59.90


print(name)
print(age)
print(prize)

age = 22
age = 24

print(age) # Value Updated


# Rules for Identifiers

myVariable = 10          # Valid
variable_1 = 20          # Valid
variable_for_print = 30  # Valid

# 1variable = 10        # Invalid: starts with a digit 
# my-var = 10           # Invalid: special symbol 
# my var = 10           # Invalid: contains a space
# 


#  Data Types

age = 23                   # int 
pi = 3.14                  # float
complex_num = 2 + 3j       # complex
A = True                   # Booalean
name = "Manjunath"         # string
x = None                   # None


print(type(age))           # use type() to check the type of a value
print(type(pi))
print(type(complex_num))
print(type(A))
print(type(name))
print(type(x))


# Basic Example 

a = 5
b = 10
sum = a + b
print("Sum is", sum)


# Types of Operators

# a) Arithmetic Operators

a, b = 10, 3

print(a + b)     # addition
print(a - b)     # subtraction
print(a * b)     # multiplication
print(a / b)     # division (always gives float)
print(a % b)     # remainder
print(a ** b)    # power: 10 to the power 3


# b) Relational / Comparison Operators ( ==, !=, >, <, >=, <= ) - These always Gives True or False 

a, b = 10, 3

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# c) Assignment Operators (=, +=, -=, *=, /=, %=, **= )

num = 10

num += 5         # num = num + 5
print(num)

num *= 2         # num = num * 2
print(num)

num -= 10        # num = num - 10
print(num)

num **= 2        # num = num ** 2
print(num)

num %= 2         # num = num % 2
print(num)


# d) Logical Operators (not, and, or)

"""
and - True only if both conditions are True
or  - True if at least one condition is True
not - Reverses the result

"""

a, b = True, False

print(a and b)
print(a or b)
print(not a)
print((5 > 3) and (2 > 1))


#  Type Conversion & Type Casting
 
# ex: 1 

a, b = 1, 2.0

sum = a + b        # int is converted to float
print(sum)


# ex: 2

a, b = 1, "2"

c = int(b)     # "2" becomes 2 - typecasting string -> int
sum = a + c
print(sum)

print(int("25"))     # str -> int
print(float(5))      # int -> float
print(str(100))      # int -> str
print(ord("A"))      # ASCII value
print(hex(255))      # hexadecimal
print(oct(8))        # octal


#  Input in Python 

# a) input(): string

name = input("Enter Your name: ")
print("Hello", name)
print(type(name))

# b) int(input()): integer

age = int(input("Enter Your age: "))
print("Next year you will be = ", age + 1)


# c) float(input()): decimal number

price = float(input("Enter the price: "))
print("Price with 10% tax:", price * 1.1)