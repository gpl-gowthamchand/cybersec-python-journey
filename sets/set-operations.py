### set operations 

## union [ | or .union() ] - combines items from both sets, and removes duplicates 

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)            # {1, 2, 3, 4, 5}
print( a.union(b) )     # {1, 2, 3, 4, 5}


## intersection [ & or .intersection() ] - keeps only common elements 

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)        # {3}
print( a.intersection(b) ) #{3}


## difference [ - or .difference() ] - keeps items that are in one set but not both 

a = {1, 2, 3}
b = {3, 4, 5}
print(a-b)        # {1, 2}
print(b-a)   # {4, 5}


## symmetric difference [ ^ or symmetric_difference() ] - keeps the items that are in either sets but not in both

a = {1, 2, 3}
b = {3, 4, 5}
print(a^b)     # {1, 2, 4, 5}
print(a.symmetric_difference(b))



### set comparison 

## issubset() - checks if all elements of one set exits in another
print( {1,2}.issubset({1,2,3})) # True

## issuperset() - checks if one set contains another
print( {1,2,3}.issuperset({1,2}))    # True

## isdisjoint() - checks if two sets have no common elements 
print( {1,2,}.isdisjoint({4,5}))     # True
