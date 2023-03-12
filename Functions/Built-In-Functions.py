#Imports
from asyncio import sleep,run
#abs if receives a negative number it will return the distance of the positive number from the 0.
class number_string:
    def __init__(self,value):
        self.value = value 
    
    def __abs__(self):
        absolute = self.value.replace('negative'," ")
        return absolute 

number = number_string("negative ten")
print(abs(number))

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
    
#This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments.
def example(x):
    if x < 0:
       pass #breakpoint()
    else:
        print('O valor de x é:',x)
example(-8)    

#Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256.    
empty_array = bytearray()
string = 'Hello World!'
array_string = bytearray(string, 'utf-8')

buffer = b'\x00\x01\x02'
array_buffer = bytearray(buffer)

list_ = [65,66,67]
array_list = bytearray(list_)

print(f'{empty_array}\n{array_string}\n{array_buffer}\n{array_list}')

#Return a new “bytes” object which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray.
bytes_obj = bytes('Hello, World!', encoding='utf-8')
print(bytes_obj)

print(bytes_obj[0])
print(bytes_obj[1])
print(bytes_obj[2])

list_ = [72,101,108,108,11,44,32,119,111,114,108,100,33]
bytes_obj2 = bytes(list_)
print(bytes_obj2)

#Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed.
def my_func():
    print('Hello, World!')
    
class MyClass:
    def __call__(self):
        print('Hello from MyClass! :3')

obj = MyClass()

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

#Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types — dict for documentation about this class.
dicionario_1 = {'Nome': 'João', 'Idade': 30, 'Cidade':'João Pessoa'}#keys
dicionario_2 = dict(nome='Maria',idade=25, cidade='Natal')#constructor
dicionario_3 = dict([('Nome', 'Pedro'), ('idade', 35), ('Cidade', 'Campina Grande')])#tuples

print(dicionario_1)
print(dicionario_2)
print(dicionario_3)

#If you pass an object as an argument to dir(), it will attempt to return a list of valid attributes for that object. This can be useful to inspect the attributes and methods available on an object, especially if you are working with an unfamiliar class or module.
class MyClass:
    def __init__(self):
        self.myattr = 42
    
    def my_method(self):
        pass

my_obj = MyClass()

print(dir())
print(dir(my_obj))

#Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.
a = 23
b = 5

result = divmod(a, b)
print(result)

#Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
fruits = ['Banana','Apple','Pineapple','Mango']
for indice, fruit in enumerate(fruits):
    print(indice, fruit)
    
#his function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs).
expressions = ['2 + 3',' 5 * 7','10 / 2','8 - 4']
results = []

for expr in expressions:
    result = eval(expr)
    results.append(result)

print(results)

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

#Convert a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument; however, there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language.
x = 123.456 
formatted_x = format(x,',.2f')
print(formatted_x)

#Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class
animals = frozenset(['gato','cachorro','pássaro','hamster'])
print(animals)

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

#Return the dictionary implementing the current module namespace. For code within functions, this is set when the function is defined and remains the same regardless of where the function is called.
def func():
    a = 1
    print(globals())
func()

#The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.)
class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
        
p = Pessoa('João', 30)

print(hasattr(p,'nome'))
print(hasattr(p,'altura'))

#Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
hash_value = hash('Hello World')
print(f"hash value of 'Hello World': {hash_value}")

my_list = [1,2,3,4,5]
hash_value_2 = hash(tuple(my_list))
print(f"hash value of 'my_list': {hash_value_2}")

my_dict = {"a": 1, "b": 2, "c": 3}
hash_value_3 = hash(frozenset(my_dict.items()))
print(f"hash value of 'my_dict': {hash_value_3}")

#Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console.
def sum(a,b):
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

#Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. If x is not a Python int object, it has to define an __index__() method that returns an integer.
# To obtain a hexadecimal string representation for a float, use the float.hex() method.
num = 2022
hex_sum = hex(num)
print(hex_sum)

#Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
a = [1,2,3]
b = a

print(id(a))
print(id(b))

c = [1,2,3]
print(id(c))

#Return the user value 
name = input('What is your name?: ')
print('Hello'+ name + '! Welcome :3')

#Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x defines __int__(), int(x) returns x.__int__(). If x defines __index__(), it returns x.__index__(). If x defines __trunc__(), it returns x.__trunc__(). For floating point numbers, this truncates towards zero.
z = int("1010", 2)
print(z) # Saída: 10

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
    
#Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument.
my_list = [1,2,3,4,5]

my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
    
#Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
text = "Hello World!"
print(len(text))

#Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.
my_string = '12345'
print(list(my_string))

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
#
x = 10 
octal_str = oct(x)
print(octal_str)

#