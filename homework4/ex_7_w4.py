import time as t

def PATH(arg: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = []                       # сбор данных
            t.localtime()
            time_start = t.ctime(t.time())
            t.clock()
            value = func(*args, **kwargs)
            time = t.clock()
            time_end = t.ctime(t.time())
            arguments = [*args]
            named_arguments = {**kwargs}
            data.append(time)
            data.append(time_start)
            data.append(time_end)
            data.append(arguments)
            data.append(named_arguments)
            if value is None:
                data.append('-')
            else:
                data.append(value)
            print(*data)
            return data
        return wrapper
    data = decorator
    with open(arg, 'w') as file:
        for elem in data:
            file.write(elem)
    return decorator

path = str(input())

# test
@PATH(path)
def random_function(*args, **kwargs):
    print('Мои аргументы', *args)
    print("Мои именованные аргументы", **kwargs)
    return

random_function(1, 1, 4, 5, sliv=True, doka2='kill mind of little pupil')