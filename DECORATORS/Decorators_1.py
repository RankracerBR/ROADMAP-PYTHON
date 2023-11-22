#Functions
from datetime import datetime
import functools
import time
import random
from dataclasses import dataclass

def add_one(number):
    return number + 1

print(add_one(2))
print('\n')

'''First-Class Objects'''
#
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))

print(greet_bob(be_awesome))
print('\n')

'''Inner Functions'''
#
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Priting from the first_child() function")
        
    def second_child():
        print("Printing from the second_child() function")
    
    second_child()
    first_child()

parent()
print('\n')

'''Returning Functions From Functions'''
#
def parent(num):
    def first_child():
        return "Hi, I am Emma"
    
    def second_child():
        return "Call me Liam"
    
    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)

print(first)

print(second)

print(first())

print(second())
print('\n')

'''Simple Decorators'''
#
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

print(say_whee())

say_whee = my_decorator(say_whee)
print(say_whee)

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee()
print('\n')

'''Syntactic Sugar!'''
#
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
print('\n')

'''Reusing Decorators'''
#
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

def do_twice_(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

print(print)

print(print.__name__)

print(help(print))

print(...)

print(say_whee)

def do_twice_3(func):
    @functools.wraps(func)
    def wrapper_to_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_to_twice

print(say_whee)

print(say_whee.__name__)

print(help(say_whee))
print('\n')

'''A Few Real World Examples'''
#
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        #Do something before
        value = func(*args, **kwargs)
        #Do something after
        return value
    return wrapper_decorator
print('\n')

'''Timing Functions'''
#
def timer(func):
    '''Print the runtime of the decorated function'''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter() # 2
        run_time = end_time - start_time # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waster_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
        
print(waster_some_time(1))

print(waster_some_time(999))
print('\n')

'''Debugging Code'''
#
def debug(func):
    '''Print the function signature and return value'''
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args] # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()] # 2
        signature = ", ".join(args_repr + kwargs_repr) # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

print(make_greeting("Benjamin"))

print(make_greeting("Richard", age=112))

print(make_greeting(name="Dorrisile", age=116))
print('\n')

'''Slowing Down Code'''
#
def slow_down(func):
    '''Sleep 1 second before calling the function'''
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)
print('\n')

'''Registering Plugins'''
#
PLUGINS = dict()

def register(func):
    '''Register a function as a plug-in'''
    PLUGINS[func.__name__] = func
    return func

@register 
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(PLUGINS)

print(randomly_greet("Alice"))

print(globals())
print('\n')

'''Fancy Decorators'''
'''Decorating Classes'''
#
class Circle:
    def __init__(self, radius):
        self._radius = radius
        
    @property
    def radius(self):
        '''Get value of radius'''
        return self._radius
    
    @radius.setter
    def radius(self, value):
        '''Set radius, raise error if negative'''
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
        
    @property
    def area(self):
        '''Calculate area inside circle'''
        return self.pi() * self.radius**2
    
    def cylinder_volume(self, height):
        '''Calculate volume of cylinder with circle as base'''
        return self.area * height
    
    @classmethod
    def unit_circle(cls):
        '''Factory method creating a circle with radius 1'''
        return cls(1)
    
    @staticmethod
    def pi():
        '''Value of π, could use math.pi instead though'''
        return 3.1415926535
    
c = Circle(5)
print(c.radius)

print(c.area)

c.radius = 2
print(c.area)

#c.area = 100 AttributeError: property 'area' of 'Circle' object has no setter

print(c.cylinder_volume(height=4))

#c.radius = -1 ValueError: Radius must be positive

c = Circle.unit_circle()
print(c.radius)

print(c.pi())

print(Circle.pi())


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

tw = TimeWaster(1000)

tw.waste_time(999)

@dataclass
class PlayingCard:
    rank: str
    suit: str
print('\n')

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

print(greet("World"))
print('\n')

'''Both Please, But Never Mind the Bread'''
#
def repeat(_func=None,*, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

@repeat
def say_whee():
    print("Whee!")
    
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

say_whee()

greet("Augusto")
print('\n')

'''Stateful Decorators'''
#
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")

say_whee()

say_whee()

print(say_whee.num_calls)
print('\n')

'''Classes as Decorators'''
#
class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")
        
counter = Counter()
print(counter())

print(counter())

print(counter.count)

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")

@CountCalls
def say_whee():
    print("Whee!")
    
print(say_whee())

print(say_whee())

print(say_whee.num_calls)
print('\n')

'''More Real World Examples'''
'''Slowing Down Code, Revisited'''
#
def slow_down(_func=None,*, rate=1):
    """Sleep given amount of seconds before calling the function"""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down
    
    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func) 

@slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)
print('\n')

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
