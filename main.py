# Задание
# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.


class MyException(Exception):
    def __init__(self, text):
        print(f'The value:{text} is wrong.')


A = 33
try:
    value = int(input('Input value: '))
    if value == A:
        raise MyException(value)
except MyException as e:
    print('Error: ')
    print(e)

print('Done.')