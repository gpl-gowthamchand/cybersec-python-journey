'''
Set Operations
Given:
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
Find:
Union
Intersection
Difference (a - b)
Symmetric Difference
'''

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))                    # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))             # {3, 4}
print(a.difference(b))   # a-b       # {1, 2}
print(a.symmetric_difference(b))     # {1, 2, 5, 6}