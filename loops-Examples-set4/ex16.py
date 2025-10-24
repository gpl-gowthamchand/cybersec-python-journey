# Find the sum of even digits in an integer. 

num = int(input("Enter a number: "))

tempNum = str(num)
sum = 0 
length = len(tempNum)

for i in range(length):
    currentDigit = tempNum[i] 
    currentDigit = int(currentDigit)
    if (currentDigit%2 == 0):
        sum = sum + currentDigit
    
print(sum)
