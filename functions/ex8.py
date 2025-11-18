''' 
Sum of a List
Write a function list_sum(lst) that returns the sum of all numbers in a list.'''

def list_sum(lst):
    total = 0
    for item in lst:
        total = total + item
    return total

lst = [1,3,4,5,6,7,9]
result = list_sum(lst)
print(result)


''' short way using sum() method 

def list_sum(lst):
    return sum(lst)

'''