"""
Recursion

Recursion is when a function calls itself repeatedly. Every recursive function
needs a base case: a condition where it stops calling itself. Without it, the function
would run forever (and Python stops it with a RecursionError ).

"""


# EX

def show(n):
    if n == 0:               # base case
        return
    print(n)
    show(n - 1)              # function calls itself
    
show(5)


# Factorial using Recursion

# n! = n × (n−1)!, and 0! = 1! = 1 (base case)

def fact(n):
    if n == 0 or n == 1: # base case
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))

"""
How it Works

Ex: fact(4)

fact(4) = 4 * fact(3)
        = 4 * 3 * fact(2)
        = 4 * 3 * 2 * fact(1)
        = 4 * 3 * 2 * 1
        = 24

"""


# practice 

# Write a recursive function to calculate the sum of the first n natural numbers.

def calc_sum(n):
    if n == 0: # base case
        return 0
    return n + calc_sum(n - 1)

print(calc_sum(5))


# Write a recursive function to print all elements in a list.

def print_list(items, idx=0):
    if idx == len(items):                     # base case: reached the end
        return
    print(items[idx])
    print_list(items, idx + 1)

print_list(["mango", "apple", "banana"])
