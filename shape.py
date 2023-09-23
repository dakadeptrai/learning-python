import math
class Shape:
    def __init__(self,color,shape):
        self.shape = shape
        self.color = color
class Circle(Shape):
    def __init__(self,radius,color,shape):
        super().__init__(color,shape)
        self.radius = radius
    def get_area(self):
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    def __init__(self,width,height,color,shape):
        super().__init__(color,shape)
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
class Rectangle(Shape):
    def __init__(self,width,height,color,shape):
        super().__init__(color,shape)
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
