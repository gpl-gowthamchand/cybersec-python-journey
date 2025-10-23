# Reverse a given string using a loop (without using slicing).

string = input("Enter a string: ")
length = len(string)

##while
while (length > 0):
    print(string[length-1], end="")
    length = length-1
print("\n")


## for 

for i in range(length-1, -1, -1):
    print(string[i], end="")
print("\n")