# Check if a string is a palindrome 

s = input("Enter a string: ")
rev_string = s[::-1]

if rev_string == s :
    print("it is palindrome")
else:
    print("it is not a palindrome")
    