# Check if a number is prime

num = int(input("Enter a num: "))
count = 0 

for i in range(1, num+1):
    if ( num%i == 0 ):
        count = count +1 

if (count == 2):
    print(f"{num} is a prime number")

else:
    print(f"{num} is a non prime number")