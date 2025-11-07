'''
Merge Two Dictionaries

a = {"x": 10, "y": 20}
b = {"z": 30, "y": 25}

Merge both and print the result.
If a key exists in both, keep the value from b.
'''

a = {"x": 10, "y": 20}
b = {"z": 30, "y": 25}

c = {}

for k in a:
    c[k] = a[k]  # add all from a
for k in b:
    c[k] = b[k]  # overwrite if exists

print(c)


'''
a = {"x": 10, "y": 20}
b = {"z": 30, "y": 25}

c = a.copy()   # start with all key-value pairs from a
c.update(b)    # update with b (overwrites duplicates)

print(c)
'''