import argparse

primes = [None, 1, 2]

def prime_gen(n, primes):
    if len(primes) - 1 < n:
        a = 2
        while a < n:
            a += 1
            b = primes[-1] + 1
            while 2**(b - 1) % b != 1: #теорема  Ферма
                b += 1
            primes.append(b)
        return primes
    else:
        return primes


parser = argparse.ArgumentParser()
parser.add_argument('--show-all', '-a', action='store_true', default=False, help='Если хотите все простые числа до n-го')
parser.add_argument('--file', '-f', action='store', default=None, help='Если хотите записать числа в файл')
parser.add_argument('number', action='store', nargs="?", help='Номер простого числа', type=int)
namespace = parser.parse_args()

N = namespace.number
primes = prime_gen(N, primes)

if namespace.file is not None:
    with open(namespace.file, 'w') as file:
        flag = namespace.show_all
        if flag:
            print(*primes[1::])
            for i in range(len(primes) - 1):
                file.write(str(primes[i + 1]) + ' ')
        else:
            print(primes[N])
            file.write(str(primes[N]) + ' ')
