#
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


#
class Dog:
    species = "Canis Familiaris"
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    #Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    #Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
#
class Dog2:
    pass

Dog2()

#Two distinct objects in memory
a = Dog2()
b = Dog2()
print(a == b)

#
miles = Dog("Miles", 4,'')
buddy = Dog("Buddy", 9,'')

print(miles.name, miles.age)

print(buddy.name, buddy.age)

print(buddy.species)

buddy.age = 10
print(buddy.age)

miles.species = "Felis Silvestris"
print(miles.species)

#
miles = Dog("Miles", 4,'')

print(miles.speak("Woof Woof"))

#print(miles)

print(miles)

print('\n')

#
class Parent:
    hair_color = "Brown"
    speaks = ["English"]

class Child(Parent):
    hair_color = "Purple"
    
    def __init__(self):
        super().__init__()
        self.speaks.append("German")
    
child = Child()

print(child.speaks)

a = child.speaks.append("Italy")
print(child.speaks)

#
miles = Dog("Miles", 4, "Jack Russel Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Woof"))

#
print(type(miles))