"""
Functions

is a block of statements that performs a specific task. We write it
once and can use it many times.

def func_name(param1, param2):     -> function definition
    # some work
    return val

func_name(arg1, arg2)              -> function call
"""

# Ex

def calc_sum(a, b):
    s = a + b
    return s


print(calc_sum(2, 3))
print(calc_sum(10, 20))

# A function without return gives back None

def greet(name):
    print("Hello,", name)

result = greet("Aman")
print(result)


"""
Types of Functions 

1. Built-in Functions: Already provided by Python 

-> print() , len() , type() , range()

2. User-defined Functions: Written by the programmer

-> Created with def , like calc_sum() above

"""


# Default Parameters

def calc_product(a=1, b=2):
    return a * b

print(calc_product())       # uses both defaults
print(calc_product(5))      # a = 5, b uses default
print(calc_product(5, 6))


# Practice Questions:

# Write a function to print the length of a list (list is the parameter).

def print_len(items):
    print(len(items))

cities = ["Delhi", "Mumbai", "Pune"]
print_len(cities)


# Write a function to print the elements of a list in a single line (list is the parameter).

def print_list(items):
    for item in items:
        print(item, end=" ")
        print()

print_list(["Delhi", "Mumbai", "Pune"])


# Write a function to find the factorial of n (n is the parameter).

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))


# Write a function to convert USD to INR.

def usd_to_inr(usd, rate=83):
    return usd * rate

print(usd_to_inr(10))        # uses default rate
print(usd_to_inr(10, 88))    # pass the current rate
