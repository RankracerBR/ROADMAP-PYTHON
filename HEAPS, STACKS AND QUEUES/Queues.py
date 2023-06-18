import threading
import queue
from dataclasses import dataclass, field
from typing import Any

#Constructor for a FIFO queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.

class Queue:
    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self.queue = []
        self.lock = threading.Lock()

    def put(self, item):
        with self.lock:
            while self.maxsize > 0 and len(self.queue) >= self.maxsize:
                self.lock.release()
                self.lock.acquire()
            self.queue.append(item)

    def get(self):
        with self.lock:
            while len(self.queue) == 0:
                self.lock.release()
                self.lock.acquire()
            item = self.queue.pop(0)
            return item



q = Queue(maxsize = 4)
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())
print('\n')

#Constructor for a LIFO queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.

list1 = queue.LifoQueue(maxsize = 3)

if list1.maxsize > 0:
    print("The list has size limit: ", list1.maxsize)
else:
    print("The list has infinite size")

list1.put(1)
list1.put(2)
list1.put(3)

print("Items in the list: ", list1.qsize())

try:
    list1.put(4, block=False)
except queue.Full:
    print("The list is full. Is not possible to put more items.")

while not list1.empty():
    item = list1.get()
    print("Removing the item: ",item," of the list.")

print("Itens in the list: ", list1.qsize())
print('\n')

#Constructor for a priority queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.The lowest valued entries are retrieved first (the lowest valued entry is the one that would be returned by min(entries)). A typical pattern for entries is a tuple in the form: (priority_number, data).If the data elements are not comparable, the data can be wrapped in a class that ignores the data item and only compares the priority number:

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

priority_list = queue.PriorityQueue(maxsize=5)

if priority_list.maxsize > 0:
    print("The priority list has the size limit: ", priority_list.maxsize)
else:
    print("The priority list has infinte size.")

priority_list.put(PrioritizedItem(3, "Item 1"))
priority_list.put(PrioritizedItem(1, "Item 2"))
priority_list.put(PrioritizedItem(2, "Item 3"))

print("Items in the priority list: ", priority_list.qsize())

try:
    priority_list.put(PrioritizedItem(4, "Item 4"), block=False)
except queue.Full:
    print("The priority list is full")

while not priority_list.empty():
    item = priority_list.get()
    print("Removing the item: ", item.item, " of the priority. Priority: ", item.priority)

print("Items in the priority: ", priority_list.qsize())
print('\n')

#