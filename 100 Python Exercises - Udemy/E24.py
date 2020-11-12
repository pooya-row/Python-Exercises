d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))

# solution 1
print('b has value ' + str(d['b']))
print('c has value ' + str(d['c']))
print('a has value ' + str(d['a']))

print()     # blank line

# solution 2
ff = ['b', 'c', 'a']
for k in ff:
    print(k + ' has values ' + str(d[k]))

print()     # blank line

# solution 3
for k, v in d.items():
    print(k, 'has values', str(v))  # no +, instead use comma
