
# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y):
    center = sd.get_point(x, y)
    sd.circle(center, 100)
    sd.circle(sd.get_point(x - 50, y + 25), 20)
    sd.circle(sd.get_point(x + 50, y + 25), 20)
    sd.line(sd.get_point(x - 50, y - 50), sd.get_point(x + 50, y - 50))
    sd.line(sd.get_point(x - 55, y - 45), sd.get_point(x - 50, y - 50))
    sd.line(sd.get_point(x + 50, y - 50), sd.get_point(x + 55, y - 45))


smile(sd.random_number(100, 500), sd.random_number(100, 500))

sd.pause()
