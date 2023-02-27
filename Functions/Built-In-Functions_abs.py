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

#    
empty_array = bytearray()
string = 'Hello World!'
array_string = bytearray(string, 'utf-8')

buffer = b'\x00\x01\x02'
array_buffer = bytearray(buffer)

list = [65,66,67]
array_list = bytearray(list)

print(f'{empty_array}\n{array_string}\n{array_buffer}\n{array_list}')
