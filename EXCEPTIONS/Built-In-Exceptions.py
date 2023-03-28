#Imports 

import sys 

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
    
#A list of the notes of this exception, which were added with add_note(). This attribute is created when add_note() is called. New in version 3.11
class MyException_2(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__notes__ = []
        
    def add_note(self, note):
        if not isinstance(note, str):
            raise TypeError("note must be a string")
        self.__notes__.append(note)
        
try:
    raise MyException_2("Something went wrong")
except MyException_2 as e:
    e.add_note("Note 1")
    e.add_note("Note 2")
    print("Notes:", e.__notes__)
    
#All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.
class MathError(Exception):
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
        raise MathError('divide', a, b, 'Division by zero')
    else:
        return a/b

try:
    result = divide(10, 0)
except MathError as e:
    print(e)

#The base class for those built-in exceptions that are raised for various arithmetic errors: OverflowError, ZeroDivisionError, FloatingPointError.
class MyArithmeticError(ArithmeticError):
    pass

def do_calculator(x, y):
    try:
        result = x / y 
    except ZeroDivisionError:
        raise MyArithmeticError("Division by zero is not allowed")
    return result

try: 
    do_calculator(5,0)
except MyArithmeticError as e:
    print(f"Caught MyArithmeticError: {e}")
   
#Raised when a buffer related operation cannot be performed.
try:
    buffer = bytearray(10)
    buffer[20] = 1
except IndexError:
    print("Error: buffer operation could not be performed due to an index out of range")

#