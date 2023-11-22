#Functions
import functools
from Decorators_1 import do_twice_
import math
from Decorators_1 import debug
from Decorators_1 import timer
from Decorators_1 import debug, do_twice_3
from Decorators_1 import count_calls
import pint

@do_twice_
def say_whee():
    print("Whee!")

say_whee()

@do_twice_
def greet(name):
    print(f"Hello {name}")

#greet("World")TypeError: do_twice.<locals>.wrapper_do_twice() takes 0 positional arguments but 1 was given
print('\n')

say_whee()

greet("World")
print('\n')

@do_twice_
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")
print(hi_adam)

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

approximate_e(5)

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num
        
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
           
tw = TimeWaster(1000)

print(tw.waste_time(999))
print('\n')

'''Nesting Decorators'''
#
@debug
@do_twice_3
def greet(name):
    print(f"Hello {name}")

print(greet("Eva"))

@do_twice_3
@debug
def greet(name):
    print(f"Hello {name}")

'''Caching Return Values'''
#    
@count_calls
def fibonnaci(num):
    if num < 2:
        return num
    return fibonnaci(num - 1) + fibonnaci(num - 2)

print(fibonnaci(10))

fibonnaci.num_calls

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonnaci(10))

print(fibonnaci(8))

@functools.lru_cache(maxsize=4)
def fibonnaci(num):
    print(f"Calculating fibonnaci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)

fibonacci(8)

fibonacci(5)

fibonacci(8)

fibonacci(5)

print(fibonnaci.cache_info())


'''Creating Singletons'''
#
def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

first_one = TheOne()
another_one = TheOne()

print(id(first_one))

print(id(another_one))

print(first_one is another_one)
print('\n')

'''Adding Information About Units'''
#
def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit

@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height

print(volume(3, 5))

print(volume.unit)

@set_unit("cm^3")
def volume(radius, height) -> "cm^3":
    return math.pi * radius**2 * height

ureg = pint.UnitRegistry()
vol = volume(3, 5) * ureg(volume.unit)

print(vol)

print(vol.to("cubic inches"))

print(vol.to("gallons").m) #Magnitude

def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    use_unit.ureg = pint.UnitRegistry()
    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)
        return wrapper_use_unit
    return decorator_use_unit

@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration

bolt = average_speed(100, 9.58)
print(bolt)

print(bolt.to("km per hour"))

print(bolt.to("mph").m) # Magnitue
print('\n')


