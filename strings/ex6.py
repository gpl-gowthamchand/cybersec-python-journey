## String functions 

# string length - len()
name = "gowtham"
print(len(name))
print()


# str() - explicitly convert to string type 
pi = 3.14 
print(type(pi))
pi = str(pi)
print(type(pi))
print()

# repr() - returns an original string representation of an object 
text = "Hello\tWorld"
print(text)
print(repr(text))
print()

# format(val, format_spec) 
print(format(12345, ',d'))
print(format(3.141599, '.2f'))
print()

# ascii() - it escapes any non printable char using \x, \u, \U 
print(ascii("PythÖn"))
print()

# eval(expression) - parses a string exprr and runs it a python code and returns the result 
print(eval("2 + 5 * 2"))
print()

# ord() - returns ascii val for chars 
print(ord("A"))
print()

# chr() - returns character for given ascii value 
print(chr(65))