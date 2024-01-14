class Shape:
    def display(self):
         raise NotImplementedError("Subclasses must implement this method")
class Circle(Shape):
     def __init__(self,radius):
        self.radius  = radius
        
     def display(self):
        return 3.14 * self.radius
class Rectangle(Shape):
     def __init__(self,length, width):
        self.length  = length
        self.width  = width

     def display(self):
          return self.length * self.width

circle = Circle(5) 
rectangle = Rectangle(5,3)
print(f"Circle : {circle.display()}")
print(f"Rectangle : {rectangle.display()}")     