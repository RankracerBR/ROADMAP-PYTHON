from collections import deque

# 1
graph = {
    1: [2,3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
}
print(graph)
print('\n')

#2
deque([])

d1 = deque(['a','b','c'])
print(d1)

d2 = deque('abc')
print(d2)

d3 = deque([{'data': 'a'}, {'data':'b'}])
print(d3)
print('\n')

#3
list1 = deque("abcde")
print(list1)

list1.append("f")
print(list1)

list1.pop()
print(list1)

list1.appendleft("z")
print(list1)

list1.popleft()
print(list1)
print('\n')

#4
queue = deque()

queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

#5
history = deque()

history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")

print(history)

history.popleft()
print(history)

history.popleft()
print(history)

#6
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
    def __repr__(self):
        return self.data
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next()
        nodes.append("None")
        return " -> ".join(nodes)

list_2 = LinkedList()
print(list_2)

first_node = Node("a")
list_2.head = first_node
print(first_node)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(first_node)
print(second_node)

#7
