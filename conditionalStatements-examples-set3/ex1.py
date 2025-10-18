# Write a program to check whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if (num>0):
    print(f"{num} is postive")

elif (num == 0):
    print(f"{num} is zero")

elif (num < 0):
    print(f"{num} is negative")

else:
    print("Enter a valid number")