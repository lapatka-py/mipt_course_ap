value = input()

try:
    type_value = type(value)
    if type_value == 'str':
        value = int(value)
    else:
        pass
except ValueError:
    print('Буквы в цифры не преобразовать!')
finally:
    print('Дошел до finally')

# test
# ghbdtn - error
# 567 - all right

print(value)