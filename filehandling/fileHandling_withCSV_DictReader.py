import csv

# 1. Setting up the reader (Using DictReader)
# We open the file in read mode ('r').
with open("names.csv", "r") as file:
    # We create a DictReader object. This is specialized: it automatically reads the 
    # very first line of the CSV file and treats those values (e.g., 'firstname', 'lastname') 
    # as the dictionary keys (fieldnames).
    data = csv.DictReader(file)

    # 2. Process the data (Row by Row)
    # When we iterate over 'data', it yields a Python dictionary for every single row.
    for line in data:
        # Instead of a list (like ['Rahul', 'Sharma', '2101']), we get a dictionary, 
        # which makes accessing data much clearer (e.g., line['firstname']).
        print(line)

''' Output demonstrates the result of DictReader:
{'firstname': 'Rahul', 'lastname': 'Sharma', 'rollno': '2101'}
{'firstname': 'Priya', 'lastname': 'Singh', 'rollno': '2102'}
{'firstname': 'Amit', 'lastname': 'Verma', 'rollno': '2103'}
{'firstname': 'Siraj', 'lastname': 'Mohammad', 'rollno': '2104'}
{'firstname': 'Vikram', 'lastname': 'Yadav', 'rollno': '2105'}
{'firstname': 'Anjali', 'lastname': 'Gupta', 'rollno': '2106'}
...
'''
# Key Benefit: We can now access data using header names (e.g., line['lastname'])
# instead of numerical indices (line[1]).