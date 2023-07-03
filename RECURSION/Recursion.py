#Imports
from sys import getrecursionlimit, setrecursionlimit
from functools import reduce
from timeit import timeit
from math import factorial

print(factorial(4))

setrecursionlimit(2000)
print(getrecursionlimit())

def function():
    x = 10
    function()

#function() RecursionError: maximum recursion depth exceeded

def countdown(n):# Recursive
    print(n)
    if n > 0:
        countdown(n - 1)

countdown(5)
print('\n')

def countdown_2(n): #Non-Recursive
    while n >= 0:
        print(n)
        n -= 1

countdown_2(10)
print('\n')

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(4))
print('\n')

def factorial_2(n):
    print(f"factorial() called with n = {n}")   
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value

print(factorial_2(4))
print('\n')

def factorial_3(n):
    return reduce(lambda x, y:x * y, range(1,n+1) or [1])

print(factorial_3(4))
print('\n')

timeit("print(string)",setup="string='foobar'",number=100)
print('\n')

setup_string = '''
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
'''

print(timeit("factorial(4)", setup = setup_string, number = 10000000))
print('\n')

setup_string_2 = '''
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value = 1
    return return_value
'''

print(timeit("factorial(4)", setup = setup_string_2, number = 10000000))
print('\n')

setup_string_3 = '''
#Functions
from functools import reduce
print("Reduce():")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
'''

print(timeit("factorial(4)", setup = setup_string_3, number = 10000000))
print('\n')

setup_string_4 = "from math import factorial"

print(timeit("factorial(4)", setup = setup_string_4, number = 10000000))
print('\n')

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"        
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

print(len(names)) #Count the elements on the top level
print('\n')

for index, item in enumerate(names):
    print(index, item)
print('\n')

print(names)
print(names[0])
print(isinstance(names[0], list))
print(names[1])
print(isinstance(names[1], list))
print(names[1][1])
print(isinstance(names[1][1], list))
print(names[1][1][0])
print(isinstance(names[1][1][0], list))
print('\n')

def count_leaf_items(item_list):
    '''
    Recursively counts and returns 
    the number of leaf items in a 
    (potentially nested) list.
    '''
    count = 0
    for item in item_list:
        if isinstance(item , list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count

print(count_leaf_items([1,2,3,4]))
print(count_leaf_items([1, [2.1, 2.2],3]))
print(count_leaf_items([]))
print(count_leaf_items(names))
