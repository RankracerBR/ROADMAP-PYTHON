import threading
import queue
from queue import SimpleQueue
from dataclasses import dataclass, field
from typing import Any
import threading
import time


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
    print("The queue has size limit: ", list1.maxsize)
else:
    print("The queue has infinite size")

list1.put(1)
list1.put(2)
list1.put(3)

print("Items in the queue: ", list1.qsize())

try:
    list1.put(4, block=False)
except queue.Full:
    print("The queue is full. Is not possible to put more items.")

while not list1.empty():
    item = list1.get()
    print("Removing the item: ",item," of the queue.")

print("Itens in the queue: ", list1.qsize())
print('\n')

#Constructor for a priority queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.The lowest valued entries are retrieved first (the lowest valued entry is the one that would be returned by min(entries)). A typical pattern for entries is a tuple in the form: (priority_number, data).If the data elements are not comparable, the data can be wrapped in a class that ignores the data item and only compares the priority number:

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

priority_list = queue.PriorityQueue(maxsize=5)

if priority_list.maxsize > 0:
    print("The priority queue has the size limit: ", priority_list.maxsize)
else:
    print("The priority queue has infinte size.")

priority_list.put(PrioritizedItem(3, "Item 1"))
priority_list.put(PrioritizedItem(1, "Item 2"))
priority_list.put(PrioritizedItem(2, "Item 3"))

print("Items in the priority queue: ", priority_list.qsize())

try:
    priority_list.put(PrioritizedItem(4, "Item 4"), block=False)
except queue.Full:
    print("The priority queue is full")

while not priority_list.empty():
    item = priority_list.get()
    print("Removing the item: ", item.item, " of the priority. Priority: ", item.priority)

print("Items in the priority: ", priority_list.qsize())
print('\n')

#Constructor for an unbounded FIFO queue. Simple queues lack advanced functionality such as task tracking.New in version 3.7.

queue1 = SimpleQueue()

queue1.put(10)
queue1.put(20)
queue1.put(30)

print("Is the queue empty?", queue1.empty())

print("Next element in the queue: ", queue1.get())

print("Current size of the queue: ", queue1.qsize())

queue1 = SimpleQueue()

print("Is the queue empty?", queue1.empty())

print('\n')

#Exception raised when non-blocking put() (or put_nowait()) is called on a Queue object which is full.

queue2 = queue.Queue(maxsize=2)

queue2.put(10)
queue2.put(20)

try:
    queue2.put(30, block=False)
except queue.Full:
    print("The queue is full. Is not possible to add more items with the method put().")

try:
    queue2.put_nowait(30)
except queue.Full:
    print("The queue is full. Is not possible to add more items with the method put_nowait().")
print('\n')

#Equivalent to get(False).

queue3 = Queue()

queue3.put(1)
queue3.put(2)
queue3.put(3)

try:
    item = queue3.get_nowait()
    print("Obtained item: ", item)
except Exception as e:
    print("The queue is empty. Error: ", e)
print('\n')


#Indicate that a formerly enqueued task is complete. Used by queue consumer threads. For each get() used to fetch a task, a subsequent call to task_done() tells the queue that the processing on the task is complete.If a join() is currently blocking, it will resume when all items have been processed (meaning that a task_done() call was received for every item that had been put() into the queue).Raises a ValueError if called more times than there were items placed in the queue.

def execute_task(task_id, queue):
    print("Executing task ", task_id)
    time.sleep(1)
    print("Task", task_id, "done")
    queue4.put(None)  

queue4 = Queue()

for i in range(3):
    thread = threading.Thread(target=execute_task, args=(i, queue4))
    thread.start()

print("All the tasks finished!")
print('\n')

#Blocks until all items in the queue have been gotten and processed.The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer thread calls task_done() to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero, join() unblocks.
def process_queue(queue):
    while True:
        item = queue.get()
        print(f"Processing item: {item}")
        queue.task_done()
    
task = queue.Queue()

num_threads = 3

for _ in range(num_threads):
    t = threading.Thread(target=process_queue, args=(task,))
    t.daemon = True
    t.start()

for i in range(10):
    task.put(i)

task.join()

print("All the tasks are fisinhed")
print('\n')

#

queue5 = SimpleQueue()

size = queue5.qsize()
print("Size of the queue", size)

queue5.put("Item 1")
queue5.put("Item 2")
queue5.put("Item 3")

size = queue5.qsize()
print("Size of the queue: ", size)

item = queue5.get()
print("Removed item: ", item)

size = queue5.qsize()
print("Size of the queue: ", size)
print('\n')

#