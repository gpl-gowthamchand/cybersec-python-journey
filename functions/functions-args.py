### 4 types args 


## Positional arguments - These arguments are passed to a function based on their order or position

def addition(a, b):
    print(a+b)

addition(3, 4)


## Keyword arguments - These arguments are passed to a function using the parameter's name, making the order of arguments irrelevant. This improves readability and flexibility, especially with functions having many parameters. 

def substraction(x, y):
    print(x-y)

substraction(x=10, y=6)


## Default arguments - These are parameters in a function definition that have a predefined value. If a value is not provided for a default argument during the function call, its default value is used.

def sayHi(name="Gowtham"):
    print(f"hello {name}")

sayHi()              # hello Gowtham
sayHi("Pradeep")     # hello Pradeep



## Arbitrary Positional Arguments (*args) - Allows a function to accept an arbitrary number of positional arguments. These arguments are collected into a tuple within the function.

def sumOfallNumbers(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    print(f"sum of all numbers {numbers} : {total}")

sumOfallNumbers(1, 2, 3, 4, 5)


## Arbitrary Keyword Arguments (`: kwargs`):** - Allows a function to accept an arbitrary number of keyword arguments. These arguments are collected into a dictionary within the function, where keys are the argument names and values are their corresponding values.

def displayInfo(**details):
    for k, v in details.items():
        print(f"{k} -> {v}")

displayInfo(name="Gowtham", id=552, dept="CNIS")
''' output:
name -> Gowtham
id -> 552
dept -> CNIS'''