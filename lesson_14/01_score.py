# -*- coding: utf-8 -*-

# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например, «-4» - ни одной кегли не было сбито за бросок (первый или второй)
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 3 фреймов запись результатов может выглядеть так:
#   «Х4/34»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – 20 очков, «4/» - 15 очков, «34» – сумма 3+4=7
# То есть для игры «Х4/34» сумма очков равна 20+15+7=42
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.
# 'X4/344/'

import argparse
from bowling import get_score
# '285-7/4/3/277-2---'
console = argparse.ArgumentParser(description='Определения количества очков игры в боулинг')
console.add_argument('--result', type=str, default=None, help='Введите результат в формате : X4/344/ или "X4/344/"')
arg = console.parse_args()
print(f'Количество очков для результатов {arg.result} - {get_score(arg.result)}')

# При написании кода помнить, что заказчик может захотеть доработок и новых возможностей...
# И, возможно, вам пригодится паттерн проектирования "Состояние",
#   см https://clck.ru/Fudd8 и https://refactoring.guru/ru/design-patterns/state

