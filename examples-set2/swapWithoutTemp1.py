a = 5
b = 2 

print(f"before swap a:{a}, b:{b}")


a, b = b, a  # this creates a temp tuple and unpacks it

print(f"after swap a:{a}, b:{b}")