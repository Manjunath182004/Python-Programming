# if-elif-else

"""

Syntax:

if condition1:
    statement1               # runs if condition1 is True
elif condition2:
    statement2               # runs if condition2 is True
else:
    statementN               # runs if none of the above are True

"""



# Ex:  Traffic light Signals

light = "yellow"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Look")
elif light == "green":
    print("Go")
else:
    print("Light is broken")


# Ex: Grade Students Based on Marks

"""
marks >= 90 -> A
90 > marks >= 80 -> B
80 > marks >= 70 -> C
marks < 70 -> D

"""

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C" 
else:
    grade = "D"           


print("Grade: ", grade)