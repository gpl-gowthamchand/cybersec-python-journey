# Calculate the factorial of a number using a while loop. 

num = int(input("Enter a number: "))
numToIterate = num
factorial = 1 

if numToIterate == 0:
    factorial = 1
    print(f"the factorial of {num} is {factorial}")

else:
    while numToIterate > 0:
        factorial = factorial*numToIterate 
        numToIterate = numToIterate-1
    print(f"the factorial of {num} is {factorial}")



''' using function
def fact(num):
    if num == 1:
        return 1

    else:
        return num*fact(num-1)

print(fact(5))
'''
