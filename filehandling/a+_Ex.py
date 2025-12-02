## a+
'''
append and read 
pointer pointer - end of the file(EOF)
if file exists - append to the end; allows reading from the start
if file dont exists - creates new file.
'''

# --- INITIAL SETUP ---
# Creating the file with its initial content using 'w' mode.
with open("a_plus_demo.txt", "w") as f:
    f.write("Existing content is here.")

'''
a_plus_demo.txt (iniitial)

Existing content is here.

'''

# 1 first run: Append, but Try to Read First
with open("a_plus_demo.txt", "a+") as file:
    # 1. Pointer is automatically placed at the EOF (End Of File).
    
    # 2. Reading now: Attempts to read from EOF to EOF.
    print("Run 1 Output (Attempted read from EOF):")
    print(f"Read result: '{file.read()}'")
    # Output is an empty string because the pointer was at the end.
    
    # 3. Write operation: Always writes at the end, regardless of where the pointer is.
    file.write(" ---NEW APPENDED DATA---")
    # Pointer is still at the new EOF.


print("-------------------------------------------------------------------")

'''
a_plus_demo.txt (after #1):

Existing content is here. ---NEW APPENDED DATA---

'''

# 2 second run: Append, then Seek to Read
with open("a_plus_demo.txt", "a+") as file: 
    # File is opened; pointer is automatically placed at the new EOF.
    
    # 1. Write operation: Append more content.
    file.write(" ---SECOND APPEND---")
    # Content is added to the very end. The pointer advances to the new EOF.
    
    # 2. Seek to 0: We must manually move the pointer back to the start (index 0).
    file.seek(0)
    
    # 3. Read operation: Read the entire file from the beginning.
    print("Run 2 Output (Read entire file after two appends):")
    print(file.read())


''' Final#2 a_plus_demo.txt Content:
Existing content is here. ---NEW APPENDED DATA--- ---SECOND APPEND---
'''