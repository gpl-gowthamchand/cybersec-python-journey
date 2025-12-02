## write() - The .write(string) method is used to write a single string to the file.

# 1 first run
with open("writeDemo.txt", "w") as file:  # opening in w mode, clear all if already exists
    print(file.write("this is first line")) # saves the written data into file and returns the no of character

    file.write("this is line two") # adds this 2nd line data in the same line 



# 2 second run
# opening again in w mode clears the first run entries

with open("writeDemo.txt", "w") as file:
    file.write("this is 2nd run first line")


# 3 third run using .writelines()
# opening again in w mode clears the second run entries and prepares to write new data

# Define the list of strings to be written
new_data = [
    "Line 1 from writelines.\n",  ## The newline character is REQUIRED to create a line break
    "Line 2 from writelines.\n",  ## Second element is written right after the first
    "Line 3 without a newline"    ## This will be followed immediately by any subsequent writes
]

with open("writeDemo.txt", "w") as file: ## Opening in 'w' mode deletes the content from Run 2
    # The .writelines() method takes a list or other iterable of strings and writes them consecutively
    file.writelines(new_data)             ## Writing the entire list of strings to the file

    # Appending a final string using .write()
    file.write("---END OF FILE---")       ## This will continue directly after "Line 3 without a newline"

# FINAL STATE of "writeDemo.txt" after run 3:
# Line 1 from writelines.
# Line 2 from writelines.
# Line 3 without a newline---END OF FILE---