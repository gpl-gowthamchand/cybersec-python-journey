'''
Factorial of a Number
Write a function factorial(n) that returns the factorial using a loop.'''

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

result = factorial(5)
print(result)
