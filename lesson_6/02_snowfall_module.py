import simple_draw as sd
import snowfall


sd.resolution = (1200, 600)
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

snowfall.create_snowflake(100)
while True:
    snowfall.paint_snowflake_color(color=sd.background_color)
    snowfall.move_snowflake()
    snowfall.paint_snowflake_color()
    reached_bottom = snowfall.numbers_reached_bottom_screen()
    if reached_bottom:
        create_new_snowflake = len(reached_bottom)
        snowfall.delete_snowflake(reached_bottom)
        snowfall.create_snowflake(create_new_snowflake)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
