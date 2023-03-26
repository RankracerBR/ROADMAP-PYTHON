#Imports
from asyncio import sleep,run
import functools 
#abs if receives a negative number it will return the distance of the positive number from the 0.
class number_string:
    def __init__(self,value):
        self.value = value 
    
    def __abs__(self):
        absolute = self.value.replace('negative'," ")
        return absolute 

number = number_string("negative ten")
print(abs(number))
print('\n')

#Return an asynchronous iterator for an asynchronous iterable. Equivalent to calling x.__aiter__(). Note: Unlike iter(), aiter() has no 2-argument variant.
class Foo: 
    def __aiter__(self):
        self.i = 0
        return self 
    async def __anext__(self):
        await sleep(1)
        self.i += 1
        return self.i 

async def using_async_for():
    async for bar in Foo():
        print(bar)
        if bar >= 10:
            break 
      
async def using_aiter_anext():
    ai = aiter(Foo())
    try: 
        while True:
            bar = await anext(ai)
            print(bar)
            if bar >= 10:
                break
    except StopAsyncIteration:
        return 

async def main():
    print('Using async for:')
    await using_async_for()
    
    print("Using aiter/anext")
    await using_aiter_anext()

if __name__ == '__main__':
    run(main())

#Return True if any element of the iterable is true. If the iterable is empty, return False.
def all(iterable):
    for element in iterable:
        if element:
            return True 
    return False

print('\n')

#Convert an integer number to a binary string prefixed with “0b”.
print(bin(3))
print(bin(-19))

print(format(14, '#b'), format(14, 'b'))
print(f'{14:#b}', f'{14:b}')

#Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure.
class bool(int):
    def __new__(cls, x=False):
        if x: 
            return super().__new__(cls, 1)
        else:
            return super().__new__(cls, 0)
    def __init__(self, x=False):
        pass

print('\n')
  
#This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments.
def example(x):
    if x < 0:
       pass #breakpoint()
    else:
        print('O valor de x é:',x)
example(-8)    

print('\n')

#Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256.    
empty_array = bytearray()
string = 'Hello World!'
array_string = bytearray(string, 'utf-8')

buffer = b'\x00\x01\x02'
array_buffer = bytearray(buffer)

list_ = [65,66,67]
array_list = bytearray(list_)

print(f'{empty_array}\n{array_string}\n{array_buffer}\n{array_list}')

print('\n')

#Return a new “bytes” object which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray.
bytes_obj = bytes('Hello, World!', encoding='utf-8')
print(bytes_obj)

print(bytes_obj[0])
print(bytes_obj[1])
print(bytes_obj[2])

list_ = [72,101,108,108,11,44,32,119,111,114,108,100,33]
bytes_obj2 = bytes(list_)
print(bytes_obj2)

print('\n')

#Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed.
def my_func():
    print('Hello, World!')
    
class MyClass_1:
    def __call__(self):
        print('Hello from MyClass! :3')

obj = MyClass_1()

print(callable(my_func))
print(callable(obj))

print(callable('hello'))
print(callable(123))

#Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'
print(chr(97))

print(chr(8364))

try:
    print(chr(1114112))
except ValueError as e:
    print(e)
    
for i in range(87,101):
    print(chr(i))
    
print('\n')

#Transform a method into a class method. A class method receives the class as an implicit first argument, just like an instance method receives the instance
class MyClass:
    x = 0
    
    @classmethod
    def increment_x(cls, amount):
        cls.x += amount

MyClass.increment_x(5)
print(MyClass.x)

obj = MyClass()
obj.increment_x(3)
print(obj.x)

print('\n')

#Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). source can either be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how to work with AST objects.The filename argument should give the file from which the code was read; pass some recognizable value if it wasn’t read from a file ('<string>' is commonly used).
source = "print('Hello, World!')"
code = compile(source, filename="<string>", mode="exec")
exec(code)

#Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter.
number1 = complex(2,3)
print('Complex Numbers created with real values and imaginaries:', number1)
number2 = complex("4+5j") #cannot contain spaces beetwen the string ("4 + 5J")
print('Complex Number created by a string:', number2)
number3 = complex(7)
print('Int Number converted to a Complex Number:',number3)
number4 = complex(2.5)
print('Float Number converted to a Complex Number:',number4)
number5 = complex(6)
print('Complex Number with the default real value and imaginary:', number5)

print('\n')

#This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it.
class Myclass:
    x = 10
    y = 20
    z = 'zooba'
obj = MyClass()
#delattr(obj, 'x')
#print(obj.x)

#The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar. name need not be a Python identifier.
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade 
    
p = Pessoa('João', 30)
print(p.nome)
print(p.idade)
#delattr(p, "name")
#print(p.nome)
#print(p.idade)

print('\n')

#Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types — dict for documentation about this class.
dicionario_1 = {'Nome': 'João', 'Idade': 30, 'Cidade':'João Pessoa'}#keys
dicionario_2 = dict(nome='Maria',idade=25, cidade='Natal')#constructor
dicionario_3 = dict([('Nome', 'Pedro'), ('idade', 35), ('Cidade', 'Campina Grande')])#tuples

print(dicionario_1)
print(dicionario_2)
print(dicionario_3)

print('\n')

#If you pass an object as an argument to dir(), it will attempt to return a list of valid attributes for that object. This can be useful to inspect the attributes and methods available on an object, especially if you are working with an unfamiliar class or module.
class MyClass_3:
    def __init__(self):
        self.myattr = 42
    
    def my_method(self):
        pass

my_obj = MyClass()

print(dir())
print(dir(my_obj))

print('\n')

#Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.
a = 23
b = 5

result = divmod(a, b)
print(result)

print('\n')

#Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
fruits = ['Banana','Apple','Pineapple','Mango']
for indice, fruit in enumerate(fruits):
    print(indice, fruit)

print('\n')

#This function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs).
expressions = ['2 + 3',' 5 * 7','10 / 2','8 - 4']
results = []

for expr in expressions:
    result = eval(expr)
    results.append(result)

print(results)

print('\n')

#This function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs).
codigo = """
def somar(a,b):
    return a+b

resultado = somar(2,3)
print(resultado)
"""
exec(codigo)

codigo_2 = """
def somar(a, b):
    return a + b

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = somar(a, b)

variaveis['resultado'] = resultado
"""

variaveis = {}
exec(codigo, globals(), {'variaveis': variaveis})
#print(variaveis['resultado'])

print('\n')

#Construct an iterator from those elements of iterable for which function is true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
ages = [5,12,17,19,24,32]

def MyFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(MyFunc, ages)

for x in adults:
    print(x)

print('\n')
  
#Return a floating point number constructed from a number or string x.
a = float(7)
print(a)
b = float('3.14')
print(b)
c = float(" -2.5 ")
print(c)
d = float("6.02e23")
print(d)
e = float("Infinity")
print(e)
f = float("-inf")
print(f)
g = float("nan")
print(g)  

print('\n')

#Convert a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument; however, there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language.
x = 123.456 
formatted_x = format(x,',.2f')
print(formatted_x)

#Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class
animals = frozenset(['gato','cachorro','pássaro','hamster'])
print(animals)

print('\n')

#Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute.
class Person_2:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
p = Person_2('Alice', 25)

name = getattr(p,'name')
print(name)

age = getattr(p, 'age')
print(age)

print('\n')

#Return the dictionary implementing the current module namespace. For code within functions, this is set when the function is defined and remains the same regardless of where the function is called.
def func():
    a = 1
    print(globals())
func()

print('\n')

#The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.)
class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
        
p = Pessoa('João', 30)

print(hasattr(p,'nome'))
print(hasattr(p,'altura'))

print('\n')

#Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
hash_value = hash('Hello World')
print(f"hash value of 'Hello World': {hash_value}")

my_list = [1,2,3,4,5]
hash_value_2 = hash(tuple(my_list))
print(f"hash value of 'my_list': {hash_value_2}")

my_dict = {"a": 1, "b": 2, "c": 3}
hash_value_3 = hash(frozenset(my_dict.items()))
print(f"hash value of 'my_dict': {hash_value_3}")

print('\n')

#Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console.
def sum_(a,b):
    """
    This function sum two numbers
    
    Arguments:
    a(int): The first number to sum
    b(int): The second number to sum
    
    Return:
    int: A sum of a and b
    """
    return a + b

help(sum)

print('\n')

#Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. If x is not a Python int object, it has to define an __index__() method that returns an integer.
# To obtain a hexadecimal string representation for a float, use the float.hex() method.
num = 2022
hex_sum = hex(num)
print(hex_sum)

print('\n')

#Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
a = [1,2,3]
b = a

print(id(a))
print(id(b))

c = [1,2,3]
print(id(c))

print('\n')

#Return the user value 
name = input('What is your name?: ')
print('Hello'+ name + '! Welcome :3')

print('\n')

#Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x defines __int__(), int(x) returns x.__int__(). If x defines __index__(), it returns x.__index__(). If x defines __trunc__(), it returns x.__trunc__(). For floating point numbers, this truncates towards zero.
z = int("1010", 2)
print(z) # Saída: 10

print('\n')

#The 'isinstance()' function in Python is used to determine if an object is an instance of a specified class or a subclass of that class
class Myclass:
    pass

class MyDerivedClass(Myclass):
    pass 

obj1 = Myclass()
obj2 = MyDerivedClass()

print(isinstance(obj1, Myclass))
print(isinstance(obj2, Myclass))
print(isinstance(obj1, MyDerivedClass))
print(isinstance(obj2, MyDerivedClass))

print('\n')

#The 'issubclass()' function takes two arguments: cls, which is the class that we want to check if it's a subclass of classinfo, and classinfo, which can be either a class or a tuple of classes.
def issubclass(cls, classinfo):
    if isinstance(classinfo, tuple):
        return any(issubclass(cls,c) for c in classinfo)
    elif isinstance(classinfo, type):
        return issubclass(cls, classinfo.__base__) or cls is classinfo
    else:
        raise TypeError("issubclass() arg 2 must be a class or a tuple of classes")

print('\n')

#Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument.
my_list = [1,2,3,4,5]

my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

print('\n')
   
#Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
text = "Hello World!"
print(len(text))

print('\n')

#Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.
my_string = '12345'
print(list(my_string))

print('\n')

#Update and return a dictionary representing the current local symbol table.
def my_function():
    name = 'Augusto'
    age = 19
    print(locals())

my_function()

print('\n')

#Return an iterator that applies function to every item of iterable, yielding the results.
def square(x):
    return x ** 2

my_list_ = [1,2,3,4,5]
result = map(square, my_list_) 

for item in result:
    print(item)
    
print('\n')

#Return the largest item in an iterable or the largest of two or more arguments.If multiple items are maximal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as sorted(iterable, key=keyfunc, reverse=True)[0] and heapq.nlargest(1, iterable, key=keyfunc).
numbers = [3,7,1,5,9,2]
largest_num = max(numbers)
print(f'The largest number in the list is: {largest_num}')

words = ["apple","banana","orange","pear","grape"]
longest_word = max(words, key=len)
print(f'The longest word in the list is: {longest_word}')

empty_list = []

default_value = 'no items'

max_value = max(empty_list, default=default_value)
print(f'The max value is: {max_value}')

print('\n')

#Return a “memory view” object created from the given argument. See Memory Views for more information.
b = bytearray(b'hello world')
m = memoryview(b)
print(bytes(m))

print('\n')

#Return the smallest item in an iterable or the smallest of two or more arguments.If multiple items are minimal, the function returns the first one encountered.
lower_value = min(5,3,8,2,10)
print(f"The lowest value is: {lower_value}")

#Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.
my_iter_ = iter([1,2,3,4,5])
print(next(my_iter_))

#Return a new featureless object. object is a base for all classes. It has methods that are common to all instances of Python classes. This function does not accept any arguments.
obj = object()
print(type(obj))

print('\n')

#Convert an integer number to an octal string prefixed with “0o”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer.
x = 10 
octal_str = oct(x)
print(octal_str)

print('\n')

#Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. See Reading and Writing Files for more examples of how to use this function.
try:
    file = open('example.txt','r')
    contents = file.read()
    file.close()
    print(contents)
except OSError:
    print("Could not open file")

print('\n')

#Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
char1 = 'a'
char2 = '€'
print(ord(char1))
print(ord(char2))

print('\n')

#Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod). The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.
x = pow(2,5)
print(x)

y = pow(2,5,7)
print(y)

z = pow(-9,0.5)
print(z)

print('\n')

#Return a property attribute. fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.
class Circle:
    def __init__(self, radius):
        self.radius = radius 
        
    def radius(self):
        """Get the radius of the circle"""
        return self.radius
    
    def radius(self, value):
        """Set the radius of the circle"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = value
    
    def radius(self):
        """Delete the radius of the circle"""
        del self.radius
        
c = Circle(5)
print(c.radius)
c.radius = 10
print(c.radius)

del c.radius 
print(hasattr(c, 'radius'))

print('\n')

#Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.
r = range(10)
for i in r:
    print(i, end=" ")
    
r2 = range(1,10,2)
print(r2.index(7))

print('\n')

#Return a string containing a printable representation of an object
class Point:
    def __init__(self, x,y):
        self.x = x 
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    
p = Point(1,2)
print(repr(p))

print('\n')

# Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
my_list_3 = [1,2,3,4,5]

for i in reversed(my_list_3):
    print(i)

print('\n')

#Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
num1 = 4.6
num2 = 3.4
num3 = 2.5

print(round(num1))
print(round(num2))
print(round(num3))

num4 = 3.14159
num5 = 2.71828
print(round(num4,3))
print(round(num5,2))

print('\n')

#Return a new set object, optionally with elements taken from iterable. set is a built-in class. See set and Set Types — set, frozenset for documentation about this class.
my_list_4 = [1,2,3,3,4,5,5]
my_set = set(my_list_4)

print(my_set)

my_set_2 = set()

my_set_2.add(1)
my_set_2.add(2) 
my_set_2.add(3)

print(my_set_2)

print('\n')

#This is the counterpart of getattr(). The arguments are an object, a string, and an arbitrary value. The string may name an existing attribute or a new attribute.
class Person:
    def __init__(self,name):
        self.name = name
        
person1 = Person('Julia <3')

setattr(person1,'age',20)

print(person1.name)
print(person1.age)


class Person_:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        
person2 = Person_('Gabriel',19)

setattr(person2,'age',20)

print(person2.name)
print(person2.age)

print('\n')

#Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop, and step which merely return the argument values (or their default).
class Slice:
    def __init__(self,start=None, stop=None, step=1):
        self.start = start 
        self.stop = stop 
        self.step = step 
        
    def __repr__(self):
        return f"slice({self.start}), ({self.stop}), ({self.step})"
    
    def __str__(self):
        return f"{self.start}, {self.stop}, {self.step}"
    
s1 = Slice(2)
print(s1)

s2 = Slice(2,10,2)
print(s2)

s3 = Slice(step=3) 
print(s3)

print('\n')

#Return a new sorted list from the items in iterable. Has two optional arguments which must be specified as keyword arguments.
def sorted(iterable, /, *, key=None, reverse=False):
    if key is not None:
        key_func = functools.cmp_to_key(lambda x: key(x).lower())
        iterable.sort(key=key_func, reverse=reverse)
    else:
        iterable.sort(reverse=reverse)
    
    return iterable

my_list_5 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(my_list_5)
print(sorted_list)

my_list_6 = ["apple","Banana","cherry","Durian"]
sorted_list_2 =  sorted(my_list_6)
print(sorted_list_2)
print('\n')

#Transform a method into a static method. A static method does not receive an implicit first argument, the @staticmethod form is a function decorator
class MyClass_:
    @staticmethod 
    def my_static_method(arg1, arg2):
        result = arg1 + arg2
        return result

result = MyClass_.my_static_method(10,20)
print(result)
print('\n')

#Return a str version of object. See str() for details, str is the built-in string class.
empty_str = str()
print(empty_str)

char_list = ['H','e','l','l','o']
hello_str = str(char_list)
print(hello_str)

byte_str = b"Hello"
hello_str_2 = str(byte_str, encoding="utf-8")
print(hello_str_2)

upper_str = "hello".upper()
lower_str = "WORLD".lower()
title_str = 'this is a title'.title()
print(upper_str)
print(lower_str)
print(title_str)

contains_o = "hello".__contains__("o")
startswith_h = "world".startswith("h")
endswith_d = "Python".endswith("d")
print(contains_o)
print(startswith_h)
print(endswith_d)

split_str = "apple,orange,banana".split(",")
join_str = "-".join(["hello","world"])
print(split_str)
print(join_str)
print('\n')

#Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.
numbers = [1, 2, 3, 4, 5]
total = sum(numbers, start=10)
print(total)
print('\n')

#Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.
class Animal:
    def __init__(self,name,age):
        self.name = name 
        self.age  = age

    def make_sound(self):
        print("The animal is barking!")

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed

    def make_sound(self):
        print("The dog is barking!")

class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    
    def make_sound(self):
        print("The cat meows!")        

dog = Dog("Rex",3, "Golden Retriever")
cat = Cat("Whiskers",2,"Grey")

dog.make_sound()
cat.make_sound()
print('\n')

#Rather than being a function, tuple is actually an immutable sequence type
empty_tuple = tuple()
print(empty_tuple)

my_tuple = ('apple','banana','orange')
print(my_tuple)

first_element = my_tuple[0]
last_element = my_tuple[-1]
print(first_element)
print(last_element)
print('\n')

#With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.__class__.
attrs = {'attr1': 1, 'attr2': 2}

MyClass = type('MyClass', (), attrs)

my_instance = MyClass()

print(my_instance.attr1)
print(my_instance.attr2)
print('\n')

#Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
class MyClass_:
    def __init__(self,value):
        self.value = value 
        self.data = vars(self)
        
obj_1 = MyClass_(1)
print(obj_1.data)

obj_2 = MyClass_("Hello")
print(obj_2.data)

obj_3 = MyClass_([1,2,3])
print(obj_3.data)
print('\n')

#Iterate over several iterables in parallel, producing tuples with an item from each one. More formally: zip() returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables.
a = [1,2,3]
b = ['a','b','c']
c = [True,False,True]

for x in zip(a,b,c, strict=True):
    print(x)
    
d = [1,2,3]
e = ['a','b','c','d']
f = [True,False]

for x in zip(a,b,c, strict=False):
    print(x)

print('\n')
    
#This function is invoked by the import statement. It can be replaced (by importing the builtins module and assigning to builtins.__import__) in order to change semantics of the import statement, but doing so is strongly discouraged as it is usually simpler to use import hooks.
module_name = 'math'
module = __import__(module_name)
print(module.sqrt(16))