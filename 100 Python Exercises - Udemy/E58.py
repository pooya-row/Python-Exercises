import json

# init_file = open('E56.json')
d = json.load(open('E56.json'))
# init_file.close()
d['employees'].append(dict(firstName="Albert", lastName='Bert'))
destination_file = open('E58.json', 'w')
destination_file.seek(0)  # put the cursor at the top of the file
json.dump(d, destination_file, indent=4)
destination_file.close()
