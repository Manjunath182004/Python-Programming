# Single Inheritance

class Car:

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car Stopped.")

class ToyataCar(Car):

    def __init__(self, name):
        self.name = name

car1 = ToyataCar("Fortuner")
car2 = ToyataCar("prius")        
        
print(car1.name)

print(car1.start())
