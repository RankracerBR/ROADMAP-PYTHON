#abs if receives a negative number it will return the distance of the positive number from the 0
class number_string:
    def __init__(self,value):
        self.value = value 
    
    def __abs__(self):
        absolute = self.value.replace('negative'," ")
        return absolute 

number = number_string("negative ten")
print(abs(number))

#Return True if any element of the iterable is true. If the iterable is empty, return False
def all(iterable):
    for element in iterable:
        if element:
            return True 
    return False

#Convert an integer number to a binary string prefixed with “0b”
print(bin(3))
print(bin(-19))

print(format(14, '#b'), format(14, 'b'))
print(f'{14:#b}', f'{14:b}')

#Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure
class bool(int):
    def __new__(cls, x=False):
        if x: 
            return super().__new__(cls, 1)
        else:
            return super().__new__(cls, 0)
    def __init__(self, x=False):
        pass
    
#This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments
def example(x):
    if x < 0:
       pass #breakpoint()
    else:
        print('O valor de x é:',x)
example(-8)    

#Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256    
empty_array = bytearray()
string = 'Hello World!'
array_string = bytearray(string, 'utf-8')

buffer = b'\x00\x01\x02'
array_buffer = bytearray(buffer)

list = [65,66,67]
array_list = bytearray(list)

print(f'{empty_array}\n{array_string}\n{array_buffer}\n{array_list}')

#Return a new “bytes” object which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray
bytes_obj = bytes('Hello, World!', encoding='utf-8')
print(bytes_obj)

print(bytes_obj[0])
print(bytes_obj[1])
print(bytes_obj[2])

list = [72,101,108,108,11,44,32,119,111,114,108,100,33]
bytes_obj2 = bytes(list)
print(bytes_obj2)

#Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed
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

#Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). source can either be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how to work with AST objects.The filename argument should give the file from which the code was read; pass some recognizable value if it wasn’t read from a file ('<string>' is commonly used)
source = "print('Hello, World!')"
code = compile(source, filename="<string>", mode="exec")
exec(code)

#