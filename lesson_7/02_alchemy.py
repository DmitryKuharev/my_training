# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
class Water:
    def __init__(self):
        self.element = "water"

    def __str__(self):
        return self.element

    def __add__(self, second_element):
        if isinstance(second_element, Wind):
            return "Storm"
        elif isinstance(second_element, Fire):
            return "Steam"
        elif isinstance(second_element, Earth):
            return "Dirt"


class Wind:
    def __init__(self):
        self.element = "wind"

    def __str__(self):
        return self.element

    def __add__(self, second_element):
        if isinstance(second_element, Water):
            return "Storm"
        elif isinstance(second_element, Fire):
            return "Lightning"
        elif isinstance(second_element, Earth):
            return "Dust"


class Fire:
    def __init__(self):
        self.element = "fire"

    def __str__(self):
        return self.element

    def __add__(self, second_element):
        if isinstance(second_element, Wind):
            return "Lightning"
        elif isinstance(second_element, Water):
            return "Steam"
        elif isinstance(second_element, Earth):
            return "Lava"


class Earth:
    def __init__(self):
        self.element = "earth"

    def __str__(self):
        return self.element

    def __add__(self, second_element):
        if isinstance(second_element, Wind):
            return "Dust"
        elif isinstance(second_element, Fire):
            return "Lava"
        elif isinstance(second_element, Water):
            return "Dirt"


print(Water(), '+', Wind(), '=', Water() + Wind())
print(Fire(), '+',Water() , '=', Fire() + Water())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Water(), '+', Water(), '=', Water() + Water())
# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())



# secret_number = 75
# n = 0
# while True:
#     user_n = int(input('Введите число от 1 до 100: '))
#     n += 1
#     if user_n == secret_number:
#         print(f"Угадано за  {n} попыток")
#         break
#     elif user_n < secret_number:
#         print("Загаданное число больше")
#     elif user_n > secret_number:
#         print("Загаданное число меньше")
#
# arr = ['add', 1, 'give', 6, 'as', 3, 'odd', 7]
#
#
# def odd_ball(arr):
#     return arr.index('odd') in arr
#
#
# def find_sum(n):
#     res = 0
#     for i in range(n + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             res += i
#     print(res)
#
#
# def find_sum2(n):
#     return sum(i for i in range(n+1) if i % 3 == 0 or i % 5 == 0)
#
#
# def name(names):
#     return [i for i in names if len(i) == 4]
