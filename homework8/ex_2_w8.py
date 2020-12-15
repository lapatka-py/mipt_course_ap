def fib(n):
    if n > 0:
        num1 = 1
        yield num1
        if n > 1:
            num2 = 1
            yield num2
            if n > 2:
                k = 2
                while k != n:
                    num3 = num1 + num2
                    yield num3
                    num1, num2 = num2, num3
                    k += 1


for i in fib(0):
    print(i)
