# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import os


class NotNameError(Exception):
    def __str__(self):
        return "Поле имени содержит НЕ только буквы"


class NotEmailError(Exception):
    def __str__(self):
        return "Поле емейл НЕ содержит @ и .(точку)"


def check_line(line_to_act):
    line_list = line_to_act.split(' ')
    if len(line_list) != 3:
        raise ValueError(f"НЕ присутсвуют все три поля в строке {line}")
    else:
        if not line_list[0].isalpha():
            raise NotNameError(f"Поле имени содержит НЕ только буквы в строке {line}")
        if "@" not in line_list[1] or "." not in line_list[1]:
            raise NotEmailError(f"Поле емейл НЕ содержит @ и .(точку) в строке {line}")
        if not int(line_list[2]) in range(10, 100):
            raise ValueError(f"Поле возраст НЕ является числом от 10 до 99 в строке {line}")


file = os.path.normpath("D:\\Skillbox\\10. Исключения\\lesson_010\\registrations.txt")
good_log = []
bad_log = []
with open(file, "r", encoding="utf8") as ff:
    for line in ff:
        line = line[:-1]
        try:
            check_line(line)
        except (ValueError, NotNameError, NotEmailError) as ex:
            print(f'Ошибка - {ex}')
            bad_log.append(line + '\n')
        else:
            good_log.append(line + '\n')

with open('good_log.txt', 'a', encoding='utf8') as f:
    for line in good_log:
        f.write(line)
with open('bad_log.txt', 'a', encoding='utf8') as f:
    for line in bad_log:
        f.write(line)