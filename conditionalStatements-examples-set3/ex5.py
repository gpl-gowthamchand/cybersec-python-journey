# Write a program to find the greatest of three numbers.

a, b, c = map(int, input("Enter three numbers separated with space: ").split())

if (a > b and a > c):
    print(f"{a} is greater than {b} and {c}")

elif (b > a and b > c):
    print(f"{b} is greater than {a} and {c}")

else:
    print(f"{c} is greater than {a} and {b}")