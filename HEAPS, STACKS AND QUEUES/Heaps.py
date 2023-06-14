import heapq
import itertools

#Push the value item onto the heap, maintaining the heap invariant.

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)

print("Updated heap: ", heap)
print('\n')

#Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

heap2 = [5,2,8,1,9]

smallest_element = heapq.heappop(heap)

print('Smallest element removed: ', smallest_element)
print('Updated heap: ', heap)
print('\n')

#Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

heap3 = [3,5,8,2,1]

new_element = 4

smallest_element2 = heapq.heappushpop(heap3,new_element)

print('New element added: ', new_element)
print('Smalles Element removed: ', smallest_element2)
print('Updated Heap: ', heap)
print('\n')

#Transform list x into a heap, in-place, in linear time
list1 = [9,4,7,2,1,5]

heapq.heapify(list1)

print("Heap transformed: ", list1)

#Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.The value returned may be larger than the item added. If that isn’t desired, consider using heappushpop() instead. Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.The module also offers three general purpose functions based on heaps.

heap4 = [3,5,8,10,2]

new_item = 1
smallest_item = heapq.heapreplace(heap,new_item)

print('Smallest item removed from the heap: ', smallest_item)
print('Updated heap: ', heap)

#Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).Has two optional arguments which must be specified as keyword arguments.key specifies a key function of one argument that is used to extract a comparison key from each input element. The default value is None (compare the elements directly).reverse is a boolean value. If set to True, then the input elements are merged as if each comparison were reversed. To achieve behavior similar to sorted(itertools.chain(*iterables), reverse=True), all iterables must be sorted from largest to smallest.Changed in version 3.5: Added the optional key and reverse parameters

iterable1 = [1,4,7,10] 
iterable2 = [2,5,8,11]

merged_iterable = heapq.merge(iterable1,iterable2)

for value in merged_iterable:
    print(value)
print('\n')

#Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key, reverse=True)[:n].

numbers = [10,5,8,20,3,15]

largest_numbers = heapq.nlargest(3, numbers)

print("Largest Numbers: ", largest_numbers)
print('\n')

#Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key)[:n].

numbers2 = [10,5,8,20,3,15]

smallest_element3 = heapq.nsmallest(3, numbers2)

print("Smallest Numbers: ", smallest_element3)
print('\n')

#A heapsort can be implemented by pushing all values onto a heap and then popping off the smallest values one at a time:

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h,value)
    return [heapq.heappop(h) for i in range(len(h))]

heapsort_name = heapsort([1,3,5,7,9,2,4,6,8,0])

for value in heapsort_name:
    print(value)
print('\n')

#Heap elements can be tuples. This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked:

h = []
heapq.heappush(h,(5,'write code'))
heapq.heappush(h,(7, 'released product'))
heapq.heappush(h,(1, 'write spec'))
heapq.heappush(h,(3, 'create tests'))
delete = heapq.heappop(h)
print(delete)
print('\n')

#
pq = []
entry_finder = {}
REMOVED = '<removed-task>'
counter = itertools.count()

def add_task(task, priority = 0):
    'Add a new task or update the priority of an existing task.'
    if task in entry_finder:
        itertools.remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED. Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED
    
def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')