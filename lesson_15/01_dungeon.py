# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход
# если изначально не писать число в виде строки - теряется точность!
# Учитывая время и опыт, не забывайте о точности вычислений!

import json
import csv
import decimal
import re
import time

field_names = ['current_location', 'current_experience', 'current_date']
json_file = 'rpg.json'


def open_game_file(json_game_file):
    with open(json_game_file, 'r') as file:
        json_data_file = json.load(file)
        start_time = time.time()
        current_location = list(json_data_file.keys())[0]
        re_experience = r'exp(\d+)'
        re_time = r'tm(\d+)'
        remaining_time = decimal.Decimal('1234567890.0987654321')
        while True:
            monsters = {}
            locations = {}

            player_experience = 0
            monster_count = 1
            location_count = 1
            print(f'Вы находитесь в {current_location}')
            print(f'У вас {player_experience} опыта и осталось {remaining_time} секунд')
            print('Прошло уже 0:00:00')
            print('Внутри вы видите:')
            for value in json_data_file[current_location]:
                if isinstance(value, str):
                    print(f'-- Монстра {value}')
                    monsters[monster_count] = [value, json_data_file[current_location].index(value)]
                    monster_count += 1
                elif isinstance(value, dict):
                    for next_location in value.keys():
                        print(f'-- Вход в локацию: {next_location}')
                        locations[location_count] = [next_location, json_data_file[current_location].index(value)]
                        location_count += 1
            print('Выберите действие:')
            if monsters:
                choice = int(input('1.Атаковать монстра\n2.Перейти в другую локацию\n3.Выход\n'))
            else:
                choice = int(input('1.Перейти в другую локацию\n2.Выход\n')) + 1
            if choice == 1:
                print(f'Выбирете какого монстра атаковать:')
                for monster in monsters:
                    print(f'{monster} - {monsters[monster][0]}')
                monster_choice = int(input())
                dead_monster = monsters[monster_choice][0]
                print(f'Вы уничтожили {dead_monster}')
                json_data_file[current_location].remove(dead_monster)
                player_experience += re.search(re_experience, dead_monster)[1]
                remaining_time -= decimal.Decimal(re.search(re_time, dead_monster)[1])
            elif choice == 2:
                print(f'Выбирете локацию:')
                for location in locations:
                    print(f'{location} - {locations[location][0]}')
                location_choice = int(input())
                json_data_file = json_data_file[current_location][locations[location_choice][1]]
                current_location = list(json_data_file.keys())[0]
                remaining_time -= decimal.Decimal(re.search(re_time, current_location)[1])
            elif choice == 3:
                print('Game over')
                return False
            else:
                print("Неверный ввод")
            round_time = round(time.time() - start_time, 5)


if __name__ == "__main__":
    open_game_file(json_file)
