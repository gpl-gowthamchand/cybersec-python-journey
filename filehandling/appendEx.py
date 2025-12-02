# a - append mode - append the content at the end of the file if already exists, if no creates one

'''
appendDemo.txt (Initial State):

this line is already present..

'''

with open("appendDemo.txt", "a") as file: ## Opening the file in Append mode ('a'); the file pointer is placed at the very end of the existing content
    file.write("\nthis is new line adding through append") # The '\n' ensures the new data starts on a new line, then the string is written after it

'''
appendDemo.txt (Final State after the run):

this line is already present..
this is new line adding through append

'''