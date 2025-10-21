# Find the sum of digits of a number.

num = int (input("Enter a number: "))
tempNum = abs(num)
sumOfDigits = 0 

while (tempNum > 0):
    lastDigit = tempNum % 10
    sumOfDigits = sumOfDigits + lastDigit
    tempNum = tempNum // 10

print(f"The sum of digits of {num} is {sumOfDigits}")

