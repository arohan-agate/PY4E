# Using JSON as a Dictionary

import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)  # creates a dictionary, info, from the text, data.
print('Name:', info["name"])  # finds the value associated with the key, "name", in the dictionary.
print('Hide:', info["email"]["hide"])  # finds the value associated with the keys "email", then "hide" in the dictionary


# Using JSON as a List

input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Chuck"
    }
]'''  # input is a list of two dictionaries

info = json.loads(input)  # info is a list
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])