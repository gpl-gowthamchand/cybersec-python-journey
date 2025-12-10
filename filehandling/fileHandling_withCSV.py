import csv 

with open("names.csv", "r") as file:
    data = csv.reader(file)

    print(data) # <_csv.reader object at 0x7fdc31e46810> -- it doesnt display the data, it displays as object

    #next(data) ## this line skips the field/top line or headings

    ## loop through it to get data
    for line in data:
        print(line)