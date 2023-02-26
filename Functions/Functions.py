import math 
def greet():
    print('Hello World') 
greet()
print('Outside the function')

def add_numbers(num1,num2):
    sum = num1 + num2 
    print('Sum: ', sum)
    
add_numbers(5,4)
#or add_numbers(num1 = 5, num2 = 4)

def find_square(num):
    result = num * num 
    return result 
square = find_square(3)
print('Square:', square)

square_root = math.sqrt(4)
print('Square Root of 4 is:',square_root)

power = pow(2,3)
print('2 to the power 3 is', power)

def get_square(num):
    return num * num 

for i in [1,2,3]:
    result = get_square(i)
    print(f'Square of {i} = {result}')