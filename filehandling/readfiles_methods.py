## read files methods - 3 types

# read() - Reads the entire file as a string.
# readline() - Reads one line at a time.(by default reads the first line)
# readlines() - Reads all lines into a list.

## read()
with open("demo2.txt") as file:
    print(file.read())

print("-------------------------------") 

## readline()
with open("demo2.txt") as file:
    print(file.readline()) #prints the first line

print("-------------------------------") 


## accesing no of lines using loops - readline()
with open("demo2.txt") as file:
    for line in range(2): # 2 lines
        print(file.readline().strip()) # .strip() to remove white spaces

print("-------------------------------") 

## using loops all lines
with open("demo2.txt") as file:
    for line in file:    #We did not explicitly call .read(), .readline(), or .readlines(), because the file object itself is an iterator
        print(line.strip())


## readlines()
with open("demo2.txt") as file:
    print(file.readlines())  # this prints all lines in a list


