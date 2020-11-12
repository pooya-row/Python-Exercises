# solution 1
d = {"a": 1, "b": 2, "c": 3}
yy = 0
for k in d:
    yy += d[k]
print(yy)

# solution 2
print(sum(d.values()))