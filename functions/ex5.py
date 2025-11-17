'''
Even or Odd Checker
Write a function check_even(num) that returns “Even” if the number is even, else “Odd”.'''

def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even(7)
print(result)
