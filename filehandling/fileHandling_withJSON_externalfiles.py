import json 

# getting already existing countries.json file

with open("countries.json", "r") as file:
    data = json.load(file)      # countries.json is opened as file and the file contents is loaded into data variable not as json formated

print(data)
# [{'name': 'Albania', 'abbreviation': 'AL', 'code': '+355'}, {'name': 'Japan', 'abbreviation': 'JP', 'code': '+81'}, {'name': 'Russia', 'abbreviation': 'RU', 'code': '+7'}, {'name': 'India', 'abbreviation': 'IN', 'code': '+91'}, {'name': 'Germany', 'abbreviation': 'DE', 'code': '+49'}]

for country in data["countries"]:
    del country["abbreviation"]

with open("new_countries.json", "w") as file:  # this creates new file named new_countries.json and open it as file
    json.dump(data, file, indent=2)
    # here 3 parameters data(existing/modified non json data), file(new file, in this we will dump the data as json formated), indent=2(this is optional but useful if we want to make look good
    
