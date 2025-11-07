'''
Dictionary Comprehension

Create a dictionary of squares from 1 to 10:
 Output: {1: 1, 2: 4, 3: 9, ..., 10: 100}
'''

squares = {x : x**2 for x in range(1,11)}
print(squares)