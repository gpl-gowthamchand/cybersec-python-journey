import json # importing json lib is important to work with json data


# json.dumps() serializes a Python object (like a dictionary or list) into a JSON-formatted string.
# json.loads() deserializes a JSON-formatted string back into a Python object.

## below this json text example
# people_string is dict contains 'people' key and list value
# the value list contains dictionaries within itself in this example
people_string = '''
{
  "people": [
    {
      "name": "Smith",
      "phone": "615-555-7164",
      "emails": "smith@gmail.com",
      "has_license": false
    },
    {
      "name": "Chris",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}   
'''

# loading the json content into our variable
data = json.loads(people_string)

print(type(data)) # <class 'dict'>
print(data)
'''{'people': [{'name': 'Smith', 'phone': '615-555-7164', 'emails': 'smith@gmail.com', 'has_license': False}, {'name': 'Chris', 'phone': '560-555-5153', 'emails': None, 'has_license': True}]}'''

print("-----------------------------------------------------------")

print(type(data["people"]))  # <class 'list'>

## loop through each person details in people
for person in data["people"]:
    print(person)
'''
{'name': 'Smith', 'phone': '615-555-7164', 'emails': 'smith@gmail.com', 'has_license': False}
{'name': 'Chris', 'phone': '560-555-5153', 'emails': None, 'has_license': True}
'''

## inside each person details like name, phone...
for person in data["people"]:
    print(person["name"])
'''
Smith
Chris'''


## delete the phone elements and dump the new data into a new variable
for person in data['people']:
    del person["phone"]

new_data = json.dumps(data, indent=2) # json.dumps() to add that data into the new variable, indent is optional parameter, sort_keys=True to alphabetically sort the keys in the output.
print(new_data)

''' output with indent=2
{
  "people": [
    {
      "name": "Smith",
      "emails": "smith@gmail.com",
      "has_license": false
    },
    {
      "name": "Chris",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

# if no indent is given the ouput will be in single line
#{"people": [{"name": "Smith", "emails": "smith@gmail.com", "has_license": false}, {"name": "Chris", "emails": null, "has_license": true}]}

