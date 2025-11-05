# Find the second largest number in a list.

listOfNumbers = [1,3,4,2,8,6,5]
large = listOfNumbers[0]

for i in listOfNumbers:
    if i > large:
        large= i 
        
listOfNumbers.remove(large)

secondLarge = listOfNumbers[0]
for i in listOfNumbers:
    if i > secondLarge:
        secondLarge= i 

print(f"The second largest number is: {secondLarge}")