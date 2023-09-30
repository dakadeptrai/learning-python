import math
class Shape:
    def __init__(self,shape = 'shape'):
        self.shape = shape
        self.color = 'red'

class Circle(Shape):
    def __init__(self,radius):
        super().__init__(shape = 'circle')
        self.radius = radius
    def get_area(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self,width,height,shape = 'Rectangle'):
        super().__init__(shape = shape)
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self,height):
        super().__init__(width = height,height = height,shape ='Square')
    def get_area(self):
        return self.height * self.height 
circle = Circle(1)

print(circle.get_area())
# Output: 314.1592653589793

rectangle = Rectangle(10, 20)
print(rectangle.get_area())
# Output: 200

square = Square(10)
print(square.get_area())
# Output: 100 
