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

list = [65,66,67]
array_list = bytearray(list)

print(f'{empty_array}\n{array_string}\n{array_buffer}\n{array_list}')

#Return a new “bytes” object which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray.
bytes_obj = bytes('Hello, World!', encoding='utf-8')
print(bytes_obj)

print(bytes_obj[0])
print(bytes_obj[1])
print(bytes_obj[2])

list = [72,101,108,108,11,44,32,119,111,114,108,100,33]
bytes_obj2 = bytes(list)
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