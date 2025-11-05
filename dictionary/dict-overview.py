## Dictionaries 
''' collection of key-value pairs, each key is unique and maps to a specific value

dict_name = { key1 : value, key2 : value2, key3 : value3}

''' 

student = {
    "name" : "Gowtham",
    "age" : 22,
    "course": "Python",
    "country" : "India"
}
print(student)           # {'name': 'Gowtham', 'age': 22, 'course': 'Python', 'country': 'India'}

## accessing dict values 
print(student["age"])         # 22
print(student.get("course"))  # Python

''' get() is safer method, it won't throw an error if key is missing, it returns the default value'''

print(student.get("email", "Not found"))   # Not found

# Modifying and updating dictionary values 
student["age"] = 23                   #modifying existing value
student["emaill"] = "xyz@gmail.com"   # adding new values

print(student)    #{'name': 'Gowtham', 'age': 23, 'course': 'Python', 'country': 'India', 'emaill': 'xyz@gmail.com'}

## dictionary comprehension
squares = { x : x*x for x in range(5) }
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

## nested dictionary 
users = {
    "user1": {"name": "Alice", "role": "admin"},
    "user2": {"name": "Bob", "role": "guest"}
}
print(users["user1"]["role"])   # admin

## looping through dictionary
for key in student:
    print(key, ":", student[key])

## You can also loop directly through items():
for k, v in student.items():
    print(f"{k} -> {v}")

## Loop Through Keys
for key in student:
    print(key)

## Loop Through Values 
for value in student.values():
    print(value)


## Loop Through Dictionary With Conditions

ports = {22: "SSH", 80: "HTTP", 443: "HTTPS", 25: "SMTP"}
for port, service in ports.items():
    if port == 80 or port == 443:
        print(f"Secure or web-related port found: {port} ({service})")

## Using enumerate() (with index) - If you want the index while looping through keys or values:
for i, (key, val) in enumerate(student.items(), start=1):
    print(f"{i}. {key}: {val}")


