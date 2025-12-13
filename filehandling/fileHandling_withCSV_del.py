import csv

with open("names.csv", "r") as file:
    old_data = csv.DictReader(file)

    with open("new_names_after_deletion.csv", "w") as new_file:
        headings = ["firstname", "lastname"]
        new_data = csv.DictWriter(new_file, fieldnames=headings, delimiter="-")

        new_data.writeheader()

        for line in old_data:
            del line["rollno"]
            new_data.writerow(line)

####
''' 
original file:
-------------------------
firstname,lastname,rollno
Rahul,Sharma,2101
Priya,Singh,2102
Amit,Verma,2103
Siraj,Mohammad,2104
Vikram,Yadav,2105
Anjali,Gupta,2106


new file: with no rollno
--------------------------
firstname-lastname
Rahul-Sharma
Priya-Singh
Amit-Verma
Siraj-Mohammad
Vikram-Yadav
Anjali-Gupta

'''