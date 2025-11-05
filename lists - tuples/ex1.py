'''Create a list of 5 fruits and:

Print the second and last fruit.

Replace one fruit name with another.

Add a new fruit and remove one fruit.
'''

fruits = ["apple", "banana", "cherry", "mango", "watermelon"]

# Print the second and last fruit
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# Replace one fruit name with another
fruits[0] = "grapes"
print("After replacing:", fruits)

# Add a new fruit and remove one fruit
fruits.append("papaya")
fruits.remove("watermelon")
print("After adding and removing:", fruits)
