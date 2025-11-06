'''
Create and Access

Create a dictionary for a student:

student = {"name": "Gowtham", "age": 22, "course": "Python"}

Print only the name.
Add a new key "grade" with value "A".
Update "age" to 23.'''

student = {
    "name": "Gowtham",
    "age": 22,
    "course": "Python"
}

print(student.get("name"))      # Prints only the name

student["grade"] = "A"          # Adds a new key-value pair
student["age"] = 23             # Updates the age

print(student)                  # Prints the updated dictionary
