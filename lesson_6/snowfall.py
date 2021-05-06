import simple_draw as sd

sd.resolution = (1200, 600)
snow = []


def create_snowflake(n):
    """создает n снежинок"""
    global snow
    for _ in range(n):
        x = sd.random_number(0, sd.resolution[0])
        y = sd.random_number(sd.resolution[1] - 550, sd.resolution[1])
        length = sd.random_number(10, 20)
        factor_a = sd.random_number(55, 65) / 100
        factor_b = sd.random_number(3, 4) / 10
        factor_c = sd.random_number(50, 70)
        snow.append({'x': x,
                     'y': y,
                     'length': length,
                     'factor_a': factor_a,
                     'factor_b': factor_b,
                     'factor_c': factor_c})


def paint_snowflake_color(color=sd.COLOR_WHITE):
    """отрисовывает все снежинки цветом color"""
    for i in snow:
        sd.start_drawing()
        first_point = sd.get_point(i['x'], i['y'])
        sd.snowflake(center=first_point, length=i['length'], color=color,
                     factor_a=i['factor_a'], factor_b=i['factor_b'], factor_c=i['factor_c'])
    sd.finish_drawing()


def move_snowflake():
    global snow
    for i in snow:
        i['x'] += sd.random_number(-6, 6)
        i['y'] -= 10


def numbers_reached_bottom_screen():
    """выдает список номеров снежинок, которые вышли за границу экрана"""
    global snow
    snow_remove = []
    for i in snow:
        if i['y'] <= 10:
            snow_remove.append(i)
    return snow_remove


def delete_snowflake(number):
    """удаляет снежинки с номерами из списка"""
    global snow
    for number in number:
        if number in snow:
            sd.snowflake(center=sd.get_point(number['x'], number['y']),
                         length=number['length'],
                         color=sd.background_color,
                         factor_a=number['factor_a'],
                         factor_b=number['factor_b'],
                         factor_c=number['factor_c'])
            snow.remove(number)
