import heapq

#1
heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)

print("Updated heap: ", heap)
print('\n')

#2
heap2 = [5,2,8,1,9]

smallest_element = heapq.heappop(heap)

print('Smallest element removed: ', smallest_element)
print('Updated heap: ', heap)
print('\n')

#3

heap3 = [3,5,8,2,1]

new_element = 4

smallest_element2 = heapq.heappushpop(heap3,new_element)

print('New element added: ', new_element)
print('Smalles Element removed: ', smallest_element2)
print('Updated Heap: ', heap)
print('\n')

#4
list1 = [9,4,7,2,1,5]

heapq.heapify(list1)

print("Heap transformed: ", list1)
