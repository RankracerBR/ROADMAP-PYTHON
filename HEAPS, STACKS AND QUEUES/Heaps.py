import heapq

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