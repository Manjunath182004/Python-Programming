# Methods:

# Methods are functions that belongs to objects. This First parameter is self
from datetime import datetime

class MyCourse:
    def __init__(self, courseName):
        self.name = courseName

    def courseName(self):
        print("Hello I am Learning", self.name)

s1 = MyCourse("Python")
s1.courseName()            


# Static Methods
"""
Static methods don't use the self parameter. They work at the class level and are
marked with the @staticmethod decorator.

"""

# simple Ex: 

class MyStudent:
    @staticmethod # decorator
    def college():
        print("ABC College")

MyStudent.college()
s1 = MyStudent()
s1.college()


# Ex: 

class Greeting:

    @staticmethod
    def get_greeting():

        current_hour = datetime.now().hour

        if current_hour < 12:
            return "Hello, Good Morning!"
        elif 12 <= current_hour < 17:
            return "Hello, Good Afternoon!"
        elif 17 <= current_hour < 21:
            return "Hello, Good Evening!"
        else:
            return "Hello, Good Night!"

message = Greeting.get_greeting()
print(message)


# class Method

class Person:
    name = "anonymous"

    @classmethod
    def changename(cls, name):
        cls.name = name
 
p1 = Person()
p1.changename("Rahul kumar")
print(p1.name)
print(Person.name)