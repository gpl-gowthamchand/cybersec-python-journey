# input:  "John"
# output: "Hello,John"

name = input("Enter your name: ")
print(f"Hello,{name}!")


print("Hello,"+name +"!")
print("Hello,{}!".format(name))
print("Hello", name, sep=",", end="!")