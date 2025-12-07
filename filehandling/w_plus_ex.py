# --- INITIAL SETUP ---
# Create a file with existing content so we can see the truncation in action.
with open("w_plus_demoText.txt", "w") as f:
    f.write("---THIS LINE WAS HERE BEFORE w+ WAS OPENED---")
    

'''
## w+ 
write and read
pointer position - start of the file ie 0
if file exists - Truncates (erases) all existing content IMMEDIATELY upon opening.
if file dont exists - creates new file
'''

# 1. Open the file in 'w+' mode
with open("w_plus_demoText.txt", "w+") as file: 
    # CRITICAL: The line "---THIS LINE WAS HERE..." is instantly ERASED upon this open call.
    # The file is now empty, and the pointer is at index 0.
    
    # 2. Write Operation
    file.write("this is first line") 
    # The string is written to the now-empty file. Pointer moves to the end (index 18).
    
    # 3. Seek Operation
    file.seek(0)
    # The pointer is moved back to the start (index 0), as 'read()' always starts from the pointer.
    
    # 4. Read Operation
    content = file.read()
    print(content)
    # The content read is only the string written in step 2.


'''
w_plus_demoText.txt (Final state after the run):

this is first line
'''