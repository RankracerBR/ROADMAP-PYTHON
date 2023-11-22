#Functions
from Square_Iter import SquareIterator
from Fib_Iter import FibonnacciIterator
from Inf_Fib import FibonacciInfIterator
from Sequence_Iter import SequenceIterator
import Math_Pipeline as mpl
from Reusable_Range import ReusableRange
from Sequence_Iterable import Iterable
from Stack import Stack
import asyncio
from Async_Rand import AsyncIterable
from time import sleep

#1
times = 0

while times < 3:
    print("Hello!")
    times += 1
print('\n')

#2
numbers = [1,2,3,4,5]

for number in numbers:
    print(number)
print('\n')

#3
def __iter__(self):
    return self

#4
class SequenceIterator:
    def __init__(self ,sequence):
        self._sequence = sequence
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

for item in SequenceIterator([1,2,3,4]):
    print(item)
print('\n')

#5
#How works internally in the class 
sequence = SequenceIterator([1,2,3,4])

'''Get an iterator over the data'''
iterator = sequence.__iter__()
while True:
    try:
        '''Retrieve the next item'''
        item = iterator.__next__()
    except StopIteration:
        break
    else:
        '''The loop's code block goes here'''
        print(item)

#
for square in SquareIterator([1,2,3,4,5]):
    print(square)
print('\n')

#
for fib_number in FibonnacciIterator():
    print(fib_number)
print('\n')

#
'''
for fib_number in FibonacciInfIterator():
    print(fib_number)
    sleep(2)
'''

#
for number in SequenceIterator([1,2,3,4]):
    print(number)
print('\n')

#
sample = range(20)

print(list(mpl.to_string(mpl.to_square(mpl.to_even(range(20))))))
print(list(mpl.to_string(mpl.to_cube(mpl.to_odd(range(20))))))
print('\n')

#
numbers_iter = SquareIterator([1,2,3,4])

for number in numbers_iter:
    print(number)

another_iter = SquareIterator([1,2,3,4])
for number in another_iter:
    print(number)
print('\n')

#
numbers_iter2 = SequenceIterator([1,2,3,4,5,6])

for number in numbers_iter2:
    if number == 4:
        break
    print(number)

print(next(numbers_iter2))

print(next(numbers_iter2))

#print(next(numbers_iter2)) StopIteration
print('\n')

#
numbers_iter3 = SequenceIterator([1,2,3,4,5,6])

#numbers_iter3[2] TypeError: 'SequenceIterator' object is not subscriptable

#numbers_iter3[1:3] TypeError: 'SequenceIterator' object is not subscriptable

print('\n')

#
numbers = ReusableRange(10)

print(list(numbers))

print(list(numbers))
print('\n')

#
'''
with open("sample_file.csv") as csv_file:
    next(csv_file)
    for line in csv_file:
        #process file line by line here...
        print(line)
'''

#
numbers_iter4 = SequenceIterator([1,2,3])
print(next(numbers_iter4))
print(next(numbers_iter4))
print(next(numbers_iter4))
#print(next(numbers_iter4)) StopIteration

numbers_iter5 = SequenceIterator([1,2,3])
print(next(numbers_iter5, 0))
print(next(numbers_iter5, 0))
print(next(numbers_iter5, 0))
print(next(numbers_iter5, 0))
print(next(numbers_iter5, 0))
print('\n')

#
for value in Iterable([1,2,3,4]):
    print(value)
print('\n')

#
'''
numbers = Iterable([1,2,3,4])
print(next(numbers)) TypeError: 'Iterable' object is not an iterator
'''

'''
letters = "ABCD"
print(next(letters)) TypeError: 'str' object is not an iterator
'''

'''
fruits = [
    'apple',
    'banana',
    'orange',
    'grape',
    'lemon',
]

print(next(fruits)) TypeError: 'list' object is not an iterator
'''

#
fruits = [
    "apple",
    "banana",
    "orange",
    "grape",
    "lemon",
]

print(iter(fruits))
print('\n')

#print(iter(42)) TypeError: 'int' object is not iterable

digits = [0,1,2,3,4,5,6,7,8,9]

print(reversed(digits))

print(list(reversed(digits)))

print('\n')

#
numbers2 = [1,2,3,4]
print(numbers2[0])
print(numbers2[2])

print('\n')

#
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(iter(stack))

for value in stack:
    print(value)

print('\n')

#
for number in [1,2,3,4]:
    print(number)

print('\n')

#
numbers3 = [1,2,3,4]

print([number**3 for number in numbers3])

print('\n')

#
numbers4 = [1,2,3,4]

one = numbers4[0]
two = numbers4[1]
three = numbers4[2]
four = numbers4[3]

print(one)
print(two)
print(three)
print(four)

print('\n')

#
numbers5 = [1,2,3,4]

one, two, three, four = numbers5

print(one)
print(two)
print(three)
print(four)

print('\n')

#
fruits2 = [
    "apple",
    "banana",
    "orange",
    "grape",
    "lemon",   
]

#print(next(fruits2)) TypeError: 'list' object is not an iterator

hello = "Hello, World!"

#print(next(hello)) TypeError: 'str' object is not an iterator

async def main():
    async for number in AsyncIterable(4):
        print(number)

print(asyncio.run(main()))