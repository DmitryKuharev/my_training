
import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

print("Возможные фигуры:\n0:Треугольник\n1:Квадрат\n2:Пятиугольник\n3:Шестиугольник")
figure = int(input("Введите номер фигуры: "))


def paint_figure(start, length, angel=0):
    for _ in range(n):
        v = sd.get_vector(start_point=start, angle=angel, length=length, width=3)
        v.draw()
        start = v.end_point
        angel += 360 / n


if figure in range(0, 4):
    n = figure + 3
    if n == 3:
        point = sd.get_point(100, 100)
        paint_figure(point, length=100)
    elif n == 4:
        point = sd.get_point(300, 100)
        paint_figure(point, length=100)
    elif n == 5:
        point = sd.get_point(100, 300)
        paint_figure(point, length=50)
    elif n == 6:
        point = sd.get_point(300, 300)
        paint_figure(point, length=50)
else:
    print("Не верный ввод!")
    sd.quit()
sd.pause()

# Код функций из упр lesson_004/02_global_color.py скопировать сюда





