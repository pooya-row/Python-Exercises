a = [1, 2, 3]
# solution 1
for i in a:
    print('Item %s has index %s' % (i, i - 1))

# solution 2
for index, item in enumerate(a):
    print("Item %s has index %s" % (item, index))

# enumerate creates an enumerate object which yields pairs of indexes and items.
