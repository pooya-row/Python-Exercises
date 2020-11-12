def foo():
    global c
    c = 1
    return c


foo()
print(c)
