import os
import string

# create a folder
if not os.path.exists('E45'):
    os.makedirs('E45')
# create files
for l in string.ascii_lowercase:
    # file_name = 'C:/Users/Pooya/Documents/Python/Python Exercises/E45/' + l + '.txt'
    file = open('C:/Users/Pooya/Documents/Python/Python Exercises/E45/' + l + '.txt', 'w')
    file.write(l + '\n')
    file.close()
