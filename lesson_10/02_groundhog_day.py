# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    def __str__(self):
        return "IamGodError"


class DrunkError(Exception):
    def __str__(self):
        return "DrunkError"


class CarCrashError(Exception):
    def __str__(self):
        return "CarCrashError"


class GluttonyError(Exception):
    def __str__(self):
        return "GluttonyError"


class DepressionError(Exception):
    def __str__(self):
        return "DepressionError"


class SuicideError(Exception):
    def __str__(self):
        return "SuicideError"


errors = {1: IamGodError, 2: DrunkError, 3: CarCrashError, 4: GluttonyError, 5: DepressionError, 6: SuicideError}


def one_day():
    dice = random.randint(1, 13)
    dice_for_error = random.randint(1, 6)
    if dice == 13:
        raise errors[dice_for_error]
    else:
        return random.randint(1, 7)


carma = 0
while carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        carma += one_day()
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as ige:
        with open("carmalog.txt", 'a', encoding="utf8") as ff:
            ff.write(f"Type error- {ige} \n")
    print(carma)
