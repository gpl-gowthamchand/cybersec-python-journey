'''
Tuple 
    - ordered, immutable collection of items 

    tuple_name = (item1, item2, item3, ...)

''' 

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers)         # (1, 2, 3, 4, 5, 6, 7, 8, 9)

## accessing elements through indexing 
print(numbers[0])       # 1 
print(numbers[1])       # 2 
print(numbers[-1])      # 9 - last element 


## tuple slicing 
print(numbers[1:5])    # (2, 3, 4, 5)
print(numbers[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1)

## tuple operations
a = (1,2,3)
b = (5,6)
print(a+b)            # (1, 2, 3, 5, 6)
print(a*2)            # (1, 2, 3, 1, 2, 3)
print( 6 in b )       # True


## looping through  tuples 
words = ("ash", "fire", "water", "air")
for word in words:
    print(word)

## tuple from generator expression 
squares = tuple( x*x for x in range(5) )
print(squares)                       # (0, 1, 4, 9, 16)

