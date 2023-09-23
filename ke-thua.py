class Animal:
    def __init__(self,leg,color,name):
        self.leg = leg
        self.color = color
        self.name = name
    def sound(self):
        print('GRUGRUGRU')
class Dog(Animal):
    def __init__(self,leg,color,name):
        super().__init__(leg)
        super().__init__(color)
        super().__init__(name)
class Chicken(Animal):
    def __init__(self,leg,color,name):
        super().__init__(leg)
        super().__init__(color)
        super().__init__(name)
animal = Animal(2,'green','cat')
