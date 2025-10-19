# Accept three sides of a triangle and check whether it’s equilateral, isosceles, or scalene.

a, b, c = map(int, input("Enter three sides of triangle seperated by space: ").split())

if (a + b > c) and (a + c > b) and (b + c > a):  # if sum of two sides greater than third then it a proper triangle
    if ( a==b and a==c):
        print("It is equilateral")

    elif ( a==b or a==c or b==c):
        print("It is isosceles triangle")

    else:
        print("It is scalene triangle")

else:
    print("The given sides do not form a valid triangle.")

