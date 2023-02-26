import sys
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try: 
    linux_interaction()
except AssertionError as error:
    print(error)
    print('Linux function was not executed')
    
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error_:
    print(error_)
    print('Linux linux_interaction() function was not executed')
    
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')
finally:
    print('Cleaning up, every irrespective of any exceptions')
    
#-raise- allows you to throw an exception at any time.
#-assert- enables you to verify if a certain condition is met and throw an exception if it isn’t.
#In the -try- clause, all statements are executed until an exception is encountered.
#-except- is used to catch and handle the exception(s) that are encountered in the try clause.
#-else- lets you code sections that should run only when no exceptions are encountered in the try clause.
#-finally- enables you to execute sections of code that should always run, with or without any previously encountered exceptions.