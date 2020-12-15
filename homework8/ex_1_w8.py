def print_map(func, iterable):
    i = True
    while i:
        try:
            print(func(next(iterable)))
        except StopIteration:
            i = False


def function(x):
    return x ** 2


a = iter([1, 2, 3, 4, 5])
print_map(function, a)
