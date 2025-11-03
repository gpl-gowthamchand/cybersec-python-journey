''' Unpack a tuple:
student = ("Gowtham", 22, "CSE", "India")
Extract and print name, age, dept, country
'''

student = ("Gowtham", 22, "CSE", "India")
name, age, dept, country = student

print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"dept.   : {dept}")
print(f"Country : {country}")