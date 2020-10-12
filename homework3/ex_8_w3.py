def division(numerator, denominator):
    try:
        value = numerator / denominator
        return value
    except ZeroDivisionError:
        print('Делим на ноль? НЕ НАДО ТАК!')

# test
# 5 0

num1, num2 = map(int, input().split())

print(division(num1, num2))