''' 
Generate a pattern of numbers:
1
1 2
1 2 3
1 2 3 4
'''

for i in range(6):
    for j in range(1,i):
        print(f"{j} ", end="")
    print()