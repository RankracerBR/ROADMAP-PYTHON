#Implicit Conversion
integer_number = 123 
float_number = 1.23

new_number = integer_number + float_number 

print(f'Value:{new_number}')
print(f'{type(new_number)}')
#Python sempre vai converte os menores valores para valores maiores, no caso o float é maior que o int

#Addition of string and integer
num_string = '12'
num_integer = 23 

print('Data type of num_string before Type Casting:',type(num_string))

#Explicit Conversion
num_string = int(num_string)
print('Data type of num_string after Type Casting:',type(num_string))

num_sum = num_integer + num_string

print('Sum:',num_sum)
print('Data type of num_sum:',type(num_sum))