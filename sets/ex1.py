'''
Create and Print

Create a set with these elements: 1, 2, 3, 4, 5
Print the set.
Add 6 to it.
Try adding 3 again and see what happens.
'''

numbers = {1, 2, 3, 4, 5}
print(numbers)              # {1, 2, 3, 4, 5}

numbers.add(6)
print(numbers)              # {1, 2, 3, 4, 5, 6}

numbers.add(3)
print(numbers)              # {1, 2, 3, 4, 5, 6}, 3 was already present, set wont allow duplicates so the newly added 3 was removed automatically