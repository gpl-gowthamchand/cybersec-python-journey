# Check if a number is a palindrome (e.g., 121 → palindrome).

num = int(input("Enter a number: "))

tempNum = num 
rev = 0 

while(tempNum > 0):
    lastDigit = tempNum % 10 
    rev = rev*10 + lastDigit
    tempNum = tempNum // 10

if num == rev:
    print(f"{num} is a palindrome")

else:
    print(f"{num} is not a palindrome")