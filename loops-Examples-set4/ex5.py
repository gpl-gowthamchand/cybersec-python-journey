# Calculate the factorial of a number using a while loop. 

num = 3
fact = 1

if num == 1:
    fact = 1
else:
    while(num >= 2):
        fact = fact * num
        num -=1

print(fact)



''' using function
def fact(num):
    if num == 1:
        return 1

    else:
        return num*fact(num-1)

print(fact(5))
'''
