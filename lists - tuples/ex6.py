# Remove duplicates from a list (hint: convert to set and back to list). 

list_of_numbers = [1, 2, 3, 5, 5, 6, 3, 7, 8, 9]

list_new = []

for i in list_of_numbers:
    if (i not in list_new):
        list_new.append(i)
print(list_new)



## using set()

numbers = [1, 2, 3, 5, 5, 6, 3, 7, 8, 9]

numbers = list(set(numbers))
print(numbers)
