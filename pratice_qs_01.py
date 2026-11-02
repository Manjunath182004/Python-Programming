# Q1. Write a program to input 2 numbers and print their sum.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

sum = a + b
print("Sum = ", sum)


# Q2. Write a program to input the side of a square and print its area.

side = float(input("Enter side of square: "))

area = side * side   #  # or side ** 2
print("Area of Square = ", area)


# Q3. Write a program to input 2 floating-point numbers and print their average.

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

avg = (a + b) / 2
print("Average =", avg)


# Q4. Input 2 integers a and b. Print True if a is greater than or equal to b, otherwise print False.

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(a >= b)