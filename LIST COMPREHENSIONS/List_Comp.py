#Libs/modules



#Functions
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

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