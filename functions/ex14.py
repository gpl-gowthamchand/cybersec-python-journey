'''
Filter Even Numbers (using filter())
Write a function filter_even(numbers) that returns a list of even numbers.
'''

def filter_even(nums):
    return list(filter(lambda x : x%2==0, nums))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_even(nums))