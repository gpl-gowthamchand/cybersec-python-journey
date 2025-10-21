# Count the number of digits in a number.

# without converting to str

num = int(input("Enter a number: "))

tempNum = abs(num)

count = 0

if tempNum == 0:
    count = 1
else:
    while(tempNum > 0):
        tempNum = tempNum//10
        count = count +1

print(f"the number of digits in {num} is {count}")




## converting to string and use len to count

num = int(input("Enter a number: "))
tempNum = abs(num)    # abs() returns absolute value of numbers eg: -123 = 123
tempNum = str(tempNum) 
numberOfDigits = len(tempNum)

print(f"the number of digits in {num} is {numberOfDigits}")

