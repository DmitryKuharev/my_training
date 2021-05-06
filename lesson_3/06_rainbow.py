
# (цикл for)

import simple_draw as sd


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
point = sd.get_point(240, 50)
radius = 400
i = 6
for color in rainbow_colors:
    radius += 5
    sd.circle(center_position=point, radius=radius, color=color, width=4)
    i -= 1

sd.line(sd.get_point(0, 0), sd.get_point(600, 0), color=sd.COLOR_GREEN,  width=100)

sd.pause()
