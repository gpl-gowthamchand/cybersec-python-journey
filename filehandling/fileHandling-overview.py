### File handling 
'''File handling means to read from and write to a file using python.

two types of files 
1 text file (.txt, .log)
2 binary files(.mp4, .mp3, .png, .. etc)

process:
1. open file
2. perform operation
3. close file.

syntax:
1 ) 
var_name = open("file.txt","mode")
#operations
var_name.close

2) with method - self closing 
with open("file", "mode") as var_name:
    #operations 
'''
# example 
test = open("demo1.txt", "w") # w - write mode, create and write into it, if already exists- clears and writes new content
test.write("Gotham needs me!!")
test.close()

# same example with other syntax
'''
with open("demo1.txt", "w") as test:
    test.write("iam batman!")
'''