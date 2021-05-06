import simple_draw as sd

sd.resolution = (1200, 600)


def bubble_paint(x, y, step):
    point = sd.get_point(x, y)
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2)
        radius += step


# Нарисовать три ряда по 10 пузырьков
for y in range(100, 400, 100):
    for x in range(100, 1000, 90):
        bubble_paint(x, y, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    sd.circle(sd.random_point(), 50, sd.random_color())


sd.pause()
