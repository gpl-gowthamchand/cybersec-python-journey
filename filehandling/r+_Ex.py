## r+ 
'''
read and write
pointer position - start of the file ie 0
if file exists - read from the start; allows writing over existing data
if file dont exists - raises FileNotFoundError '''

''' demoforRplus.txt (initial state):
1234567890
abcdefghij
'''


# 1 first run: Write, then Seek, then Read
with open("demoforRplus.txt", "r+") as file: 
    # Pointer starts at 0.
    
    file.write("hello")  # Overwrites '12345'. Pointer moves to 5.
    # File content is now: hello67890\nabcdefghij
    
    file.seek(0)         # Moves the pointer back to index 0 (start).
    
    # Read the file from the current pointer (index 0) to the EOF.
    print("Run 1 Output (After write and seek(0)):")
    print(file.read())      

''' demoforRplus.txt (updated after 1st run):
hello67890
abcdefghij
'''
# File content is permanently updated: "hello67890\nabcdefghij"

print("-------------------------------------------------------------------")


# 2 second run: Simple Full Read
with open("demoforRplus.txt", "r+") as file: 
    # File is opened; pointer resets to 0 (start). Content is NOT overwritten.
    
    # Read the entire updated file from index 0.
    print("Run 2 Output (Full read of updated file):")
    print(file.read())

''' output here is :
    hello67890
    abcdefghij
'''
print("----------------------------------------------------------------------")


# 3 third run: Seek to Desired Read Point
with open("demoforRplus.txt", "r+") as file: 
    # File is opened; pointer resets to 0 (start).
    
    file.seek(8)                  # Moves the pointer to index 8.
    # The content is 'hello67890\n...'
    # Index 8 is the '9' character.
    
    # Read the file from the current pointer (index 8) to the EOF.
    print("Run 3 Output (Reading from index 8 onwards):")
    print(file.read())

''' output 
90
abcdefghij
'''