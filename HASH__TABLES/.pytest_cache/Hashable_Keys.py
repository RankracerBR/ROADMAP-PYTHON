#1
print(hash(frozenset(range(10))))

#print(hash(set(range(10)))) TypeError: unhashable type: 'set'
print("\n")

#2
hashable = frozenset(range(10))
print({hashable: "set of numbers"})

unhashable = set(range(10))
#print({unhashable: "set of numbers"}) TypeError: unhashable type: 'set'
print('\n')

#3
#@dataclass(unsafe_hash = True)
class Person:
    #__hash__ = None This will prevent hash() from working on instances of your class.
    
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if self is other:
            return True

        if type(self) is not type(other):
            return False
        
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)

print(hash(Person("Joe")))

print(hash(Person("Augusto")))

print(hash(Person("Joe")) == hash(Person("Joe")))

alice = Person("Alice")
bob = Person("Bob")

employess =  {alice: "project manager", bob:"engineer"}

print(employess[bob])

print(employess[Person("Bob")])

bob.name = "Bobby"

#employess[bob] KeyError: <__main__.Person object at 0x7f607e325e40>

#employess[Person("Bobby")]

#employess[Person("Bob")]