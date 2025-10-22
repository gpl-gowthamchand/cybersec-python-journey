''' 
Check if a number is prime:

Use a for loop with else to print "Prime number" if not divisible by any number.'''

num = int (input("Enter a number: "))

if (num <= 1):
    print(f"{num} is non prime")

else:
    for i in range(2, num):
        if (num%i == 0):
            print(f"{num} is non prime")
            break 

    else:
        print(f"{num} is prime ")