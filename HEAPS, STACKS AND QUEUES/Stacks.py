from collections import deque
from queue import LifoQueue

#1
mystack = []

mystack.append('a')
mystack.append('b')
mystack.append('c')

print(mystack)

mystack.pop()
mystack.pop()
mystack.pop()
#mystack.pop() IndexError
print(mystack)

print('\n')

#2
mystack2 = deque()
mystack2.append('a')
mystack2.append('b')
mystack2.append('c')
print(mystack2)

mystack2.pop()
mystack2.pop()
mystack2.pop()
#mystack2.pop() IndexError
print(mystack2)

#3
mystack3 = LifoQueue()