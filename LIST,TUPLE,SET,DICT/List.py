#Variables
l1 = []

l2 = [1,2,'3',4]

l3 = list()

l4 = list((1,2,3))

l5 = l2[2:]

print(f'List l1: {l1}')
print(f'List l2: {l2}')
print(f'List l3: {l3}')
print(f'List l4: {l4}')
print(l5)

#Acessing the variables
print(f'The first element of the lis l2 is: {l2[0]}.')

print(f'The third element of the list l4 is: {l4[2]}.')

print(f'The second and third element of the list l2: {l2[1:3]}.')

l1.append(5)
print('Append 5 to the list l1: {}'.format(l1))

l1.remove(5)
print(f'Removed element 5 from the list l1: {l1}')

l2[2] = 5
print(f'Modified l2: {l2}')