'''
Find the largest and smallest number from a list
nums = [12, 5, 89, 34, 7, 56]
'''
nums = [12, 5, 89, 34, 7, 56]
largest = nums[0]
smallest = nums[0]
for i in nums:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i 

print(f"the largest: {largest}")
print(f"the smallest: {smallest}")



''' using the built in functiions
nums = [12, 5, 89, 34, 7, 56]
print(f"The largest: {max(nums)}")
print(f"The smallest: {min(nums)}")
'''
