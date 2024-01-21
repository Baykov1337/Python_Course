class Circle:
    def __init__(self,radius : int):
        self.radius = radius
    pi = 3.14

    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius 
    
    def get_area(self):
        return (self.radius**2)*self.pi
    
    def get_circumference(self):
        return 2 * self.radius * self.pi
    

circle = Circle(10)

print (circle.get_area())
print (circle.get_circumference())

circle.set_radius(12)
print (circle.get_area())
print (circle.get_circumference())