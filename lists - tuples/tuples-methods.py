## Tuple methods 

" Since tuple immutable it has only TWO built in methods "

# count() - returns the no of times an item occurred in a tuple 
numbers = (1, 4, 2, 3, 4, 2, 2, 4, 5, 6, 9, 2, 8)
print(numbers.count(2))

# index() - returns the index of first occrence of an item 
print(numbers.index(4))


## list functions 



# len() - returns the total no of elements aka length 
print(len(numbers))

# max() - returns the largest item in a tuple - if items are of same comparable type 
print(max(numbers))

# min() - returns the smallest 
print(min(numbers))

# sum() - returns the sum of all numeric elements 
print(sum(numbers))

# sorted() - returns the list of sorted elements in new list (does not modify the original tuple)
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# del - this statement can be used to delete an entire tuple, but not individual elements.
del(numbers)
print(numbers)  # output : NameError: name 'numbers' is not defined. Did you forget to import 'numbers'? (because numbers tuple is deleted)