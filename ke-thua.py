class Animal:
    def __init__(self,sound,color,id):
        self.sound = sound
        self.color = color
        self.id = id
    def speed1(self):
        print('10-30 mph') 
class Dog(Animal):
    def __init__(self,sound,color,id):
        super().__init__(sound,color,id)
    def speed2(self):
        print('15-20 mph') 
class Cat(Animal):
    def __init__(self,sound,color,id):
        super().__init__(sound,color,id)
    def speed3(self):
        print('20-30 mph')    
animal = Animal('wwuwuwu','green','222')
dog = Dog('barkbark','brown','123')
cat = Cat('mewmew','yellow','223')
cat.speed3()
print(cat.sound)
