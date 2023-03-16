class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print("The animal makes a sound")
    
class Mammal(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def feed_milk(self):
        print("The animal needs to feed theyr puppy :3")
        
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def lay_eggs(self):
        print("The bird lays eggs")
        
dog = Mammal("Dog")
dog.speak()
dog.feed_milk()

eagle = Bird("Eagle")
eagle.speak()
eagle.lay_eggs()