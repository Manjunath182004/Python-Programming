# Dictionaries & Sets Pratice prblms


"""
Store the following word meanings in a Python dictionary

table : "a piece of furniture", "list of facts & figures"
cat : "a small animal"

"""

dictionary = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}

print(dictionary)



"""
Count the classrooms needed for the subjects below (one classroom per subject).
"python", "java", "C", "python", "javascript", "java", "python", "java", "C", "C"

"""

subjects = {"python", "java", "C++", "python", "javascript", "java", 
            "python", "java", "C++", "C"}

print("Classroom needed: ", len(subjects))   # A set keeps only unique subjects, so its length is the number of classrooms.


#  Enter marks of 3 subjects from the user and store them in a dictionary.

marks = {}

marks["phy"] = int(input("Enter phy marks: "))
marks["chem"] = int(input("Enter chem marks: "))
marks["Bio"] = int(input("Enter Bio marks: "))

print(marks)


# Store 9 and 9.0 as separate values in a set.

# python treats 9 and 9.0 as equal, so a set keeps only one of them

values = {9, 9.0}
print(values)                  # output: {9}


# To keep both, store each as a tuple that also records its type

values = {("int", 9), ("float", 9.0)}
print(values)
print(len(values))


#  Loops Pratice Problems

# Using While Loop

#  Print numbers from 1 to 100.

i = 1
while i <= 100:
    print(i)
    i += 1


# Print numbers from 100 to 1.

i = 100
while i >= 1:
    print(i)
    i -= 1


# Print the multiplication table of a number n.

n = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(n, "X", i, "=", n * i)
    i += 1


#  Print the elements of the following list using a loop.
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


#  Search for a number x in this tuple using a loop.

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 36

idx = 0
while idx < len(nums):
    if nums[idx] == x:
        print("Found at index: ", idx)
    idx += 1



# for Loop Practice Problems

#  Print the elements of the following list using a loop.
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)


#  Search for a number x in this tuple using a loop.

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 49

idx = 0
for el in nums:
    if el == x:
        print("Found at index: ", idx)
        break
    idx += 1
else:
    print("Else Not found")        


# range() practice Prblms

# Print numbers from 1 to 100.

for i in range(1, 101):
    print(i)

# Print numbers from 100 to 1.

for i in range(100, 0, -1):         #  negative step counts down
    print(i)

# Print the multiplication table of a number n.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)



# Using Both while and for loop

# Find the sum of the first n numbers (using while).

n = int(input("Enter n: "))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum: ", total)


# Find the factorial of n (using for).

n = int(input("Enter n: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)   