# Check whether a given character is uppercase, lowercase, digit, or special symbol.

char = input("Enter a character : ")

if len(char) == 1 :
    ascii_val = ord(char)

    if ascii_val >= 97 and ascii_val <= 122 :
        print(f"{char} is lowercase")
    elif 97 <= ascii_val <= 122:
        print(f"{char} is a lowercase letter.")
    elif 48 <= ascii_val <= 57:
        print(f"{char} is a digit.")
    else:
        print(f"{char} is a special symbol.")

else:
    print("Enter a valid single character")