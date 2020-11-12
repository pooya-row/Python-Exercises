# solution1
def trans(word1, dic):
    if word1.upper() in [x.upper() for x in dic.keys()]:
        return dic[word1.lower()]
    else:
        return "We couldn't find that word!"


# solution 2
def vocab(word2, dic):
    try:
        return dic[word2.lower()]
    except KeyError:
        return "We couldn't find that word!"


d = dict(weather="clima", earth="terra", rain="chuva")
word = input('Enter word: ')
# word = input('Enter word: ').lower()  # alternative
print(trans(word, d))
