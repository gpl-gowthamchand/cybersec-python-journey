'''
Subset / Superset Check
Given:  
    x = {1, 2, 3}
    y = {1, 2, 3, 4, 5}
Check:
Is x a subset of y?
Is y a superset of x?
'''

x = {1, 2, 3}
y = {1, 2, 3, 4, 5}

print(x.issubset(y))     # True
print(y.issuperset(x))   # True