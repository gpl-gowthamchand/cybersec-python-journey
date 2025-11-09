'''
Add & Remove Elements
Create a set {10, 20, 30, 40}.

Add 50 using add().

Remove 20 using remove().

Use discard(60) and observe what happens.'''

numbers = { 10, 20, 30, 40 }
print(numbers)              # {40, 10, 20, 30}

numbers.add(50)
print(numbers)               # {40, 10, 50, 20, 30}

numbers.remove(20)
print(numbers)               # {40, 10, 50, 30}

numbers.discard(60)
print(numbers)               # {40, 10, 50, 30}

''' 
.remove(x) it removes the element from the set, if element not found it returns an error
.discard(x) it removes the element from the set, returns no error if element not found
'''