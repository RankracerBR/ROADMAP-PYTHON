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