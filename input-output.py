#input


name = input("Enter your name: ") # we can also include a string inside the input() function, the string inside it passed as a prompt.

num = input()  # it takes str as default input type

num = int(input("Enter a int num: ")) # now it takes integer inputs
num = float(input())                  # it takes float inputs


# multiple inputs
a, b = input("Enter two numbers seperated by space: ").split()
print(type(a))  # str type
print(a, b)

# for int multiple inputs
a, b = map(int, input("Enter two numbers with space: ").split() )
print(type(a))
print(a, b)




# output

print("Hello world") # we print() function to display output

print("hello " + name)

x= 10
y= 11
print("the numbers are", x, "and", y)

#using sep and end
print("x", "y", "'z", sep="--", end=".")

# formatted output f-strings
name = "Gowtham"
age = 22
print(f"My name is {name} and i am {age} years old")

# format() method
n = 4
m = 5
print("the sum of {} and {} is {}".format(n,m, n+m))


t= (1,2,3,4)
print(*t) # prints this tuple as 1 2 3 4 not as (1, 2, 3, 4)
'''The * (asterisk) operator before t
The * is called the unpacking operator (or splat operator).
It tells Python to unpack the elements of the tuple (or list, or any iterable) into separate arguments.'''