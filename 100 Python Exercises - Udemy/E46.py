# solution 1
import string

ls = []
for l in string.ascii_lowercase:
    file = open('C:/Users/Pooya/Documents/Python/Python Exercises/E45/' + l + '.txt', 'r')
    # cont = file.read()
    ls.append(file.read().strip('\n'))  # strip removes the outermost leading and trailing chars argument values
    file.close()
print(ls)

# solution 2
import glob

ls = []
file_list = glob.glob('E45/*.txt')  # get a list of files in the directory with a particular pattern
for file_name in file_list:
    file = open(file_name, 'r')
    ls.append(file.read().strip('\n'))
    file.close()
print(ls)
