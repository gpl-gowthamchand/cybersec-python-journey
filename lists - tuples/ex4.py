# Count even and odd numbers in a list.

numbers = [1,2,4,5,6,7,8,9,0]


even_count = 0 
odd_count = 0 


for i in numbers:
    if (i %2 == 0):
        even_count += 1
    else:
        odd_count += 1

print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")