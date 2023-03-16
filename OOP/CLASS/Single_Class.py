class Animal:
    def __init__(self,name,age):
        self.name= name
        self.age = age 
    
    def speak(self):
        print("The animal makes a sound")
        
    
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak_2(self):
        print("The cat meows")

felix = Cat("Felix",3, "Black")
print(felix.name)
print(felix.age)
print(felix.color)
felix.speak()

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def speak(self):
        print("Hello, my name is {} and my age is {}".format(self.name, self.age))
        

class Student(Person):
    def __init__(self, name,age, enrollment):
        super().__init__(name,age)
        self.enrollment = enrollment
    
    def study(self):
        print("{} is studying".format(self.name))
        
augusto = Student("Augusto", 19,1234)
print(augusto.name)
print(augusto.age)
print(augusto.enrollment)
augusto.speak()