"""
Lists - stores the collection of values in []

A list can store elemnets of differents types(int, float, str..etc)

list are mutable 

"""

marks = [89, 67, 45, 46, 34, 90]
student = ["Manju", "Abhi", 89, "Kali"]

print(marks)
print(student)
print(marks[0])
print(student[3])


student = ["karana", 78, "Harshi"]
student[0] = "Arjun"    # List also mutable unlike str

print(student)
print(len(student))


# List Slicing

# list_name(starting_idx : ending_idx)  ending not included 

marks = [89, 67, 45, 46, 34, 90] 

print(marks[1:4])
print(marks[:4])            # same as marks[0:4]
print(marks[1:])            # same as marks[1:len(marks)]
print(marks[-3:-1])         # negative indexes



# list Methods

num = [2, 1, 3]
num.append(4)                # append() Adds one element at the end
print(num)

num = [2, 1, 3]
num.sort()                     # sort() Sorts in ascending order
print(num)

num = [2, 1, 3]
num.sort(reverse=True)          #  Sorts in descending order
print(num)


num = [2, 1, 3]
num.reverse()              #  Reverses the list
print(num)


num = [2, 1, 3]
num.insert(1, 5)                 # insert 5 at index 1
print(num)


nums = [2, 1, 3, 1]
nums.remove(1)                   # removes first 1 only
print(nums)


nums = [2, 1, 3, 1]
nums.pop(2)                       # removes element at index 2
print(nums)