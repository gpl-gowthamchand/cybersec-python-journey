## Sets 
''' collection of unique and unordered items, 
   - unordered , no index
   - unique, no duplicates
   - mutable
   - heterogenous.. can contain different data type elements

   set_name = {item1, item2, item3, ..}
   set_name = set([item1, item2, item3, ..])

'''
## creating sets 
fruits = {"apple", "banana", "cherry"}
print(fruits)       # {'cherry', 'apple', 'banana'}

numbers = set([1, 2, 3, 3, 4, 5])
print(numbers)       #{1, 2, 3, 4, 5} - here duplicate 3 automatically removed

## empty set - use set() method, not curly braces'{}' for empty set 
empty_set = set()        # this creates empty set
print(type(empty_set))   # <class 'set'>

empty_set2 = {}          # this creates a dict, not set
print(type(empty_set2))  # <class 'dict'>

## accessing elements - no indexing, use loops.
for fruit in fruits:
    print(fruit)

## adding elements 
# add() - add one element 
fruits.add("mango")
print(fruits)         # {'apple', 'mango', 'cherry', 'banana'}

# update() - add multiple elements
fruits.update(["grapes","sapota"])
print(fruits)              # {'mango', 'grapes', 'apple', 'sapota', 'cherry', 'banana'}

## removing elements 
# remove() - removes items, gives error if not found
# discard() - removes items, no error if not found
# pop() - removes random element 
# clear() - empties the entire set 

fruits.discard("banana")
print(fruits)          # {'grapes', 'apple', 'sapota', 'cherry', 'mango'}

fruits.pop()
print(fruits)         # {'apple', 'sapota', 'cherry', 'mango'}

## copying a set - use copy() method otherwise both vars points to the same set
a = {1, 2, 3}
b = a.copy()
print(b)  # {1, 2, 3}


## frozenset() - immutable set 
fs = frozenset([1, 3, 4, 5])