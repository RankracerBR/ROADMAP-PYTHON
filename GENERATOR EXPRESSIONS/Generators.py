#Libs/modules
import cProfile
import sys

#Functions
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def is_palindrome(num):
    #Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    
    if num == reversed_num:
        return num
    else:
        return False

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        
def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = 1
        num += 1

#Variables
'''
file_name = ''
csv_gen = (row for row in open(file_name))
row_count = 0

for row in csv_gen:
    row_count += 1
    
print(f"Row count is: {row_count}")
'''

#
a = range(5)
print(list(a))
print('\n')


'''
for i in infinite_sequence():
    print(i, end=" ")
'''

gen = infinite_sequence()

print(next(gen))

print(next(gen))

print(next(gen))

print(next(gen))

print('\n')

#
'''
for i in infinite_sequence():
    pal = is_palindrome(i)
    if pal:
        print(i)
'''

#
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))
print(nums_squared_lc)
print(nums_squared_gc) #Generator Expression, mostra na memória onde se localiza
print('\n')

#
nums_squared_lc2 = [i ** 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc2))

nums_squared_gc2 = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc2))
print('\n')

#
cProfile.run('sum([i * 2 for i in range(1000)])')
print('\n')
cProfile.run('sum((i * 2 for i in range(1000)))')
print('\n')

#
multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
#print(next(multi_obj))

#

letters = ['a','b','c','y']
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)

#

pal_gen = infinite_palindromes()
'''
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
'''

for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        #pal_gen.throw(ValueError("We don't like large palindromes"))
        pal_gen.close()
    pal_gen.send(10 ** (digits))