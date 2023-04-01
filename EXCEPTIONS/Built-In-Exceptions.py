#Imports 

import sys 
import math

#The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined classes (for that, use Exception). If str() is called on an instance of this class, the representation of the argument(s) to the instance are returned, or the empty string when there were no arguments.
try:
    x = int(input("Type a negative number: "))
    if x < 0:
        raise ValueError("Negative numbers are not allowed >:3")
except(ValueError, BaseException) as e: ##
    print("Error: ",e)
print('\n')

#The tuple of arguments given to the exception constructor
class MyException(Exception):
    def __init__(self,arg1,arg2):
        self.arg1 = arg1 #
        self.arg2 = arg2 #
        super().__init__(f"MyException was raised with args: {arg1}, {arg2}")
        
try: 
    raise MyException("value", "value2")    
except MyException as e:
    print(f"Exception args: {e.args}")
print('\n')

#This method sets tb as the new traceback for the exception and returns the exception object. It was more commonly used before the exception chaining features of PEP 3134 became available.
try:
    1 / 0
except ZeroDivisionError as e:
    
    tb = sys.exc_info()[2]
    
    new_exception = ValueError("Something went wrong").with_traceback(tb) #
    
    print(new_exception)
print('\n')

#Add the string note to the exception’s notes which appear in the standard traceback after the exception string. A TypeError is raised if note is not a string.
class CustomException(Exception):
    def __init__(self, message):
        self.notes = []
        super().__init__(message)

    def add_note(self, note): #
        if not isinstance(note, str):
            raise TypeError("Note must be a string")
        self.notes.append(note)

try:
    raise CustomException("Something went wrong!")
except CustomException as e:
    e.add_note("Additional information about the error")
    print(e)
print('\n')

#A list of the notes of this exception, which were added with add_note(). This attribute is created when add_note() is called. New in version 3.11
class MyException_2(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__notes__ = []
        
    def add_note(self, note):
        if not isinstance(note, str):
            raise TypeError("note must be a string") ##
        self.__notes__.append(note)
        
try:
    raise MyException_2("Something went wrong")
except MyException_2 as e:
    e.add_note("Note 1")
    e.add_note("Note 2")
    print("Notes:", e.__notes__)
print('\n')

#All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.
class MathError(Exception): ##
    """Exception raised for errors in math operations."""
    
    def __init__(self, operation, operand1, operand2, message="Error in math operation"):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message}: {self.operation}({self.operand1}, {self.operand2})'

def divide(a, b):
    if b == 0:
        raise MathError('divide', a, b, 'Division by zero') ##
    else:
        return a/b

try:
    result = divide(10, 0)
except MathError as e:
    print(e)
print('\n')

#The base class for those built-in exceptions that are raised for various arithmetic errors: OverflowError, ZeroDivisionError, FloatingPointError.
class MyArithmeticError(ArithmeticError):
    pass

def do_calculator(x, y):
    try:
        result = x / y 
    except ZeroDivisionError: ##
        raise MyArithmeticError("Division by zero is not allowed")
    return result

try: 
    do_calculator(5,0)
except MyArithmeticError as e:
    print(f"Caught MyArithmeticError: {e}")
print('\n')

#Raised when a buffer related operation cannot be performed.
try:
    buffer = bytearray(10) ##
    buffer[20] = 1
except IndexError:
    print("Error: buffer operation could not be performed due to an index out of range")
print('\n')

#The base class for the exceptions that are raised when a key or index used on a mapping or sequence is invalid: IndexError, KeyError. This can be raised directly by codecs.lookup().
class InvalidKeyError(LookupError): ##
    pass

class InvalidIndexError(LookupError):##
    pass

def get_value(my_list,index):
    try:
        return my_list[index]
    except IndexError:
        raise InvalidIndexError(f"Invalid Index: {index}")

my_list = [1,2,3]
index = 5 

try: 
    value = get_value(my_list,index)
except InvalidIndexError as e:
    print(str(e))
print('\n')

#Raised when an assert statement fails.
def divide(a,b):
    assert b != 0, "'b' cannot be zero" #assert verify the cases
    return a / b

try: 
    result = divide(10,0)
except AssertionError as e:
    print(str(e))
print('\n')

#Raised when an attribute reference (see Attribute references) or assignment fails. (When an object does not support attribute references or attribute assignments at all, TypeError is raised.)
class MyClass:
    def __init__(self, name):
        self.name = name 
        
my_object = MyClass("Jhon")

try:
    my_object.age
except AttributeError as e:
    print(str(e))
print('\n')

#Not currently used.
try:
    resultado = 1.0 / 0.0 
    if math.isnan(resultado):
        raise FloatingPointError("Operand result is NaN")
except FloatingPointError as e:
    print("A error occured on the floating point: ",e)
except Exception as e:
    print("Occured an error: ",e)
print('\n')

#Raised when a generator or coroutine is closed; see generator.close() and coroutine.close(). It directly inherits from BaseException instead of Exception since it is technically not an error.
def my_generator(stop_value):
    for i in range(10):
        if i == stop_value:
            print("Closing the generator")
            raise GeneratorExit
        yield i

try:
    gen = my_generator(5) 
    for item in gen:
        print(item)
        
except GeneratorExit:
    print("Generator Closing.")
print('\n')

#Raised when the import statement has troubles trying to load a module. Also raised when the “from list” in from ... import has a name that cannot be found.The name and path attributes can be set using keyword-only arguments to the constructor.
try:
    import my_module
except ImportError as e:
    print("Import Error:", e)
print('\n')

#A subclass of ImportError which is raised by import when a module could not be located. It is also raised when None is found in sys.modules.New in version 3.6.
try:
    if "my_module" in sys.modules:
        sys.modules["my_module"] = None 
    import my_module 
except ModuleNotFoundError as e:
    print("Import error:",e)
print('\n')

#Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, TypeError is raised.)
my_list_2 = [1,2,3]

try:
    print(my_list_2[3])
except IndexError as e:
    print("Index error:",e)
print('\n')

#