#Fuctions
import os
import random
import math
import sys
import collections

'''os module'''
#
#os.mkdir("c:\\tempdir")

#os.chdir("c:\\temp")

print(os.getcwd())

#os.rmdir("d:\\temp")

#os.chdir("..")

#os.rmdir("temp")

print(os.listdir("c:\\Users"))
print('\n')

'''random module'''
#
print(random.random())

print(random.randint(1,100))

print(random.randint(1,100))

print(random.randrange(1, 10))

print(random.randrange(1,10,2))

print(random.randrange(0,101,10))

print(random.choice('computer'))

print(random.choice([12,23,45,67,65,43]))

print(random.choice([12,23,45,67,65,43]))

numbers = [12,23,45,67,65,43]

print(random.shuffle(numbers))

print(numbers)

print(random.shuffle(numbers))

print(numbers)
print('\n')

'''math module'''
#
print(math.pi)

print(math.e)
print('\n')

'''Trigonometric functions'''
#
print(math.radians(30))

print(math.degrees(math.pi/6))

print(math.sin(0.5235987755982988))

print(math.cos(0.5235987755982988))

print(math.tan(0.5235987755982988))

print(math.log10(10))

print(math.e**10)

print(math.pow(4,4))

print(math.sqrt(100))

print(math.sqrt(3))
print('\n')

'''Representation functions'''
#
print(math.ceil(4.5867))

print(math.floor(4.5687))

print('\n')

'''sys module'''
#
#python Modules.py Augusto 20
#print("My name is {}. I am {} years old".format(sys.argv[1], sys.argv[2]))

print(sys.maxsize)

print(sys.path)

print(sys.version)
print('\n')

'''collections module'''
#