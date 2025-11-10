## Nested Functions - You can define a function inside another.

def outer():
    def inner():
        print("Inner function executed")
    inner()
outer()