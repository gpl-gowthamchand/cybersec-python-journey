# Find the reverse of a number using a while loop.

## arithmetic method

num = int(input("Enter a number: "))
rev = 0

while( num > 0) :
    lastDigit = num % 10 
    rev = rev * 10 + lastDigit
    num = num // 10

print(rev)



## method 2 convert int to str print using indexing through while loop

num = int(input("Enter a number: "))
num = str(num)
length = len(num)
while(length > 0 ):
    print(num[length-1], end=("")) # index starts from 0, if lenght=4, then 0 1 2 3
    length = length-1 


## method 3 string slice
''' convert int to str, use string slicing to reverse it '''

num = int(input("Enter a number: "))
num = str(num)
print(num[::-1])

