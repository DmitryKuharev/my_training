
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".

import simple_draw as sd
from art import list_art

sd.resolution = 1500, 600


list_art.man(1300, 350)
list_art.rainbow()
list_art.grass()
list_art.house()

snow = []
for _ in range(200):
    snow.append(list_art.generate_snow())

for i in snow:
    first_point = sd.get_point(i['x'], i['y'])
    list_art.snow(center=first_point, length=i['length'])


point_s = sd.get_point(900, 0)
list_art.draw_branches(point=point_s, angle=90, length=150)


sd.pause()


