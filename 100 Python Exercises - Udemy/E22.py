from pprint import pprint

# solution 1
la = list(range(1, 11))
lb = list(range(11, 21))
lc = list(range(21, 31))
d = dict([('a', la), ('b', lb), ('c', lc)])
pprint(d)

print()

# solution 2
d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(d)

print()

# solution 3
d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))
pprint(d)