'''
Reverse Keys and Values

Input : d = {"a": 1, "b": 2, "c": 3}
Output: {1: "a", 2: "b", 3: "c"}
'''

d = {"a": 1, "b": 2, "c": 3} 
d2 ={}
for k, v in d.items():
    d2[v]= k

d.clear()
d.update(d2)
print(d)


''' shorter version 
d = {"a": 1, "b": 2, "c": 3}
reversed_d = {v: k for k, v in d.items()}
print(reversed_d)
'''