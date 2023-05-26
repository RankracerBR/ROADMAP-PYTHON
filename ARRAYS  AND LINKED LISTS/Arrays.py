import array

#A new array whose items are restricted by typecode, and initialized from the optional initializer value, which must be a list, a bytes-like object, or iterable over elements of the appropriate type.
my_array = array.array('i',[1,2,3,4,5])

print(my_array)

my_array.append(6)

print(my_array)

print(my_array[2])

my_array.remove(4)

print(my_array)

print(len(my_array))

my_list = my_array.tolist()

print(my_list)
print('\n')

#The typecode character used to create the array.
type_codes = array.typecodes
print(type_codes)
print('\n')

#The length in bytes of one array item in the internal representation.
my_array = array.array('i')

item_size = my_array.itemsize

print("Size of a item in array: ", item_size, "bytes")
print('\n')

#Return a tuple (address, length) giving the current memory address and the length in elements of the buffer used to hold array’s contents
my_array = array.array('i', [1,2,3,4,5])

buffer_info = my_array.buffer_info()

address = buffer_info[0]
length = buffer_info[1]

buffer_size = length * my_array.itemsize

print('Memory Address: ', address)
print('Length: ', length)
print('Buffer Size (in bytes): ', buffer_size)
print('\n')

#