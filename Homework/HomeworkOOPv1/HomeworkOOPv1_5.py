class Vehicle():
    def __init__(self, max_speed:int = 150, mileage:int=0):
        self.max_speed = max_speed
        self.mileage = mileage 
        self.gadgets = []


car = Vehicle(150,20)   
print (car.max_speed)
print (car.mileage)
print (car.gadgets)
car.gadgets.append('test')
print (car.gadgets)
