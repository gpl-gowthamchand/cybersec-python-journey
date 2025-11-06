'''
Check Existence

Write a program that checks if "email" key exists in the dictionary.
If not, add "email": "gowtham@gmail.com".
'''

student = {
    "name": "Gowtham",
    "age": 22,
    "course": "Python"
}

student.setdefault("email", "gowtham@gmail.com")
print(student)

'''
setdefault(key, value) :-

checks if the key exists in the dictionary.

If it exists, it does nothing.

If it doesn’t exist, it adds that key with the given value.
'''


''' manually adding using decision making statement 

if "email" not in student:
    student["email"] = "gowtham@gmail.com"

'''