'''
Password Strength Checker
Write a function check_password(pwd) that returns:

“Strong” if length ≥ 8, has uppercase, lowercase, digit, and special char

“Weak” otherwise

(Hint: use any() and string methods like isupper(), isdigit(), etc.)
'''

def check_password(pwd):
    if len(pwd) >= 8:
        upper = any(chr.isupper() for chr in pwd)
        lower = any(chr.islower() for chr in pwd)
        digit = any(chr.isdigit() for chr in pwd)
        special = any(not chr.isalnum() for chr in pwd)
        if upper and lower and digit and special:
            return "Strong"
        else:
            return "Weak"
    else:
        return "Weak"

pwd = input("Enter password: ")
print(check_password(pwd))