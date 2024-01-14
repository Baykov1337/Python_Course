#create class Car with the following attributes

class Car:
    def __init__  (self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print (f"Car Brand:[{self.brand} Model:{self.model} Year : {self.year} Milleage : {self.mileage}") 

class ElectricCar(Car):
    def __init__(self, brand, model, year, mileage,battery_capacity):
        super().__init__(brand, model, year, mileage) 
        self.battery_capacity = float(battery_capacity)
    def display_info(self):
        print (f"Car Brand:[{self.brand} Model:{self.model} Year : {self.year} Milleage : {self.mileage} Battery Capacity: {self.battery_capacity}") 

test = ElectricCar("Audi","A4","2003", "245000","100")
print (test.display_info())

