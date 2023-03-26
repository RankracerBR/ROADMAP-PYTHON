#The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined classes (for that, use Exception). If str() is called on an instance of this class, the representation of the argument(s) to the instance are returned, or the empty string when there were no arguments.
try:
    x = int(input("Type a number: "))
    if x < 0:
        raise ValueError("Negative numbers are not allowed")
except(ValueError, BaseException) as e:
    print("Error: ",e)
    
#