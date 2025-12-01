with open("demo2.txt", "r") as file:  ## Using 'with' statement to open 'demo2.txt' in read mode ('r') and assigning the file object to the variable 'file'
    content = file.read()            ## Calling .read() method on the file object to read all contents and store the resulting string in the 'content' variable

print(content)                       ## Printing the string stored in the 'content' variable to the console


'''
with open("demo2.txt", "r") as file:
    print(file.read())
'''