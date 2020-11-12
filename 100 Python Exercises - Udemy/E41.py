import string

file = open('new_file.txt', 'w')
for letter in string.ascii_lowercase:
    file.write(letter + '\n')
file.close()
