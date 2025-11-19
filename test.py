def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

nums = [1, 2, 3, 4, 5, 6, 8]
print(filter_even(nums))



def is_even(n):
    return n % 2 == 0

def filter_even(numbers):
    return list(filter(is_even, numbers))
