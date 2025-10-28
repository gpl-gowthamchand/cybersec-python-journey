## string formatting 

name = "Rogers"
age = 105

# f strings 
print(f"I am {name}, {age} years old")

# format() method 
print("I am {}, {} years old".format(name,age))

print("I am {1}, {0} years old".format(name, age)) # indexing

# modulo formatting
print("I am %s, %d years old" %(name, age))
