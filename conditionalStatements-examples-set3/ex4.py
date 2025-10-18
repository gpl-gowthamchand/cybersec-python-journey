# Write a program to find the greatest of two numbers.

a, b = map(int, input("Enter two numbers separated with space: ").split())

if (a > b):
    print(f"{a} is greater than {b}")

elif(a == b):
    print(f"Both {a} and {b} are equal")

else:
    print(f"{b} is greater than {a}")