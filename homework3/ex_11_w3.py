def c():
    raise ValueError('my exeption')
    pass


def b():
    c()
    pass


def a():
    b()
    return 5


a = a()
print(a)
