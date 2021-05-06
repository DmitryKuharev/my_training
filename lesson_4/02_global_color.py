import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом
print("Возможные цвета:\n 1 - Красный\n 2 - Оранжевый\n 3 - Желтый\n 4 - Зеленый\n 5 - Бирюзовый\n"
      " 6 - Голубой\n 7 - Сиреневый")
vod = int(input('Введите цвет фигур(цифру): '))


def pentagon(start, length, angel=0):
    for _ in range(n):
        v = sd.get_vector(start_point=start, angle=angel, length=length, width=3)
        v.draw(color=color_1)
        start = v.end_point
        angel += 360 / n


if vod in range(0, 8):
    color_print = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN,
                   sd.COLOR_BLUE, sd.COLOR_PURPLE)
    color_1 = color_print[vod - 1]
    for n in range(3, 7):
        if n == 3:
            point = sd.get_point(100, 100)
            pentagon(point, length=100)
        elif n == 4:
            point = sd.get_point(300, 100)
            pentagon(point, length=100)
        elif n == 5:
            point = sd.get_point(100, 300)
            pentagon(point, length=50)
        elif n == 6:
            point = sd.get_point(300, 300)
            pentagon(point, length=50)
    sd.pause()

else:
    print("Не верный ввод! Повторите еще раз!")
    sd.quit()


# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE





