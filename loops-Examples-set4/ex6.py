# Display the Fibonacci sequence up to n terms.

num = int(input("Enter a number: "))

if (num<=0):
    print("Enter a positve number")
elif(num == 1 ):
    print("0")
elif (num == 2):
    print("0\n1")
else:
    a = 0
    b = 1

    print(a)
    print(b)
    for i in range( num -2):
        c = a+b 
        print(c)
        a = b 
        b = c