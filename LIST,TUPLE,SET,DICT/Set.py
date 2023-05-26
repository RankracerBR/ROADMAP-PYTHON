import time

s1 = {1,2,3}
s2 = set([1, 2, 3, 4])

print(f'Set s1: {s1}')
print(f'Set s2: {s2}')

names1 = set(["Glory","Tony","Joel","Dennis"])
names2 = set(["Morgan","Joel","Tony","Emmanuel","Diego"])

names_union = names1.union(names2)

names_union = names1 | names2

print(names_union)

names_intersection = names1.intersection(names2)
names_intersection = names1 & names2

print(names_intersection)

#Return all the elements that are present in the first set, but not in the second one
names_difference = names1.difference(names2)

names_difference = names1 - names2 

print(names_difference)

def find_element(iterable):
    """Find an element in range 0-4999 (included) in an iterable and pass."""
    for i in range(5000):
        if i in iterable:
            pass

s = set(range(10000000))

l = list(range(10000000))

start_time = time.time()
find_element(s)
print(f'Finding an element in a set took: {time.time() - start_time} seconds')

start_time = time.time()
find_element(l)
print(f'Finding an element in a list took: {time.time() - start_time} seconds')