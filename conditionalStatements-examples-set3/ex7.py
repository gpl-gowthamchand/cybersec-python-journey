# Write a program to check if a character is a vowel or consonant.

char = input("Enter a single character: ")

if len(char) == 1:
    char = char.lower()
    ascii_val = ord(char)

    #check if its an alphabet(a-z) without isalpha() function
    if (ascii_val >= 97 and ascii_val <= 122):
        if (char in ['a', 'e', 'i', 'o', 'u']):
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
    else:
        print("invalid input, enter a alphbet character")    


else:
    print("Invalid input. Please enter only one character.")




# using isalpha() function
'''
char = input("Enter a single alphabet character: ").lower()

if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")

'''