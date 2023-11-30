#Libs/modules
import timeit
import random


#Functions
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

def get_price(price):
    return price if price > 0 else 0

def get_weather_data():
    return random.randrange(90, 110)



def get_price2(txn):
    return txn * (1 + TAX_RATE)

def get_prices_with_map():
    return list(map(get_price2, txns))

def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]

def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price2(txn))
    return prices


#Variables
squares = []
for i in range(10):
    squares.append(i * i)

print(squares)      
print('\n')

#
txns = [1.09,23.56,57.84,4.56,6.78]
TAX_RATE = .08

final_prices = map(get_price_with_tax,txns)
print(list(final_prices))
print('\n')

#

squares2 = [i * i for i in range(10)]
print(squares2)
print('\n')

#
final_prices2 = [get_price_with_tax(i) for i in txns]
print(final_prices2)
print('\n')

#
sentence = 'The rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']

print(vowels)
print('\n')

sentence2 = 'The rocket, who was named Ted, came back \ from mars because he missed his friends'

consonants = [i for i in sentence2 if is_consonant]

print(consonants)
print('\n')

#
original_prices = [1.25,-9.45, 10.22, 3.78, -5.92,1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)
print('\n')

princes = [get_price(i) for i in original_prices]
print(prices)
print('\n')

#
quote = "Life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)
print('\n')

#
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps)
print('\n')

#
cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}
print(temps)
print('\n')

matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)
print('\n')

#
flat = [num for row in matrix for num in row]
print(flat)
print('\n')

#
matrix = [
    [0,0,0],
    [1,1,1],
    [2,2,2],
]

flat = []

for row in matrix:
    for num in row:
        flat.append(num)

print(flat)

#
#print(sum(i * i for i in range(1000000000))) #Dont run this

#
#print(sum(map(lambda i: i*i, range(1000000000))))

#
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100000)]

print(timeit.timeit(get_prices_with_map, number=100))
print(timeit.timeit(get_prices_with_comprehension, number=100))
print(timeit.timeit(get_prices_with_loop, number=100))