class MobilePhone:

    def __init__(self, owner_name):
        self.owner = owner_name
        self.__battery_life = 50


    def charge_phone(self):
        if self.__battery_life < 100:
            self.__battery_life += 10
            print(f"phone charging... Battery is now {self.__battery_life}%")        
        else:
            print("Battery already full!")


    def make_call(self):
        print("Connecting to network...")
        print("Finding satellite signals...")
        print("Ringing your friend...")


my_phone = MobilePhone("Rahul")

my_phone.make_call()

my_phone.charge_phone()