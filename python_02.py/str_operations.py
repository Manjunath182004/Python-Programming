#  Basic Operations

# a) Concatenation

first = "Hello"
second = input("Enter Your Name: ")
third = "Good Morning"

print(first + " " + second + " " + third )


# b) Length of a String

collge_name = "Visvesvaraya Technological University" 
print("Number of characters in ", collge_name, "is :", len(collge_name))             # len()  returns the number of characters in a string (spaces count too)


# Indexing

collge_name = collge_name = "Visvesvaraya Technological University" 

print(collge_name[0])
print(collge_name[5])
print(collge_name[9])


# Slicing

# Syntax = string[staring_idx : ending_ idx] where ending_idx is not included 

collge_name = collge_name = "Visvesvaraya Technological University"
 
print(collge_name[1:4])    # characters at index 1, 2, 3

print(collge_name[:4])               # college_name[0:4]

print(collge_name[4:])               # college_name[4:leg(college_name)]


# slicing - Negative Index - Negative indexes count from the end of the string. The last character is at index

fruit = "Apple"

print(fruit[-1])
print(fruit[-3:-1])   # index -3 and -2
print(fruit[-3:])