#  Write a program to input the user's first name and print its length

name = input("Enter your first name: ")
print("Length of your name is", len(name))


# Write a program to find the occurrence of '$' in a string.

text = "Hi $ I am $ learning Python $"
print("Occurrences of $ :", text.count("$"))



# Write a program to check if a number entered by the user is odd or even.


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Write a program to find the greatest of 3 numbers entered by the user.    

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a >= b and a >= c:
    print("Greatest is", a)
elif b >= c:
    print("Greatest is", b)
else:
    print("Greatest is", c)


#  Write a program to check if a number is a multiple of 7 or not.


num = int(input("Enter a number: "))

if num % 7 == 0:
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")




# Ask the user to enter the names of their 3 favorite movies and store them in a list.


movies = []

movies.append(input("Enter 1st Movie: "))
movies.append(input("Enter 2nd Movie: "))
movies.append(input("Enter 3rd Movie: "))

print(movies)



# Check if a list is a palindrome (reads the same forwards and backwards).


# Ex:  [1, 2, 3, 2, 1] and [1, "abc", "abc", 1] are palindromes. Hint: use the copy() method.

nums = [1, 2, 3, 2, 1]
 
copy_nums = nums.copy()            # make a copy first
copy_nums.reverse()                # reverse the copy, not the original


if nums == copy_nums:
    print("Palindrome")
else:
    print("Not a palindrome")    


# Count the number of students with the "A" grade in the following tuple.

grades = ("C", "A", "C", "D", "A", "D", "A", "B", "A")

print("Students with A grade: ", grades.count("A"))


# Store the above values in a list and sort them from "A" to "D".

grades = ["C", "A", "C", "D", "A", "D", "A", "B", "A"]   

grades.sort()
print(grades)