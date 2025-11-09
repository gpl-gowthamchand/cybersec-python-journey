'''
Copy a Set
Make a copy of a set {10, 20, 30} using .copy() 
and show that modifying one doesn’t affect the other.'''

set1 = {10, 20, 30}
set2 = set1.copy()

print(set1)        # {10, 20, 30}
print(set2)        # {10, 20, 30} 

l = {70, 89}
set2.update(l)
print(set2)        # {20, 70, 89, 10, 30}

print(set1)        # {10, 20, 30}