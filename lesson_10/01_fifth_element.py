# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as valerr:
    print(f'Не верный ввод,введите 5 чисел, а не буквы. Ошибка: {valerr}')
except IndexError as index:
    print(f'Не верный ввод,введите 5 чисел или больше. Ошибка: {index}')
except Exception as ex:
    print(f'Непонятная ошибка. Ошибка: {ex}')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




