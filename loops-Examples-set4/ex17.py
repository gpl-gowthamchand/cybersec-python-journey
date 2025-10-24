''' 
Check if a number is an Armstrong number.
(e.g., 153 = 1³ + 5³ + 3³) '''

number = int(input("Enter a number: "))
temp = number
length = len(str(number))
arm = 0 

for i in range (length):
    lastDigit = temp % 10 
    arm = arm + (lastDigit**length)
    temp = temp // 10 

if (number == arm):
    print(f"{number} is a armstrong number")
else:
    print(f"{number} is not a armstrong number")
