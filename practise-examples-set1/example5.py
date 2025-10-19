# input: "John",25
# output: "Name:John,Age:25"

name, age = input("Enter your name and age seperated by comma: ").split(",")
print(f"Name:{name},Age:{age}")