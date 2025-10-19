# Write a program to check if a given year is a leap year or not.

year = int(input("Enter the year: "))

if (year % 4 == 0):
    if (year %100 == 0):
        if (year % 400 == 0):
            print(f"{year} is leap year")
        else:
            print(f"{year} is not a leap year")

    else:
        print(f"{year} is leap year")    

else:
        print(f"{year} is not a leap year")   


''' 
A year is a leap year if it is divisible by 4.
However, if it is also divisible by 100, it must be divisible by 400 to be considered a leap year.
''' 