import argparse

def fib(n):
    try:
        n = int(n)
        if n == 2 or n == 1:
            return n - 1
        elif n <= 0:
            raise ValueError
        else:
            return fib(n - 1) + fib(n - 2)
    except ValueError:
        print('Введите натуральное число')


parser = argparse.ArgumentParser()
parser.add_argument('-n', action='store', default=None, help='Введите натуральное число')
parser.add_argument('number', action='store', nargs="?", help='Введите натуральное число')
namespace = parser.parse_args()

try:
    if not namespace.n is None and not namespace.number is None:
        raise ValueError
    elif namespace.n is None and not namespace.number is None:
        N = namespace.number
    elif not namespace.n is None and namespace.number is None:
        N = namespace.n
    elif namespace.n is None and namespace.number is None:
        raise ValueError
except ValueError:
    print('После названия программы напишите натуральное число')

print(fib(N))