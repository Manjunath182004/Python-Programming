"""
Create a Student class that takes name and marks of 3
subjects as arguments in the constructor. Then create a
method to print the average.

"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        avg = sum(self.marks) / len(self.marks)
        print(self.name, "average:", avg)


s1 = Student("Tony Stark", [99, 98, 97]) 
s1.get_avg()           

s2 = Student("Captain America", [67,89, 45])
s2.get_avg()


"""
Create an Account class with 2 attributes: balance and
account number. Create methods for debit, credit and printing
the balance.

"""        

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "Was debited")   
        self.get_balance()

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "Was Credited")
        self.get_balance()

    def get_balance(self):
        print("Total balance =", self.balance)


acc1 = Account(10000, 12345678)
acc1.debit(1000)
acc1.credit(500)


"""
Define a Circle to create a circle with radius r using the constructor.
define an Area() method of the class which calculates the area of the circle.
define a Perimeter method of the class which allows you to calculatethe perimeter of the circle.

"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius   


c1 = Circle(21)
print(c1.area())
print(c1.perimeter())        


"""
Define a Employe class with attribute role, department & salary. This class alos as the show() details method
create an Engineer class that inherits properties from Employee & has additional attributes names and age

"""

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role=", self.role)  
        print("dept=", self.dept)
        print("salary=", self.salary)    



class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "It", "75000")
        

eng1 = Engineer("Modi", 56)  
eng1.showDetails()     


"""
create a class called order which stores item & its price.
Use Dunder function __get__() to convey that 
order1> order2> order3

"""

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("Chips", 20)
ord2 = Order("tea", 15)    
             
print(ord1 > ord2)        