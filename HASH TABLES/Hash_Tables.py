import string
from collections import Counter
from string import printable

#1
glossary = {"BFDL": "Benevolent Dictator For Life"}
glossary["GIL"] = "Global Interpreter Lock" #Add
glossary["BFDL"] = "Guido wan Rossum" #Update

del glossary["GIL"]
glossary["BFDL"]

print(glossary)
print('\n')

#2

text = string.ascii_uppercase * 100_000_000

print(text[:50])

print(len(text))

print(text[0])

print(text[len(text) // 2])

print(text[-1])
print('\n')

#3

print(hash(3.14))

print(hash(3.14159265358979323846264338327950288419716939937510))

print(hash("Lorem"))

print(hash("Lorem ipsum dolor sit amet, consectetur adipisicing elit,"
    "sed do eiusmod tempor incididunt ut labore et dolore magna"
    "aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
    "ullamco laboris nisi ut aliquip ex ea commodo consequat."
    "Duis aute irure dolor in reprehenderit in voluptate velit"
    "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
    "occaecat cupidatat non proident, sunt in culpa qui officia"
    "deserunt mollit anim id est laborum."))

print(hash(None))

print(hash(hash))

class Person:
    pass

print(hash(Person))

print(hash(Person()))
print('\n')

#4

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * ""
        print(f"{key:3} {'■'}{padding}({count})")
        
plot(distribute(printable, num_containers=2))

plot(distribute(printable, num_containers=5))
print('\n')

#5

print(id("Lorem"))
print('\n')

#6

def hash_function(text):
    return sum(ord(character) for character in text) # hash collision

print(hash_function("Lorem"))
print(hash_function("Loren"))
print(hash_function("Loner")) 
print('\n')

#7

def hash_function_2(key):
    return sum(ord(character) for character in str(key)) #dont differ string to a number

print(hash_function_2("Lorem"))
print(hash_function_2(3.14))
print(hash_function_2(True))
print(hash_function_2("3.14"))
print(hash_function_2(3.14))
print('\n')

#8

def hash_function_3(key):
    return sum(ord(character) for character in repr(key))

print(hash_function_3("3.14"))
print(hash_function_3(3.14))
print('\n')

#9

def hash_function_4(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start = 1)
    )
    
print(hash_function_4("tity"))
print(hash_function_4("This has a somewhat medium length."))
print(hash_function_4("This is very long and slow!" * 1_000_00))
print(hash_function_4("Tiny") % 100)
print(hash_function_4("This has somewhat medium length.") % 100)
print(hash_function_4("This is very long and slow.!" * 1_000_00) % 100) 
print('\n')

#10