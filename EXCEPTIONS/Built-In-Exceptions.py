#Imports 
import sys 
import math
import time
import errno
import os
import weakref
import asyncio
import ast
import numpy as np
import socket
import io
import signal
import requests
import subprocess
import warnings

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

#Raised when a mapping (dictionary) key is not found in the set of existing keys.
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('d','Key not found')
print(value)
print('\n')

#Raised when the user hits the interrupt key (normally Control-C or Delete). During execution, a check for interrupts is made regularly. The exception inherits from BaseException so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting.
try:
    for i in range(10):
        print(f"Running steps {i+1}...")
        time.sleep(1) # espera por 1 segundo
except KeyboardInterrupt:
    print("\nThe program was interrupt by the user :3")
print('\n')   
#Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects).
try:
    big_list = [1] * (10**9)
except MemoryError as e:
    print(f'Memory error: {e}')
print('\n')
  
#Raised when a local or global name is not found. This applies only to unqualified names. The associated value is an error message that includes the name that could not be found.
def geek_message():
    try:
        geek = "GeeksforGeeks"
        return geeksforgeeks
    except NameError:
        return "NameError occured. Some variable isn't defined."
print(geek_message())
print('\n')

#This exception is derived from RuntimeError. In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method, or while the class is being developed to indicate that the real implementation still needs to be added.
def get(self):
        raise NotImplementedError() 
print('\n')

#This exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or “disk full” (not for illegal argument types or other incidental errors).
try:
    with open('/only_reading/file.txt', 'w') as f:
        f.write('conteúdo')
except OSError as e:
    print(f'Error: {e.strerror}. Code Error: {e.errno}')
print('\n')

#A numeric error code from the C variable errno.
try:
    f = open('non_existent_file.tx','r')
except OSError as e:
   if e.errno == errno.ENOENT:
       print('File not found')
   else:
       print('Unknown error ocurred!')
print('\n')

#Under Windows, this gives you the native Windows error code. The errno attribute is then an approximate translation, in POSIX terms, of that native error code.
try:
    os.rename("original.txt","copy.txt")
except OSError as e:
    if hasattr(e,'winerror'):
        print(f'Native windows error: {e.winerror}')
    else:
        print(f'OS error: {e}')
print('\n')

#The corresponding error message, as provided by the operating system. It is formatted by the C functions perror() under POSIX, and FormatMessage() under Windows.
try:
    f = open('nonexistent_file.txt','r')
except OSError as e:
    print(f'Number Error: {e.errno}')
    print(f'Message Error: {e.strerror}')
print('\n')

#For exceptions that involve a file system path (such as open() or os.unlink()), filename is the file name passed to the function. For functions that involve two file system paths (such as os.rename()), filename2 corresponds to the second file name passed to the function.
try:
    os.remove('file.txt')
except OSError as e:
    print(f'Error {e.errno}: {e.strerror}')
    print(f'Filename: {e.filename}')
print('\n')

#Raised when the result of an arithmetic operation is too large to be represented. This cannot occur for integers (which would rather raise MemoryError than give up). However, for historical reasons, OverflowError is sometimes raised for integers that are outside a required range.
value_ = 5.0 

try:
    for i in range(1, 1000):
        value_ = value_**i
        print(value_)
except OverflowError as e:
    print("Overflow error happened")
    print(f'{e}, {e.__class__}')
print('\n')

#This exception is derived from RuntimeError. It is raised when the interpreter detects that the maximum recursion depth (see sys.getrecursionlimit()) is exceeded. New in version 3.5: Previously, a plain RuntimeError was raised.
def recursive_function(count):
    if count == 0:
        return
    recursive_function(count - 1)
    
try:
    recursive_function(sys.getrecursionlimit() + 1)
except RecursionError as e:
    print("Recursion error happened")
    print(f'{e}: {e.__class__}')
print('\n')

#This exception is raised when a weak reference proxy, created by the weakref.proxy() function, is used to access an attribute of the referent after it has been garbage collected. For more information on weak references, see the weakref module.
class ExpensiveObject(object):
    def __del__(self):
        print('(Deleting %s)' % self)

obj = ExpensiveObject
r = weakref.ref(obj)

print('obj: ',obj)
print('ref: ',r)  
print('r(): ',r())  

print('Deleting obj')  
del obj
print('r(): ',r()) 
print('\n')

#Raised when an error is detected that doesn’t fall in any of the other categories. The associated value is a string indicating what precisely went wrong.
def calculate_discount(price,discount):
    if discount > 1 or discount < 0:
        raise RuntimeError("Invalid discount value, must be between 0 and 1.")
    return price * (1 - discount)

try:
    calculate_discount(100,1.5)
except RuntimeError as e:
    print(f"Error: {e}")
print('\n')

#Raised by built-in function next() and an iterator's __next__() method to signal that there are no further items produced by the iterator.
def example_iterator():
    items = [1,2,3]
    for item in items:
        yield item

my_iterator = example_iterator()

try:
    while True:
        item = next(my_iterator)
        print(item)
except StopIteration:
    print("End of iteration")
print('\n')

#Must be raised by __anext__() method of an asynchronous iterator object to stop the iteration. New in version 3.5.
async def async_range(stop):
    for i in range(stop):
        yield i
        await asyncio.sleep(0.1)

async def main():
    async for i in async_range(10):
        print(i)
        if i == 5:
            raise StopAsyncIteration

try:
    asyncio.run(main())
except StopAsyncIteration:
    print("Async iteration stopped.")
print('\n')
    
#The name of the file the syntax error occurred in.
try:
    exec("print('Hello,world!'")
except SyntaxError as e:
    print(f'SyntaxError: {e.msg}')
    print(f'Ocurred in file {e.filename} at line {e.lineno}')
print('\n')

#Which line number in the file the error occurred in. This is 1-indexed: the first line in the file has a lineno of 1.
try:
    exec('for i in range(10): print(i')
except SyntaxError as e:
    print(f'Syntax error ocurred in {e.filename} at line {e.lineno}: {e.msg}')
print('\n')

#The column in the line where the error occurred. This is 1-indexed: the first character in the line has an offset of 1.
try:
    eval("print'Hello, world!'")
except SyntaxError as e:
    print(f"Syntax error in {e.filename} at line {e.lineno}, column {e.offset}: {e.msg}")
print('\n')

#The source code text involved in the error.
try:
    exec("x = 1 2")
except SyntaxError as e:
    print(f'Syntax error on line {e.lineno} in {e.filename}: {e.msg}')
    print(f'Offending code: {e.text.strip()}')
print('\n')

#Which line number in the file the error occurred ends in. This is 1-indexed: the first line in the file has a lineno of 1.
def parse_code(code_str):
    try:
        parsed = ast.parse(code_str)
    except SyntaxError as e:
        print("Syntax error in file '{}', line {}, col {}: {}".format(e.filename, e.lineno, e.offset, e.msg))
        print("Code excerpt:\n{}\n".format(e.text.strip()))
        print("Ends in line {}\n".format(e.end_lineno))

code_with_syntax_error = "x = 10\nif x = 5:\n    print('x is 5')"
parse_code(code_with_syntax_error)
print('\n')

#The column in the end line where the error occurred finishes. This is 1-indexed: the first character in the line has an offset of 1.
try:
    eval("x = 5 + 2 1")
except SyntaxError as e:
    print(f'Syntax Error: {e.text.strip()}')
    print(f'File: {e.filename}')
    print(f'Line: {e.lineno}, Column: {e.offset}')
    print(f'End of line: {e.end_lineno}, End of Column: {e.end_offset} ')
print('\n')

#Base class for syntax errors related to incorrect indentation. This is a subclass of SyntaxError.
def my_function():
    raise IndentationError("Indentation error ocurred")

try:
    my_function()
except IndentationError as e:
    print("Indentation error:", e)
except Exception as e:
    print("Other exception:", e)
print("\n")

#Raised when indentation contains an inconsistent use of tabs and spaces. This is a subclass of IndentationError.
def my_function_2():
    raise TabError("TabError occured")

try:
    my_function_2()
except TabError as e:
    print("TabError: ",e)
print('\n')

#Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope. The associated value is a string indicating what went wrong (in low-level terms).
try:
    x = 2 + 2
    if x == 4:
        raise SystemError("Something went wrong in the interpreter")
except SystemError as e:
    print("Oops! SystemError Ocurred:", e)
print('\n')

#This exception is raised by the sys.exit() function. It inherits from BaseException instead of Exception so that it is not accidentally caught by code that catches Exception. This allows the exception to properly propagate up and cause the interpreter to exit. When it is not handled, the Python interpreter exits; no stack traceback is printed.
try:
    sys.exit(0)
except SystemExit as e:
    print("Exited with:", e.code)
print('\n')

#The exit status or error message that is passed to the constructor. (Defaults to None.)
try:
    sys.exit(42)
except SystemExit as e:
    print("Exit code:", e.code)
print('\n')

#Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
def multiply_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments should be integers")
    return a * b

try:
    result = multiply_numbers(2, '3')
except TypeError as e:
    print("TypeError:", e)
print('\n')

#Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. This is a subclass of NameError.
def my_calculation():
    try:
        x += 1
    except UnboundLocalError:
        print("The variable x was called before the attribution")
        
my_calculation()
print('\n')

#Raised when a Unicode-related encoding or decoding error occurs. It is a subclass of ValueError. UnicodeError has attributes that describe the encoding or decoding error. For example, err.object[err.start:err.end] gives the particular invalid input that the codec failed on.
try:
    s = "Hello, world!🌍"
    b = s.encode('ascii')
except UnicodeError as err:
    print(f'Error to codify the string: {err}')
    print(f'The invalid input is: {err.object[err.start:err.end]}.') #the invalid therm 
else:
    print(f'The string was codified with sucess: {b}')
print('\n')

#The name of the encoding that raised the error.
s = 'Hello, World! 🐍\n🐍'

try:
    s.encode('ascii')
except UnicodeError as error:
    print('Codify error: ',error.encoding)
print('\n')

#A string describing the specific codec error
try:
    b = b'\xe9'
    b.decode("ascii")
except UnicodeError as error:
    print("Description error of codec: ", error.reason)
print('\n')

#The object the codec was attempting to encode or decode.
s = "🤖"
try:
    s.encode('ascii')
except UnicodeError as error:
    print('Codify error for the object: ', error.object)
print('\n')

#Raised when a Unicode-related error occurs during encoding. It is a subclass of UnicodeError.
my_string = "Hello, world!\ud83c"

try:
    my_string.encode('utf-8')
except UnicodeEncodeError as error:
    print("An error occured during the codification string:", error)
    print("The first valid index is:", error.start)
    print("The last invalid index: ",error.end)
print('\n')

#
my_bytes = b'\xc3\x28'

try:
    my_bytes.decode('utf-8')
except UnicodeDecodeError as error:
    print('An error occured during the decodification of the bytes sequence: ',error)
print('\n')

#Raised when the second argument of a division or modulo operation is zero. The associated value is a string indicating the type of the operands and the operation.
try:
    result = 10/ 0
except ZeroDivisionError:
    print("Oops! Division by zero isn't allowed")
print('\n')

print('>>The following exceptions are kept for compatibility with previous versions; starting from Python 3.3, they are aliases of OSError.')

try:
    file = open('non_existent_file.txt',"r")
except EnvironmentError as e:
    print("An error ocurred:", e)

try:
    file = open("non_existent_file.txt", "r")
except IOError as e:
    print("An I/O error occurred: ", e)

# Only available on Windows.
try:
    os.startfile("non_existent_file.txt")
except WindowsError as e:
    print("A Windows error ocurred:", e)
print('\n')
print('\n')

#Raised when an operation would block on an object (e.g. socket) set for non-blocking operation. Corresponds to errno EAGAIN, EALREADY, EWOULDBLOCK and EINPROGRESS.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setblocking(False)

try:
    s.connect(('12.0.0.1',8888))
except BlockingIOError as e:
    print(f'BlockingIOError occurred: {e}')
print('\n')

#In addition to those of OSError, BlockingIOError can have one more attribute:

#An integer containing the number of characters written to the stream before it blocked. This attribute is available when using the buffered I/O classes from the io module.
try:
    with io.StringIO() as file:
        file.write("Hello World")
        print(file.read())
        print(f"Charaters written: {file.characters_written}")
except AttributeError:
    print("AttributeError: 'StringIO' object has no attribute 'characters_written'")
print('\n')

#Raised when an operation on a child process failed. Corresponds to errno ECHILD.
try:
    os.waitpid(99999,0)
except ChildProcessError as e:
    print("Error: ",e)
print('\n')

#A base class for connection-related issues. Subclasses are BrokenPipeError, ConnectionAbortedError, ConnectionRefusedError and ConnectionResetError.
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost',8888))
except ConnectionError as e:
    print('An error occured in connection:', e)
print('\n')

#A subclass of ConnectionError, raised when trying to write on a pipe while the other end has been closed, or trying to write on a socket which has been shutdown for writing. Corresponds to errno EPIPE and ESHUTDOWN.
def send_message(message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 9999))
        s.send(message.encode())
    except BrokenPipeError:
        print('Error: BrokenPipeError - Connection was closed')
    except ConnectionRefusedError:
        print('Error: ConnectionRefusedError - Connection was refused')
    
send_message('Hello, world!')
print('\n')

#A subclass of ConnectionError, raised when a connection attempt is aborted by the peer. Corresponds to errno ECONNABORTED.
HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except ConnectionAbortedError:
        print("Connection error: aborted connection by the server.")
    except ConnectionRefusedError:
        print("Connection error: conexão recusada pelo servidor.")
    except Exception as e:
        print(f"Connection error: {e}")
print('\n')

#A subclass of ConnectionError, raised when a connection attempt is refused by the peer. Corresponds to errno ECONNREFUSED.
HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Error during the connection: connection was refused from server.")
print('\n')

#Raised when trying to create a file or directory which already exists. Corresponds to errno EEXIST.
try:
    os.mkdir("example")
    os.mkdir("example")
except FileExistsError:
    print(f"The directory already exist")
print('\n')

#Raised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT.
try:
    with open("non_existent_file.txt") as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found!")
print('\n')

#Raised when a system call is interrupted by an incoming signal. Corresponds to errno EINTR. Changed in version 3.5: Python now retries system calls when a syscall is interrupted by a signal, except if the signal handler raises an exception (see PEP 475 for the rationale), instead of raising InterruptedError.
try:
    time.sleep(10)
except InterruptedError:
    print("The operation was interrupted by a signal")
print('\n')

#Raised when a file operation (such as os.remove()) is requested on a directory. Corresponds to errno EISDIR
directory = "test_directory"

if os.path.exists(directory):
    print(f"{directory} already exists, skipping creation")
else:
    os.mkdir(directory)

try:
    with open(directory, "r") as file:
        data = file.read()
except IsADirectoryError:
    print(f"{directory} is a directory, cannot read from it")
except PermissionError:
    print(f"Creation denied")
finally:
    os.rmdir(directory)
print('\n')

#Raised when a directory operation (such as os.listdir()) is requested on something which is not a directory. On most POSIX platforms, it may also be raised if an operation attempts to open or traverse a non-directory file as if it were a directory. Corresponds to errno ENOTDIR.
try:
    files = os.listdir("myfile.txt")
except FileNotFoundError:
    print("File not found")
except NotADirectoryError as e:
    print(f"Erro: {e}")
print('\n')

#Raised when trying to run an operation without the adequate access rights - for example filesystem permissions. Corresponds to errno EACCES, EPERM, and ENOTCAPABLE.
filename = "example.txt"
directory = "/root/"

try:
    with open(os.path.join(directory, filename), "w") as file:
        file.write("Hello, World!")
except PermissionError:
    print(f"Failed to create {filename} in {directory}: Permission denied!")
except FileNotFoundError:
    print("File not found.... again!")
print('\n')

#exception ProcessLookupError Raised when a given process doesn’t exist. Corresponds to errno ESRCH.
process_name = "notepad.exe"
try:
    output = subprocess.check_output(f"tasklist /FI \"IMAGENAME eq {process_name}\"", shell=True)
    if process_name.encode() in output:
        print(f"O processo {process_name} está em execução.")
    else:
        raise ProcessLookupError(f"O processo {process_name} não está em execução.")
except subprocess.CalledProcessError:
    raise ProcessLookupError("Não foi possível obter a lista de processos.")
except ProcessLookupError:
    print("ProcessLookupError: error")
print("\n")

#Raised when a system function timed out at the system level. Corresponds to errno ETIMEDOUT.
server_address = ('localhost',8080)
timeout = 5

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(timeout)
    
    client_socket.connect(server_address)
    
    print("Connection Succeed")
except socket.timeout:
    raise TimeoutError(f"The connection expired after {timeout} seconds")
except socket.error as e:
    print(f"Error to connect: {e}")
finally:
    client_socket.close()
print('\n')

#
class MyWarning(Warning):
    pass

def my_function_2(x):
    if x < 0:
        warnings.warn("The argument x needs to be positive.", MyWarning)
    return x**2

result = my_function_2(-5)
print(result)
print('\n')

#Base class for warning categories.
class CustomWarning(Warning):
    def __init__(self,message,category):
        self.message = message
        self.category = category
        
    def __str__(self):
        return f"{self.category}: {self.message}"

warning = CustomWarning("This is a custom warning message.","Custom category")
print(warning)
print('\n')

#Base class for warnings generated by user code
message = "This is a user warning message"
category = UserWarning

warnings.warn(message,category)
print('\n')

#Base class for warnings about deprecated features when those warnings are intended for other Python developers. Ignored by the default warning filters, except in the __main__ module (PEP 565). Enabling the Python Development Mode shows this warning.The deprecation policy is described in PEP 387.
feature = "some_feature"
message = "This feature will be deprecated in the next version"

warnings.warn(f"{feature} is deprecated: {message}", DeprecationWarning)
print('\n')

#Base class for warnings about features which are obsolete and expected to be deprecated in the future, but are not deprecated at the moment.This class is rarely used as emitting a warning about a possible upcoming deprecation is unusual, and DeprecationWarning is preferred for already active deprecations.Ignored by the default warning filters. Enabling the Python Development Mode shows this warning.The deprecation policy is described in PEP 387.
function_name = "some_feature"
message = "This feature will be deprecated in a future version"

def deprecated_function():
    warnings.warn(f"{function_name} is pending deprecation: {message}", PendingDeprecationWarning)

deprecated_function()
print('\n')

#Base class for warnings about dubious syntax.
def some_function(a, b):
    if a or b:
        warnings.warn("Dubious syntax detected in some_function()", SyntaxWarning)
    return a + b

result = some_function(2, 3)
print(result)
print('\n')

#Base class for warnings about dubious runtime behavior.
def calculate_speed(distance,time):
    if time == 0:
        warnings.warn("Dubious runtime behaviour: time is zero", RuntimeWarning)
        return float('inf')
    else:
        return distance / time
    
speed = calculate_speed(10,0)
print(speed)
print('\n')

#Base class for warnings about deprecated features when those warnings are intended for end users of applications that are written in Python.
def deprecated_function():
    warnings.warn("This function is deprecated and will be removed in the future", FutureWarning)
    print("Excuting deprecated function...")

deprecated_function()
print('\n')

#Base class for warnings about probable mistakes in module imports.Ignored by the default warning filters. Enabling the Python Development Mode shows this warning.
try:
    import non_existent_module
except ImportError:
    warnings.warn("Probable mistake in module import", ImportWarning)
print('\n')

#Base class for warnings related to Unicode.
with open('meu_arquivo.txt', 'w') as f:
    f.write('This is the content of the file')

try:
    with open('meu_arquivo.txt', 'r', encoding='latin-1') as f:
        content = f.read()

    try:
        print(content)
    except UnicodeWarning as e:
        print(f"Catch a Unicode error: {e}")
        print(content.encode('utf-8').decode('utf-8'))

except FileNotFoundError as e:
    print(f"Cannot open the file: {e}")

f.close()
print('\n')

#Base class for warnings related to encodings. See Opt-in EncodingWarning for details. New in version 3.10.
def raise_encoding_warning():
    warnings.warn("This is another example EncodingWarning.", EncodingWarning)

warnings.warn("This is a generic warning.")

class EncodingWarning(Warning):
    pass

raise_encoding_warning()
print('\n')

#Base class for warnings related to bytes and bytearray.
class BytesWarning(Warning):
    pass

def raise_bytes_warning():
    warnings.warn("This is an example BytesWarning.", BytesWarning)

raise_bytes_warning()
print('\n')

#Base class for warnings related to resource usage. Ignored by the default warning filters. Enabling the Python Development Mode shows this warning. New in version 3.2.
class ResourceWarning(Warning):
    pass

def raise_resource_warning():
    warnings.warn("This is an example ResourceWarning.", ResourceWarning)

raise_resource_warning()
print('\n')

#
class ExceptionGroup(Exception):
    def __init__(self, msg, excs):
        self.msg = msg
        self.exceptions = excs

    def __str__(self):
        exception_list = '\n'.join(str(exc) for exc in self.exceptions)
        return f'{self.msg}\n\n{exception_list}'
try:
    raise ValueError('Invalid Value')
except ValueError as exc1:
    try:
        raise TypeError('Invalid Type')
    except TypeError as exc2:
        exception_group = ExceptionGroup('Multiple Exceptions: ', [exc1, exc2])
        raise exception_group
    except None: ####
        print()
print('\n')

#Both of these exception types wrap the exceptions in the sequence excs. The msg parameter must be a string. The difference between the two classes is that BaseExceptionGroup extends BaseException and it can wrap any exception, while ExceptionGroup extends Exception and it can only wrap subclasses of Exception. This design is so that except Exception catches an ExceptionGroup but not BaseExceptionGroup.
class BaseExceptionGroup(Exception):
    def __new__(cls,msg,excs):
        if all(isinstance(exc, Exception) for exc in excs):
            return ExceptionGroup(msg,excs)
        else:
            return super().__new__(cls)
    
    def __init__(self,msg,excs):
        super().__init__(msg)
        self.exceptions = excs
        
class ExceptionGroup(Exception):
    def __init__(self, msg, excs):
        if any(not isinstance(exc, Exception) for exc in excs):
            raise TypeError("Contained exceptions must be subclasses of Exceptions.")
        super().__init__(msg)
        self.exceptions = excs
    
    def __str__(self):
        exception_list = '\n'.join(str(exc) for exc in self.exceptions)
        return f'{self.msg}\n\n{exception_list}'
    
try:
    raise ValueError('Invalid Error')
except ValueError as exc1:
    try:
        raise TypeError('Invalid Type')
    except TypeError as exc2:
        exception_group = BaseExceptionGroup("Multiple Exceptions: ", [exc1,exc2])
        raise exception_group
    except None:
        print()
print('\n')

#