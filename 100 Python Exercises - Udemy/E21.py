# Dictionary comprehension

d = {"a": 1, "b": 2, "c": 3}
print(dict((k, v) for k, v in d.items() if v <= 1))