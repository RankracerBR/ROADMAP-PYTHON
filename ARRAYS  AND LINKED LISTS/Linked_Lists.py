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
#queue = fila
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
#stacks = pilha
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
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

list2 = LinkedList()
print(list2)

first_node = Node("a")
list2.head = first_node
print(list2)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(list2)
print('\n')

#7
class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
     
class LinkedList2:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node2(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node2(data=elem)
                node = node.next
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
list3 = LinkedList2(["a", "b", "c", "d", "e"])

for node in list3:
    print(node)

print('\n')
#8
class Node3:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
     
class LinkedList3:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node3(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node3(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def add_first(self,node):
        node.next = self.head
        self.head = node
        
list4 = LinkedList3()

list4.add_first(Node3("b"))
for node in list4:
    print(node)

list4.add_first(Node3("a"))
for node in list4:
    print(node)

#9
class Node4:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
        
class LinkedList4:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node4(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node4(data = elem)
                node = node.next
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next     
    
    def add_last(self,node):
        if self.head is None:
            self.head = node
            return 
        for current_node in self:
            pass
        current_node.next

list5 = LinkedList4(["a","b","c","d"])

list5.add_last(Node4("e"))
print(list5)

list5.add_last(Node4("f"))
print(list5)