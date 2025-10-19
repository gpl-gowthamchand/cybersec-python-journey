# simple calculator

a, b = map(int, input("Enter two numbers with space: ").split())

op = input("Select operation (+ - * /): ")

if (op == "+"):
    print(f"Addition of {a} and {b} is {a + b}")

elif (op == "-"):
    print(f"Subtraction of {a} and {b} is {a + b}")

elif (op == "*"):
    print(f"Multiplication of {a} and {b} is {a + b}")

elif (op == "/"):
    print(f"Division of {a} and {b} is {a + b}")

else:
    print(f"{op} is not a valid operator, give a valid one")