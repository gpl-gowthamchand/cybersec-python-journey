# Write a program to find the first number divisible by both 3 and 5 between 1–100 (use break) 

for i in range(1, 101):
    if (i%3==0 and i%5==0):
        print(f"The first number divisible by both 3 and 5 is {i}")
        break