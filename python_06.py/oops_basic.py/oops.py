"""
OPPs: 

To map code to real-world scenarios, we use objects. Programming with objects
is called object oriented programming (OOP).
For example, every student has a name and marks, and can do things like
calculate an average. OOP lets us bundle that data and those actions together.

"""

# Class & Objects

# Class is Blue print for creating Objects
# an Object(instance) is real thing made from that blueprint


# creating class

class Student:                 
    name = "Manjunath"

# creating object (instance)
s1 = Student()
print(s1.name)


# Class & Instance Attributes

# Class Attributes - shared by all objects of the class.
# Instance Attributr - belongs to one particular object.

class University:
    collge_name = "Visvesvaraya Technological University"   # class attribute

    def __init__(self, name):
        self.name = name                                    # instance attribute      

s1 = University("Manjunath")
s2 = University("Roshan")

print(s1.name, s2.name)
print(University.collge_name)
print(s1.collge_name)


# __init__ Function (Constructor)

# All classes have a function called __init__() , which is always executed when an object is created. It is used to give initial values to the object.

# creating class
class MyCollege:

    def __init__(self, fullname):
        self.name = fullname


# creating object
s1 = MyCollege("Karan")
print(s1.name)

# del keyword

# del s1
# print(s1) 

# private and Public 

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass           # private

    def reset_pass(self):
        print(self.__acc_pass)    

acc1 = Account("12345", "dwde4sf")  

print(acc1.acc_no)
print(acc1.reset_pass)

# EX:

class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()    

p1 = Person()
print(p1.welcome())    


# property

class Student:
    def __init__(self, phy, chm, math):
        self.phy = phy
        self.chm = chm
        self.math = math


    @property
    def percentage(self):
        return str((self.phy + self.chm + self.math / 3)) + "%"


stu1 = Student(89, 78, 77)
print(stu1.percentage)

stu1.math = 67
print(stu1.percentage)