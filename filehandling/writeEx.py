## write() - The .write(string) method is used to write a single string to the file.

# 1 first run
with open("writeDemo.txt", "w") as file:  # opening in w mode, clear all if already exists
    print(file.write("this is first line")) # saves the written data into file and returns the no of character

    file.write("this is line two") # adds this 2nd line data in the same line 



# 2 second run
# opening again in w mode clears the first run entries

with open("writeDemo.txt", "w") as file:
    file.write("this is 2nd run first line")