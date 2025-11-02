# List methods 
 
fruits = [ "apple", "Grapes", "cherry", "Orange", "apple"]
print(fruits)                                 # ['apple', 'Grapes', 'cherry', 'Orange', 'apple']

## append(x) - adds items at end
fruits.append("mango")
print(fruits)                               # ['apple', 'Grapes', 'cherry', 'Orange', 'apple', 'mango']

## insert(i, x) - insert at index i 
fruits.insert(1, "Kiwi")
print(fruits)                               # ['apple', 'Kiwi', 'Grapes', 'cherry', 'Orange', 'apple', 'mango']

## remove(x) - removes first occurrence 
fruits.remove("apple")
print(fruits)                              # ['Kiwi', 'Grapes', 'cherry', 'Orange', 'apple', 'mango']

## pop(i) - remove element at index i 
fruits.pop(0)
print(fruits)                              # ['Grapes', 'cherry', 'Orange', 'apple', 'mango']

## pop() - removes at end
fruits.pop()
print(fruits)                         # ['Grapes', 'cherry', 'Orange', 'apple']

## clear - removes all elements 
fruits.clear()
print(fruits)                         # [] - now it is empty list


##########

nums = [ 10, 20, 40, 65, 3, 25, 8]
print(nums)                           # [10, 20, 40, 65, 3, 25, 8]

## sort() - sorts ascending 
nums.sort()
print(nums)                           # [3, 8, 10, 20, 25, 40, 65]

## reverse() - to reverse the list 
nums.reverse()
print(nums)                        # [65, 40, 25, 20, 10, 8, 3]

## count(x) - it counts the occurrences 
print(nums.count(25))              # 1

## index(x) - finds the index of element
print(nums.index(20))             # 3

## extend(iterable) - adds all elements from an iterable(like list or tuple) at end
li = ["grapes", "orange"]
nums.extend(li)
print(nums)             # [65, 40, 25, 20, 10, 8, 3, 'grapes', 'orange']

## copy() - copies elements into another

newlist = nums.copy()
print(newlist)




### append() VS extend()

a = [1, 2, 3, 4]
b = [5, 6]

a.append(b)
print(a)     # [1, 2, 3, 4, [5, 6]]


x = [5,6,7,8]
y = [0,1,2,3]

x.extend(y)
print(x)      # [5, 6, 7, 8, 0, 1, 2, 3]