# solution 1
def word_count(ff):
    file = open(ff, 'r')  # 'r' for reading
    cont = file.read()
    file.close()
    cont = cont.replace(',', ' ')
    return len(cont.split(' '))


print(word_count('words2.txt'))

# solution 2
import re


def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(",| |:", text)  # | separates the delimiters in this case ',' and ' ' and ':'
    return len(string_list)


print(count_words_re("words2.txt"))
