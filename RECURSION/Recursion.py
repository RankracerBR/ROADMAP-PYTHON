from sys import getrecursionlimit, setrecursionlimit
setrecursionlimit(2000)
print(getrecursionlimit())

def function():
    x = 10
    function()

#function() RecursionError: maximum recursion depth exceeded

def countdown(n):# Recursive
    print(n)
    if n > 0:
        countdown(n - 1)

countdown(5)
print('\n')

def countdown_2(n): #Non-Recursive
    while n >= 0:
        print(n)
        n -= 1

countdown_2(10)
print('\n')

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(4))
print('\n')

def factorial_2(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value

factorial_2(4)