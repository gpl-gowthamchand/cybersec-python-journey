### Functions 
''' A function is a block of reusable code that performs a specific task, 
you define it once and call it anytime you need.

syntax : 
        def function_name(parameters):
            # code block
            return statement

always call the function after definition only

'''
## simple function
def greet():
    print(f"Hello there!")

greet()



## function with paramenters and return

def customGreet(name):
    return f"Hello {name}"

greetGowtham = customGreet("Gowtham")
print(greetGowtham)
