#Functions
import dis
import unittest
from functools import reduce
from timeit import timeit
from math import factorial
from contextlib import contextmanager
import secrets
import functools

'''Lambda Calculus'''
'''First Example'''
#
def identity(x):
    return x

lambda x: x

lambda x: x + 1

(lambda x: x + 1)(2)

'''
(lambda x: x + 1)(2) = lambda 2: 2 + 1
                     = 2 + 1
                     = 3
'''

add_one = lambda x: x + 1
print(add_one(2))

def add_one(x):
    return x + 1

full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
print(full_name('guido', 'van rossum'))
print('\n')

'''Anonymous Functions'''
#
lambda x, y: x + y

print((1, 2))

print((lambda x, y: x + y)(2, 3))

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))
print('\n')

'''Python Lambda and Regular Functions'''
'''Functions'''
#
add = lambda x, y: x + y
print(type(add))
print(dis.dis(add))
print(add)

def add(x, y): return x + y
print(type(add))
print(dis.dis(add))
print(add)

div_zero = lambda x: x / 0
#print(div_zero(2)) ZeroDivisionError: division by zero

def div_zero(x): return x / 0
#print(div_zero(2)) ZeroDivisionError: division by zero
print('\n')

'''Syntax'''
#
#(lambda x: assert x == 2) (2) SyntaxError: invalid syntax
'''Single Expression'''
#
print((lambda x:
(x % 2 and 'odd' or 'even'))(3))
print('\n')

'''Type Annotations'''
#
def full_name(first: str, last: str) -> str:
    return f'{first.title()} {last.title()}'

#lambda first: str, last: str: first.title() + " " + last.title() -> str SyntaxError: only single target (not tuple) can be annotated
print('\n')

'''IIFE'''
#
print((lambda x: x * x)(3))
print('\n')

'''Arguments'''
#
print((lambda x, y, z: x + y + z)(1, 2, 3))
print((lambda x, y, z=3: x + y + z)(1,2))
print((lambda x, y, z=3: x + y + z)(1, y=2))
print((lambda *args: sum(args))(1, 2, 3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))
print('\n')

'''Decorators'''
#
def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorator_function(x):
    print(f"With argument '{x}'")
    
decorator_function("Python")

#Defining a decorator

def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

#Applying decorator to a function
@trace
def add_two(x):
    return x + 2

#Calling the decorated function

add_two(3)

#Applying decorator to a lambda
print((trace(lambda x: x **2 ))(3))

print(list(map(trace(lambda x: x*2), range(3))))
print('\n')

'''Closure'''
#
def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"Closure({i+5}) = {closure(i+5)}\n")

def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"Closure({i+5}) = {closure(i+5)}")
print('\n')

'''Evaluation Time'''
#
def wrap(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda n=n: print(n))

for f in funcs:
    f()
print('\n')

'''Testing Lambdas'''
#
addtwo = lambda x: x + 2

class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2),4)
        
    def test_add_two_point_two(self):
        self.assertEqual(add_two(2.2), 4.2)
    
    def test_add_three(self):
        #Should fail
        self.assertEqual(add_two(3), 6)


#if __name__ == '__main__':
#    unittest.main(verbosity=2)
#print('\n')

#======================================================================
#FAIL: test_add_three (__main__.LambdaTest.test_add_three)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "c:\Users\Windows 10\Documents\ROADMAP\LAMBDAS\Lambdas.py", line 202, in test_add_three
#    self.assertEqual(add_two(3), 6)
#AssertionError: 5 != 6

#----------------------------------------------------------------------
#Ran 3 tests in 0.005s


'''doctest'''
#
addtwo = lambda x: x + 2
addtwo.__doc__ = '''Add 2 to a number
    >>> addtwo(2)
    4
    >>>addtwo(2.2)
    4.2
    >>>addtwo(3) #Should fail
    6
    '''

#if __name__ == '__main__':
#    import doctest
#    doctest.testmod(verbose=True)

print('\n')

'''Lambda Expression Abuses'''
'''Raising an Exception'''
#
def throw(ex): raise ex
#(lambda: throw(Exception('Something bad happened')))()

'''Cryptic Style'''
#
print((lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10]))

print((lambda some_list: list(map(lambda n: n // 2,
                                  some_list)))([1,2,3,4,5,6,7,8,9,10]))

def div_items(some_list):
    div_by_two = lambda n: n // 2
    return map(div_by_two, some_list)

print(list(div_items([1,2,3,4,5,6,7,8,9,10])))
print('\n')

'''Python Classes'''
#
class Car:
    """Car with methods as lambda functions"""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
   #brand = property(lambda self: getattr(self, '_brand'),
   #                 lambda self, value: setattr(self, '_brand', value))
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value
    
    year = property(lambda self: getattr(self, '_year'),
                    lambda self, value: setattr(self, '_brand', value))
    
    #__str__ = lambda self: f'{self.brand} {self.year}' # 1: error E731
    
    def __str__(self):
        return f'{self.brand} {self.year}'
    
    honk = lambda self: print('Honk!') # 2: error E731
    

'''Appropriate Uses of Lambda Expressions'''
'''Classic Functional Constructs'''
#
print(list(map(lambda x: x.upper(), ['cat','dog','cow'])))

print(list(filter(lambda x: 'o' in x, ['cat','dog','cow'])))

print(reduce(lambda acc, x: f'{acc} | {x}', ['cat','dog','cow']))
print('\n')

'''Key Functions'''
#
ids = ['id1','id2','id3','id4','id5','id6']
print(sorted(ids)) # Lexicographic sort
sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
print(sorted_ids)
print('\n')

'''UI Frameworks'''
#
import tkinter as tk
import sys

window = tk.Tk()
window.grid_columnconfigure(0, weight=1)
window.title("Lambda")
window.geometry("300x100")
label = tk.Label(window, text="Lambda Calculus")
label.grid(column=0, row=0)
button = tk.Button(
    window,
    text="Reverse",
    command=lambda: label.configure(text=label.cget("text")[::-1]),
)
button.grid(column=0, row=1)
window.mainloop()
print('\n')

'''Python Interpreter'''
#
print(timeit("factorial(999)","from math import factorial", number=10))
print(timeit(lambda: factorial(999), number=10))
print('\n')

'''Monkey Patching'''
#
def gen_token():
    """Generate a random token."""
    return f"TOKEN_{secrets.token_hex(8)}"

@contextmanager
def mock_token():
    """Context manager to monkey patch the secrets.token_hex 
    function during testing"""
    default_token_hex = secrets.token_hex
    secrets.token_hex = lambda _: 'feedfacecafebeef'
    yield
    secrets.token_hex = default_token_hex

def test_gen_key():
    """Test the random token."""
    with mock_token():
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"
        
test_gen_key()

def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'

def test_gen_key(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"

'''Alternatives to Lambdas'''
'''Map'''
#
print(list(map(lambda x: x.capitalize(), ['cat','dog','cow'])))

print([x.capitalize() for x in ['cat','dog','cow']])
print('\n')

'''Filter'''
#
even = lambda x: x%2 == 0
print(list(filter(even, range(11))))

print([x for x in range(11) if x%2 == 0])
print('\n')

'''Reduce'''
#
pairs = [(1,'a'),(2, 'b'),(3,'c')]
print(functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0))

pairs = [(1, 'a'), (2,'b'), (3,'c')]
print(sum(x[0] for x in pairs))

pairs = [(1, 'a'), (2,'b'), (3, 'c')]
print(sum(x for x, _ in pairs))
