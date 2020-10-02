def decor(func):
    def wrapper(arg):
        value = func(arg)
        if value == 0:
            print('Нет')
        elif 0 < value <= 10:
            if value == 1:
                print(value, "- четное число!")
            elif 2 <= value <= 4:
                print(value, '- четных числа!')
            else:
                print(value, '- четных чисел!')
        else:
            print('Очень много')
    return wrapper

@decor
def even_finder(list_of_numbers):
    count = 0
    for x in list_of_numbers:
        if x % 2 == 0:
            count += 1
    return count

try:
    numbers = list(map(int, input().split()))
except ValueError:
    print("Введите список целых чисел")

even_finder(numbers)
