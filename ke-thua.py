class Animal:
    def __init__(self,leg,color,name):
        self.leg = leg
        self.color = color
        self.name = name
    def sound(self):
        print('GRUGRUGRU')
class Dog(Animal):
    def __init__(self,leg,color,name):
        super().__init__(leg,color,name)
    def sound2(self):
        print('wufwuf')
class Chicken(Animal):
    def __init__(self,leg,color,name):
        super().__init__(leg,color,name)
    def sound(self):
        print('cuctaccuctac')    
animal = Animal(2,'green','cat')
dog = Dog(4,'brown','kiki')
chicken = Chicken(2,'yellow','sus')
chicken.sound()
