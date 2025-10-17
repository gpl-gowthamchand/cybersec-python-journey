# input   : a=1, b = -3, c = 2 
# output  : Roots:(2.0,1.0)

# quadratic equation --> ax² + bx + c = 0 
# here x = {-b +- √ (b²-4ac)} / 2a 
# so iam taking (b²-4ac) as d, and square root as power of 0.5 or 1/2


a, b, c = map(int, input("Enter 3 vals a b c seperated by space: ").split())

d = ((b**2) - 4*a*c)

root1 = (-b + (d**0.5)) / (2*a)

root2 = (-b - (d**0.5)) / (2*a)

print(f"Roots:({root1},{root2})")