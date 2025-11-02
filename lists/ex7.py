'''
Get only the unique elements from two lists:
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
 Expected: [1, 2, 5, 6]
'''



a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = []
for i in a :
    if i not in b:
        c.append(i)

for i in b:
    if i not in a:
        c.append(i)

print(c)


''' 
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

unique = list(set(a) ^ set(b))  # ^ means symmetric difference
print(unique)
'''