#Imports
from sys import getrecursionlimit, setrecursionlimit
from functools import reduce
from timeit import timeit
from math import factorial
import statistics
import random

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
print('\n')

def count_leaf_items_2(item_list):
    '''
    Recursively counts and returns 
    the number of leaf items in a 
    (potentially nested) list.
    '''
    print(f'List: {item_list}')
    count = 0
    for item in item_list:
        if isinstance(item, list): #isinstance(item, list) is True, so count_leaf_items_2() has found a sublist
            print("Encoutered sublist")
            count += count_leaf_items_2(item) #The function calls itself recursively to count the items in the sublist, then adds the result to the accumulating total.
        else: #isinstance(item, list) is False, so count_leaf_items() has encountered a leaf item.
            print(f"-> Returning count {count}")
            count += 1 #The function increments the accumulating total by one to account for the leaf item.
            
    print(f"-> Returning count {count}")
    return count

print(count_leaf_items_2(names))
print('\n')

def count_leaf_items_3(item_list):
    '''
    Non-recursively counts and returns 
    the number of leaf items in a 
    (potentially nested) list.
    '''
    count = 0
    stack = []
    current_list = item_list
    i = 0
    
    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue
        
        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1

print(count_leaf_items_3([1,2,3,4]))
print(count_leaf_items_3([1, [2.1,2.2], 3]))
print(count_leaf_items_3([]))
print(count_leaf_items_3(names))
print('\n')

def is_palindrome(word):
    '''Return True if word is a palindrome, False if not'''
    return word == word[::-1]

print(is_palindrome("foo"))
print(is_palindrome("racecar"))
print(is_palindrome("troglodyte"))
print(is_palindrome("civic"))
print('\n')

def is_palindrome_2(word):
    '''Return True if word is a palindrome, False if not.'''
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_2(word[1:-1])

#Base Cases
print(is_palindrome_2(""))
print(is_palindrome_2("a"))

#Recursive Cases
print(is_palindrome_2("foo"))
print(is_palindrome_2("racecar"))
print(is_palindrome_2("troglodyte"))
print(is_palindrome_2("civic"))
print('\n')

def quicksort(numbers):
    if len(numbers) <= 1: #The base cases where the list is either empty or has only a single element
        return numbers
    else:
        pivot = statistics.median( #Calculation of the pivot item by the median-of-three method
            [
            numbers[0],
            numbers[len(numbers) // 2],
            numbers[1]
            ]
        )
        items_less, pivot_items, items_greater = ( #Creation of the three partition lists
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )
        
        return ( #Recursive sorting and reassembly of the partition lists
            quicksort(items_less) + 
            pivot_items + 
            quicksort(items_greater) 
        )

print(quicksort([]))
print(quicksort([42]))
print(quicksort([5,2,6,3]))
print(quicksort([10,-3,21,6,-8]))
print('\n')

def get_random_numbers(length, minimun = 1, maximum = 100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimun,maximum))
    
    return numbers

numbers = get_random_numbers(20)
print(numbers)

print(quicksort(numbers))

numbers_2 = get_random_numbers(15, -50, 50)
print(numbers_2)

print(quicksort(get_random_numbers(10, maximum=500)))
print(quicksort(get_random_numbers(10, 1000, 2000)))