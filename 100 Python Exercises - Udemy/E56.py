import json

d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}
file = open('E56.json', 'w')
json.dump(d, file, indent=4, sort_keys=True)
file.close()
# pprint(d)
