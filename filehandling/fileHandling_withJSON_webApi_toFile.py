import json 
from urllib.request import urlopen

## Fetch & Read: urlopen() and source.read() grab the data as a byte string.
with urlopen("https://jsonplaceholder.typicode.com/todos/1") as source:
    response_data = source.read()


## Deserialize: json.loads(response_data) converts the bytes into a usable Python dictionary (raw_data).
raw_data = json.loads(response_data)


## Serialize & Format: json.dumps(raw_data, indent=2) converts the dictionary into a beautiful, multi-line, indented JSON string (data).
data = json.dumps(raw_data, indent=2)


## Save: file.write(data) saves that exact formatted string into the local file.
with open("dataFromUrl.txt", "w") as file:
    file.write(data)