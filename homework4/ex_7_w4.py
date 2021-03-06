import time as t

def data_of_func(arg: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = []                       # сбор данных
            t.localtime()
            time_start = t.time()
            value = func(*args, **kwargs)
            time_end = t.time()
            time = time_start - time_end
            arguments = [*args]
            named_arguments = {**kwargs}
            data.append(str(time))
            data.append(str(t.ctime(time_start)))
            data.append(str(t.ctime(time_end)))
            data.append(str(arguments))
            data.append(str(named_arguments))
            if value is None:
                data.append('-')
            else:
                data.append(value)
            print(*data)
            with open(arg, 'w') as file:
                data = map(lambda x: x + '\n', data)
                file.writelines(data)
            return value
        return wrapper
    return decorator


path = str(input())

# test
@data_of_func(path)
def random_function(*args, **kwargs):
    print('Мои аргументы', *args)
    print('Мои ключи именованных аргументы', *kwargs.keys())
    return


random_function(1, 1, 4, 5, arg=True, doka2='kill mind of little schoolars')
