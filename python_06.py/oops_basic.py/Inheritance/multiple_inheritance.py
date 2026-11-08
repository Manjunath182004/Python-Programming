class A:
    varA = "welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class c"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


# Ex2 

class Camera:
    def take_photo(self):
        print("Click! Photo taken and saved to gallery.")

class Phone:
    def make_call(self, number):
        print(f"Dialing {number}...")      


class Smartphone(Camera, Phone):
    def browse_internet(self):
        print("Opening the web browser...")


my_phone = Smartphone()

my_phone.take_photo()

my_phone.make_call("Emergency")

my_phone.browse_internet()


# Ex 3

class DigitalProduct:
    def __init__(self, price):
        self.price = price

    def show_price(self):
        print(f"Price: ${self.price}")   


class PhysicalProduct:
    def __init__(self, weight_kg):
        self.weight_kg = weight_kg

    def show_shipping(self):
        print(f"Shipping weight: {self.weight_kg} kg")    


class SmartWatch(DigitalProduct, PhysicalProduct):

    def __init__(self, model_name, price, weight_kg):
        DigitalProduct.__init__(self, price)
        PhysicalProduct.__init__(self, weight_kg)
        self.model_name = model_name

    def display_info(self):
        print(f"--- {self.model_name} Info ---")
        self.show_price()      
        self.show_shipping()

my_watch = SmartWatch(model_name="FitBit V2", price=199, weight_kg=0.15)    

my_watch.display_info()