import csv 

# 1. SET UP THE READER (Our Data Source)
# We open the original file, 'names.csv', in read mode ('r').
with open("names.csv", "r") as file:
    # This creates our CSV 'translator' (the reader). Its job is to read the file
    # and turn every line of comma-separated text into a clean Python list for us.
    original_data = csv.reader(file) 

    # 2. SET UP THE WRITER (Our Destination)
    # We open the new file, 'new_names.csv', in write mode ('w') to start fresh.
    with open("new_names.csv", "w") as new_file:
        # This creates our CSV 'formatter' (the writer). We connect it to the new file
        # and specify that we want to use the pipe symbol '|' as the column separator (delimiter).
        new_data = csv.writer(new_file, delimiter="|") 

        # 3. CONVERT THE DATA ROW BY ROW
        # We loop through every single row that our 'translator' (original_data) yields.
        for line in original_data:
            # We take the list of data (the current 'line') and ask the 'formatter' (writer) 
            # to save it. It automatically joins the list elements using the '|' delimiter.
            new_data.writerow(line) 
