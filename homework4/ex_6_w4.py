def swap(func):
    def wrapper(*args, **named_arg):
        func(*args[::-1], **named_arg)
    return wrapper

@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)