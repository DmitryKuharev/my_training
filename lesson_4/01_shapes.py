# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника


# def triangle(start, length, angel=0):
#     for _ in range(3):
#         v = sd.get_vector(start_point=start, angle=angel, length=length)
#         v.draw()
#         start = v.end_point
#         angel += 120
#
#
# point = sd.get_point(200, 200)
# triangle(point, length=200)

# - квадрата
# def square(start, length, angel=0):
#     for _ in range(4):
#         v = sd.get_vector(start_point=start, angle=angel, length=length, width=50)
#         v.draw()
#         start = v.end_point
#         angel += 90
#
#
# point = sd.get_point(200, 200)
# square(point, length=200)

n = 5
# - пятиугольника


def pentagon(start, length, angel=0):
    for _ in range(n):
        v = sd.get_vector(start_point=start, angle=angel, length=length)
        v.draw()
        start = v.end_point
        angel += 360/n


point = sd.get_point(200, 200)
pentagon(point, length=200)

# - шестиугольника

# def square(start, length, angel=0):
#     for _ in range(6):
#         v = sd.get_vector(start_point=start, angle=angel, length=length)
#         v.draw()
#         start = v.end_point
#         angel += 60
#
#
# point = sd.get_point(200, 200)
# square(point, length=200, angel=25)
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()



sd.pause()
