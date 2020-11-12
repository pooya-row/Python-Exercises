# solution 1
def trans(word1, dic):
    if word1 in dic.keys():
        return dic[word1]
    else:
        return "We couldn't find that word!"


# solution 2
def vocab(word2, dic):
    try:
        return dic[word2]
    except KeyError:
        return "We couldn't find that word!"


d = dict(weather="clima", earth="terra", rain="chuva")
word = input('Enter word: ')
print(vocab(word, d))
