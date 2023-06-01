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

#“Byteswap” all items of the array. This is only supported for values which are 1, 2, 4, or 8 bytes in size; for other types of values, RuntimeError is raised. It is useful when reading data from a file written on a machine with a different byte order.
def byteswap_array(arr):
    if arr.itemsize not in (1,2,4,8):
        raise RuntimeError("Byteswap is only supported for 1,2,4 or 8 bytes")
    
    arr.byteswap()

my_array = array.array('i',[1,2,3,4,5])
print("Before change the bytes: ", my_array)

byteswap_array(my_array)
print("After change the bytes: ", my_array)
print('\n')

#Return the number of occurrences of x in the array.
def count_occurrences(arr, x):
    count = arr.count(x)
    return count

my_array = array.array('i', [1,2,3,2,4,2,5])
element = 2

occurencies = count_occurrences(my_array,element)
print("Occurrencies numbers of the element: ", element, "in array: ", occurencies)
print('\n')

#Append items from iterable to the end of the array. If iterable is another array, it must have exactly the same type code; if not, TypeError will be raised. If iterable is not an array, it must be iterable and its elements must be the right type to be appended to the array.
def extend_array(arr,iterable):
    if isinstance(iterable, array.array):
        if arr.typecode != iterable.typecode:
            raise TypeError("Type codes of the arrays do not match")
        arr.extend(iterable)
    else:
        arr.extend(iterable)
        
my_array = array.array('i', [1,2,3])
my_iterable = [4,5,6]

extend_array(my_array, my_iterable)
print("Array after the extension: ", my_array)
print('\n')

#Appends items from the string, interpreting the string as an array of machine values (as if it had been read from a file using the fromfile() method).New in version 3.2: fromstring() is renamed to frombytes() for clarity.
def frombytes_example(s, typecode):
    arr = array.array(typecode)
    arr.frombytes(s)
    
    return arr

my_string = b'\x01\x02\x03\x04\x05'
my_typecode = 'B'

my_array = frombytes_example(my_string,my_typecode)
print("Resultant Array: ", my_array)
print('\n')

#Read n items (as machine values) from the file object f and append them to the end of the array. If less than n items are available, EOFError is raised, but the items that were available are still inserted into the array.
def fromfile(arr, file_path, n):
    try:
        with open(file_path, 'rb') as file_obj:
            values = array.array(arr.typecode)
            values.fromfile(file_obj, n)
            arr.extend(values)
    except EOFError as e:
        arr.extend(values[:e.args[0]])
    except FileNotFoundError:
        print(f"The file '{file_path}' cannot be found.")

my_array = array.array('i')
file_path = 'data.bin'
fromfile(my_array, file_path, 4)
print(my_array)
print('\n')

#Append items from the list. This is equivalent to for x in list: a.append(x) except that if there is a type error, the array is unchanged.
def fromlist(arr,lst):
    for item in lst:
        try:
            arr.append(item)
        except TypeError:
            pass
    return arr

a = [1,2,3]
b = [4, 'five', 6]
fromlist(a,b)
print(a)
print('\n')

#Extends this array with data from the given unicode string. The array must be a type 'u' array; otherwise a ValueError is raised. Use array.frombytes(unicodestring.encode(enc)) to append Unicode data to an array of some other type.
def fromunicode(arr,s):
    if arr.typecode != 'u':
        raise ValueError("This array must be of type 'u'")
    
    if isinstance(s, str):
        s = s.encode('utf-8')

a = array.array('u','hello')
s = ' world'
fromunicode(a, s)
print(a)
print('\n')

#