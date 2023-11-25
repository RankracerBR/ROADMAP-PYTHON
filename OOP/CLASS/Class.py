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

#
class Dog3:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"

#
class JackRussellTerrier(Dog3):
    pass

class Dachshund(Dog3):
    pass

class Bulldog(Dog3):
    pass

#
class JackRussellTerrier2(Dog3):
    def speak(self, sound="Arf"):
        return super().speak(sound)


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

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


print(type(miles))

print(isinstance(miles, Dog))

print(isinstance(miles, Bulldog))

#
miles = JackRussellTerrier2("Miles",4)  
print(miles.speak())