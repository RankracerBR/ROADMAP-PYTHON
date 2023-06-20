import string


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

