# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
N = 100


def generate_snow():
    x = sd.random_number(10, sd.resolution[0])
    y = sd.random_number(sd.resolution[1]+50, sd.resolution[1]+500)
    length = sd.random_number(10, 20)
    factor_a = sd.random_number(55, 65)/100
    factor_b = sd.random_number(3, 4)/10
    factor_c = sd.random_number(50, 70)
    return {'x': x,
            'y': y,
            'length': length,
            'factor_a': factor_a,
            'factor_b': factor_b,
            'factor_c': factor_c}


snow = []
for _ in range(N):
    snow.append(generate_snow())


while True:
    for i in snow:
        sd.start_drawing()
        first_point = sd.get_point(i['x'], i['y'])
        sd.snowflake(center=first_point, length=i['length'], color=sd.background_color,
                     factor_a=i['factor_a'], factor_b=i['factor_b'], factor_c=i['factor_c'])
        i['x'] += sd.random_number(-5, 5)
        i['y'] -= 10
        second_point = sd.get_point(i['x'], i['y'])
        sd.snowflake(center=second_point, length=i['length'], color=sd.COLOR_WHITE,
                     factor_a=i['factor_a'], factor_b=i['factor_b'], factor_c=i['factor_c'])
        if i['y'] < 15:
            i['y'] = sd.random_number(sd.resolution[1], sd.resolution[1] + 200)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()