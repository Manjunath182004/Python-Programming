#Ex: 1

class Car:

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car Stopped.")

class ToyataCar(Car):

    def __init__(self, brand):
        self.name = brand

    
class Fortuner(ToyataCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("Diesel")
car1.start()

# Ex 2

class Animal:

    def breathe(self):
        print("Breathing air...")

class Mammal(Animal):
    def feed_milk(self):
        print("Feeding Milk to babies..")

class Dog(Mammal):
    def bark(self):
        print("woof woof!")


my_dog = Dog()

my_dog.breathe()

my_dog.feed_milk()

my_dog.bark()


# Ex 3:

class Device:

    def __init__(self, brand, power_source):
        self.brand = brand
        self.power_source = power_source
        self.is_on = False

    def toggle_power(self):
        self.is_on = not self.is_on
        status = "ON" if self.is_on else "OFF"
        print(f"{self.brand} device is now {status}")   

class Computer(Device):

    def __init__(self, brand, power_source, ram_gb):
        super().__init__(brand, power_source)
        self.ram = ram_gb

    def run_app(self, app_name):
        if self.is_on:
            print(print(f"Running '{app_name}' using {self.ram}GB RAM."))
        else:
            print(f"Cannot run '{app_name}'. Turn on the device first!")



class SmartPhone(Computer):

    def __init__(self, brand, power_source, ram_gb, network_type):
        super().__init__(brand, power_source, ram_gb)
        self.network = network_type

    def make_call(self, phone_number):
        if self.is_on:
            print(f"Connecting call to {phone_number} via {self.network}...")
        else:
            print("No signal. The phone is powered off.")



my_phone = SmartPhone(brand="Apple", power_source="Battery", ram_gb=8, network_type="5G")

my_phone.run_app("Instagram")

my_phone.toggle_power()

my_phone.run_app("Instagram")

my_phone.make_call("7847585885")