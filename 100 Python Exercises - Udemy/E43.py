import string

# solution 1
file = open('E43.txt', 'w')
letters = string.ascii_lowercase
l = 0
while l < len(letters):
    file.write(letters[l] + letters[l + 1] + '\n')
    l = l + 2
file.close()

# solution 2
file = open('E43.txt', 'w')
lt1 = string.ascii_lowercase[::2]
lt2 = string.ascii_lowercase[1::2]
for a, b in zip(lt1, lt2):
    file.write(a + b + '\n')
file.close()
