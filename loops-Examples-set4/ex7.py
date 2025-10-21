# Find the reverse of a number using a while loop.

## arithmetic method

num = int(input("Enter a number: "))
rev = 0

while( num > 0) :
    lastDigit = num % 10          # getting the last digit
    rev = rev * 10 + lastDigit    # add digit to the reversed number
    num = num // 10               # remove the last digit

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

