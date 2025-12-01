### Modes in filehandling
'''
r - read (file must exists)
w - write (create file, overwrites if exists)
a - append to file
x- creates a newfile(error if exists)
r+ - read and write
w+ - read and write (overwrites files)
a+ - read and append

rb - read binary
wb - write binary
'''

'''
## r - read
read 
pointer position- start of the file
if file exists - reads from the begining
if file dont exist - raises FileNotFoundError

## w - write
write
pointer position - start of the file
if file exists - truncates(erases) all existing content
if dont exists - creates a new file

## a - append
append
pointer position - end of the file
if file exists - writes new content at the end
if file dont exists - creates new file

## x - exclusive creation
exclusive creation
pointer positioin - start of the file
if file exists - raises FileExistsError
if file dont exists - creates new file


## r+ 
read and write
pointer position - start of the file
if file exists - read from the start; allows writing over existing data
if file dont exists - raises FileNotFoundError

## w+ 
write and read
pointer position - start of the file
if file exists - Truncates (erases) all existing content.
if file dont exists - creates new file

## a+
append and read 
pointer pointer - end of the file
if file exists - append to the end; allows reading from the start
if file dont exists - creates new file.

'''

''' binary modes 
## rb 
 Read a file in binary mode (e.g., loading an image).

## wb 
 Write to a file in binary mode (e.g., saving an image).

## r+b or rb+
 Read and write in binary mode.

## r+b or rb+
 Read and write in binary mode.
'''

## example binary
# Open an image file for reading and writing in binary mode
with open("profile.jpg", "rb+") as f:
    # Read the first 100 bytes
    header = f.read(100)
    print(f"Read {len(header)} bytes of the header.")

    # Move the pointer to the end of the file
    f.seek(0, 2) # 0 bytes offset from position 2 (end of file)

    # Write some binary data to the end (e.g., a simple EOF marker)
    f.write(b'\xFF\xD9')