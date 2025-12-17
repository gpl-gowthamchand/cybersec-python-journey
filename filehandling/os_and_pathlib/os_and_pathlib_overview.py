import os
from pathlib import Path

print(Path.cwd()) # prints the current working directory

## loop over the path in the current working directory and print
for p in Path.cwd().iterdir():
    print(p)
'''output example:
example_directory
os_and_pathlib_overview.py
'''

## lets create different path objects for each
my_dir = Path("example_directory")
my_file = Path("os_and_pathlib_overview.py")

print(my_dir) #example_directory
print(my_file) #os_and_pathlib_overview.py
# this just printed the file/directory names

print(my_dir.name) # this also prints the name, but we mentioning explicitly
print(my_file.name)

## get the file extension
print(my_dir.suffix) # prints nothing because it is a directory, it dont have any extension
print(my_file.suffix) # .py --it is the file extension

## get only the file name without extension
print(my_dir.stem) # example_directory
print(my_file.stem) # os_and_pathlib_overview

## lets access a file within the the directory example_directory
# we dont need paths here, because we already have the path object here

new_file = my_dir / "newFile.txt" # we used already existing path object my_dir
# in pathlib we use forward slash operator
print(new_file) #example_directory/newFile.txt

# in os module we use obj.joinpath("new")
# new_file = my_dir.joinpath("newFile.txt")

# we created a path to new file, it is printed but does it really exists?, NO 
print(my_dir.exists()) # True
print(my_file.exists()) # True
print(new_file.exists()) # False

# .parent - to get the parent directory of our directory/file
print(my_file.parent) # .

# .absolute() - to get the abosolute path
print(my_file.absolute()) #/mnt/Data/VsCode/python for cybersecurity/practice/filehandling/os_and_pathlib/os_and_pathlib_overview.py
print(my_file.parent.absolute()) #/mnt/Data/VsCode/python for cybersecurity/practice/filehandling/os_and_pathlib

# .resolve() - also returns the absolute path, convert a relative path into absolute path while resolving symbolic links(sym links) and normalising the path structure.


