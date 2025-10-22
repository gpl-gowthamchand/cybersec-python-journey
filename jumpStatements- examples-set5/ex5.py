# Write a program to print all odd numbers except multiples of 5 (use continue). 

for i in range (1, 50, 2):
    if (i%5==0):
        continue
    print(i)