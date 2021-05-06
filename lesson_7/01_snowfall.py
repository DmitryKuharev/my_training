import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.random_number(sd.resolution[1], sd.resolution[1] + sd.resolution[1] * 1.1)
        self.length = sd.random_number(10, 20)
        self.factor_a = sd.random_number(55, 65) / 100
        self.factor_b = sd.random_number(3, 4) / 10
        self.factor_c = sd.random_number(50, 70)

    def clear_previous_picture(self):
        """удаляет все с экрана"""
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c, color=sd.background_color)

    def move(self):
        """Перемещает снежинку"""
        self.x += sd.random_number(-2, 2)
        self.y -= 10

    def draw(self):
        """Рисует снежинку"""
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)

    def can_fall(self):
        """Проверяет достигла ли снежинка низа экрана"""
        if self.y <= 10:
            return True


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:


def get_flakes(count):
    """Генератор снежинок"""
    return [Snowflake() for _ in range(count)]


flakes = get_flakes(count=50)  # создать список снежинок


def get_fallen_flakes():
    b = 0
    for i in flakes:
        if i.can_fall():
            b += 1
            flakes.remove(i)
    return b


def append_flakes(count):
    for _ in range(count):
        snow = Snowflake()
        flakes.append(snow)


while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

#
#
#
#
# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
