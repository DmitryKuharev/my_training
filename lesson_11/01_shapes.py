import simple_draw as sd

# На основе вашего кода из решения lesson_4/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_figure(point, angle, length):
        for _ in range(n):
            vector = sd.get_vector(start_point=point, angle=angle, length=length)
            vector.draw()
            point = vector.end_point
            angle += 360 / n
    return draw_figure


draw = get_polygon(n=8)
draw(point=sd.get_point(200, 200), angle=30, length=100)


sd.pause()
