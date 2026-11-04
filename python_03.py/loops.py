"""
Loops are used to repeat instructions.
pythonn has two kinds of loops : while and for 

"""

# While loop - keeps running as long as its condition is True.

# print "hello" 5 times

count = 1

while count <= 5:
    print("hello")
    count += 1
 
# print numbers 1 to 5

i = 1

while i <= 5:
    print(i)
    i += 1


# print numbers 5 to 1

i = 5

while i >= 1:
    print(i)
    i -= 1



# break and continue in loops

"""
break: terminates the loop immediately when encountered.
continue: skips the rest of the current iteration and moves on to the next one.

"""

# break - stop searching as soon as the number found

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

idx = 0
while idx < len(nums) :
    if nums[idx] == x:
        print("Fount at index: ", idx)
        break                              # no need to check further
    idx += 1

print("End of search")    


# continue - print numbers from 1 to 10, but skip multiples of 3.

i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue             # skip this number
    print(i)



# for Loop -  used for sequential traversal: going through each item of a list, string, tuple, etc

nums = [1, 2, 3]

for el in nums:
    print(el)


for ch in "python":
    print(ch)


"""
for loop with else  

The else block runs when the loop finishes normally. It does not run if the loop is stopped by break
"""

# Ex: 1

nums = [1, 2, 3]

for el in nums:
    print(el)
else:
    print("END")    


# Ex:2

nums = [1, 2, 3]

for el in nums:
    if el == 2:
        break
    print(el)
else:
    print("END")     # skipped because of break



# range()
"""
returns a sequence of numbers. It starts from 0 by default, increases by 1
by default, and stops before the given stop number. 

syntax: range(start, stop, step)  where start & step optional

"""

for el in range(5):    # 0 to 4
    print(el)

for el in range(1, 5):
    print(el)           # 1 to 4

for el in range(1, 10, 2):         # 1 to 9, step of 2
    print(el)    


# pass Statement
"""
is a null statement that does nothing. It is used as a placeholder for code
you will write later, because Python does not allow an empty block

"""

for el in range(10):
    pass                      # to be written later

print("Program continues")