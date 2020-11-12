def word_count(ff):
    file = open(ff, 'r')  # 'r' for reading
    cont = file.read()
    file.close()
    return len(cont.split(' '))


print(word_count('C:/Users/Pooya/Downloads/words1.txt'))
print(word_count('words1.txt'))
