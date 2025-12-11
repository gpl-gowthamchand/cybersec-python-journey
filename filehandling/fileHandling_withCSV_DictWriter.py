import csv 

# 1. SETUP THE DICTREADER (Reading the Source File)
with open("names.csv", "r") as file:
    # We use DictReader to read the file. It automatically reads the first row 
    # of 'names.csv' and uses those values (e.g., "firstname", "lastname", "rollno") 
    # as the keys for every subsequent row (dictionary).
    old_data = csv.DictReader(file)

    # 2. SETUP THE DICTWRITER (Writing the Destination File)
    with open("new_name_csvDictWriter.csv", "w") as new_file:

        # Define the exact headers (fieldnames) that the DictWriter must use. 
        # These keys MUST match the keys produced by the DictReader for the data to transfer correctly.
        headings = ["firstname", "lastname", "rollno"]   
        
        # Create the DictWriter, connecting it to the new file and specifying:
        # - fieldnames: The required order of the columns.
        # - delimiter: The separator to use in the output file (here, a pipe '|').
        new_data = csv.DictWriter(new_file, fieldnames=headings, delimiter="|")

        # Write the header row (the fieldnames themselves) to the very first line of the new file.
        new_data.writeheader()

        # 3. CONVERSION LOOP
        # Iterate over the dictionaries yielded by the DictReader.
        for line in old_data:
            # .writerow() takes the entire dictionary (line) and writes it 
            # to the file, matching the keys to the defined 'fieldnames'.
            # Example: {'firstname': 'Rahul', 'lastname': 'Sharma', 'rollno': '2101'}
            new_data.writerow(line)

