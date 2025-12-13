import csv 

# opening the file without specifying the delimiter, so default it takes comma
with open("new_names_withDifferentDelimiter.csv", "r") as file:
    data = csv.reader(file)

    for line in data:
        print(line)

''' output
['Name|Email']
['Gowtham|gowtham51@gmail.com']
['Pradeep|pradeep@yahoo.com']
'''

# Now we are specifying the correct delimiter we used in the file.
with open("new_names_withDifferentDelimiter.csv", "r") as file:
    data = csv.reader(file, delimiter="|")
    for line in data:
        print(line)

''' output
['Name', 'Email']
['Gowtham', 'gowtham51@gmail.com']
['Pradeep', 'pradeep@yahoo.com']
'''