#1
def sequence_generator(sequence):
    for item in sequence:
        yield item

print(sequence_generator([1,2,3,4]))
print('\n')

for number in sequence_generator([1,2,3,4]):
    print(number)

#2
print([item for item in [1,2,3,4]]) #List Comprehension
print('\n')

#3
(item for item in [1,2,3,4]) #Generator Expression

generator_expression = (item for item in [1,2,3,4])
for item in generator_expression:
    print(item)
print('\n')

#4
def square_generator(sequence):
    for item in sequence:
        yield item**2
 
    
for square in square_generator([1,2,3,4,5]):
    print(square)
print('\n')

#5
def fibonacci_generator(stop=10):
    current_fib, next_fib = 0, 1
    for _ in range(0, stop):
        fib_number = current_fib
        current_fib, next_fib = (
            next_fib, current_fib + next_fib
        )
        yield fib_number

print(list(fibonacci_generator()))
print(list(fibonacci_generator(15)))
print('\n')

#6
def fibonnaci_generator(stop=10):
    current_fib, next_fib = 0, 1
    index = 0
    while True:
        if index == stop:
            return
        index += 1
        fib_number = current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
        yield fib_number
print('\n')

#7
def square_list(sequence):
    squares = []
    for item in sequence:
        squares.append(item**2)
    return squares

numbers = [1,2,3,4,5]
print(square_list(numbers))

    
    