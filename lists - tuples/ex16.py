'''Sort a list of file names by extension: 
files = ["report.pdf", "data.txt", "notes.docx", "image.png"]
'''

files = ["report.pdf", "data.txt", "notes.docx", "image.png"]

names = []
extensions = []

for file in files :
    name, ext = file.split(".")
    names.append(name)
    extensions.append(ext)

extensions.sort()
print(extensions)

reordered_list = []

for i in extensions:
    for j in files :
        if i in j:
            reordered_list.append(j)



print(reordered_list)


'''
files = ["report.pdf", "data.txt", "notes.docx", "image.png"]

# Sort the list by the file extension (the part after '.')
files.sort(key=lambda file: file.split(".")[1])

print(f"Files sorted by extension: {files}")

How it works:

lambda file: file.split(".")[1] → extracts the extension part.

sort(key=...) → sorts based on that extension.
'''