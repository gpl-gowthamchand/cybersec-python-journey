'''
Search for a number in a list:

If found → print "Number found!" and break

Else (after loop) → print "Number not found"
''' 

listOfNums = [1, 4, 2, 8, 7, 5, 9, 6]

key = int(input("Enter a key number to search: "))

n = len(listOfNums)

for i in range(n):
    if key == listOfNums[i]:
        print(f"Number found at index {i}")
        break
else:
    print("Number not found")