''' 
Lists 
   - ordered , mutable, can contain duplicates and different datatype items

list = [item1, item2, item3]

'''

list1 = [1, 2, 3, 4]
list2 = [ "A", "b"]
list3 = [5, "g", 1.2]

print(list3)


## acessing elements - through indexing
numbers = [10, 20, 30, 40, 50]
print(numbers[1])                 # 20
print(numbers[-1])                # 50

## list slicing
print(numbers[1:4])               # [20, 30, 40]
print(numbers[ : 3])              # [10, 20, 30]
print(numbers[ : : 2])            # [10, 30, 50]


## list is mutable - list cab be changed after creation
nums = [1,2,3]
nums[1] = 10
print(nums)                  # [1, 10, 3]

## List operations 
a = [1, 2, 3]
b = [4, 5]
print(a+b)             # [1, 2, 3, 4, 5]
print(a * 2)           # [1, 2, 3, 1, 2, 3]
print( 3 in a )        # True 

## looping through lists 
fruits = ["Grapes", "cherry", "orange"]
for f in fruits:
   print(f)


## List comprehension - a compact way to create lists 
squares = [ x*x for x in range(5)]
print(squares)                       # [0, 1, 4, 9, 16]