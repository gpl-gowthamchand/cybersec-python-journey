import json
from urllib.request import urlopen

## grabing data from the public api and parsing that data

with urlopen("https://jsonplaceholder.typicode.com/todos/1") as respone: # opening the urls json into response variable
    source = respone.read()  # read that into source 

print(source) # b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'

data = json.loads(source) # loading the content into data variable as normal string
print(data) # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

indented_data = json.dumps(data, indent=2) # dumping that modified data into indented_data varible as json formated
print(indented_data)
'''
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
'''