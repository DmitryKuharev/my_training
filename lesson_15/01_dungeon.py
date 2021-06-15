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
import datetime
from termcolor import cprint


RULES = 'Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах, планируя набеги на\n' \
        'близлежащие поселения. Само подземелье состоит из двух главных разветвлений и нескольких развилок,и лишь\n' \
        'один из путей приведёт вас к главному Боссу и позволит предотвратить набеги и спасти мирных жителей.\n' \
        'Правила игры! Необходимо исследовать это подземелье выбирая действие вводом чисел.\n' \
        'Движение осуществляется только в глубь подземелья - обратного пути нет!\n' \
        'Как победить? Необхобимо набрать 280 очков опыта, и следить за тем, чтобы не закончился запас времени, т.к \n' \
        'перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации\n' \
        'Так же время расходуется при атаке монстров.\nУдачи!\n'


class Dungeon:
    re_experience = r'exp(\d+)'
    re_time = r'tm([0-9]*[.,]?[0-9]*)'
    field_names = ['current_location', 'current_experience', 'current_date']

    def __init__(self, json_file_game):
        self.json_file_game = json_file_game
        self.journal = []
        self.json_data_file = {}
        self.player_experience = 0
        self.remaining_time = decimal.Decimal('1234567890.0987654321')
        self.start_time = datetime.datetime.now().replace(microsecond=0)
        self.expected_value = 0
        self.monsters = {}
        self.locations = {}
        self.trigger = True
        self.current_location = ''

    def open_game_file(self):
        cprint(RULES, 'grey', attrs=['bold'])
        with open(self.json_file_game, 'r') as file:
            self.json_data_file = json.load(file)
            return self.json_data_file

    def write_journal_file(self):
        with open('dungeon.csv', 'w', newline='', encoding='utf-8') as file:
            write = csv.DictWriter(file, dialect="excel", fieldnames=self.field_names)
            write.writeheader()
            write.writerows(self.journal)

    def check_user_input(self):
        choice = input()
        try:
            if int(choice) in range(1, self.expected_value + 1):
                return int(choice)
            else:
                raise Exception
        except Exception:
            cprint('Некорректный ввод, повторите')
            return self.check_user_input()

    def attack_monster(self):
        cprint('\nВыбирете какого монстра атаковать:', 'red')
        for monster in self.monsters:
            print(f'{monster} - {self.monsters[monster][0]}')
        self.expected_value = len(self.monsters)
        monster_choice = self.check_user_input()
        dead_monster = self.monsters[monster_choice][0]
        print(f'Вы уничтожили {dead_monster}\n')
        self.json_data_file[self.current_location].remove(dead_monster)
        self.player_experience += int(re.search(self.re_experience, dead_monster)[1])
        self.remaining_time -= decimal.Decimal(re.search(self.re_time, dead_monster)[1])

    def move(self):
        print(f'Выбирете локацию:')
        for location in self.locations:
            print(f'{location} - {self.locations[location][0]}')
        self.expected_value = len(self.locations)
        location_choice = self.check_user_input()
        self.json_data_file = self.json_data_file[self.current_location][self.locations[location_choice][1]]
        self.current_location = list(self.json_data_file.keys())[0]
        self.remaining_time -= decimal.Decimal(re.search(self.re_time, self.current_location)[1])

    def game(self):
        self.current_location = list(self.json_data_file.keys())[0]
        self.monsters = {}
        self.locations = {}
        monster_count = 1
        location_count = 1
        end_time = datetime.datetime.now().replace(microsecond=0)
        cprint(f'Вы находитесь в {self.current_location}', 'green')
        cprint(f'У вас {self.player_experience} опыта и осталось {self.remaining_time} секунд', 'green')
        cprint(f'Прошло уже {end_time - self.start_time}', 'green')
        self.journal.append({self.field_names[0]: self.current_location,
                             self.field_names[1]: self.player_experience,
                             self.field_names[2]: datetime.datetime.now()})
        if self.json_data_file[self.current_location]:
            cprint('\nВнутри вы видите:', attrs=['underline'])
            for value in self.json_data_file[self.current_location]:
                if isinstance(value, str):
                    cprint(f'-- Монстра {value}', 'red', attrs=['dark'])
                    self.monsters[monster_count] = [value, self.json_data_file[self.current_location].index(value)]
                    monster_count += 1
                elif isinstance(value, dict):
                    for next_location in value.keys():
                        cprint(f'-- Вход в локацию: {next_location}', 'magenta')
                        self.locations[location_count] = [next_location,
                                                          self.json_data_file[self.current_location].index(value)]
                        location_count += 1
        if self.monsters and self.locations:
            cprint('\nВыберите действие:', attrs=['underline'])
            cprint('1.Атаковать монстра\n2.Перейти в другую локацию\n3.Выход\nВаш выбор: ')
            self.expected_value = 3
            choice = self.check_user_input()
            if choice == 1:
                self.attack_monster()
            elif choice == 2:
                self.move()
            else:
                self.trigger = False
        elif self.monsters:
            cprint('\nВыберите действие:', attrs=['underline'])
            cprint('1.Атаковать монстра\n2.Выход\nВаш выбор: ')
            self.expected_value = 2
            choice = self.check_user_input()
            if choice == 1:
                self.attack_monster()
            else:
                self.trigger = False
        elif self.locations:
            cprint('\nВыберите действие:', attrs=['underline'])
            cprint('1.Перейти в другую локацию\n2.Выход\nВаш выбор: ')
            self.expected_value = 2
            choice = self.check_user_input()
            if choice == 1:
                self.move()
            else:
                self.trigger = False
        else:
            if self.player_experience >= 280 and int(self.remaining_time) > 0:
                cprint(f'Вы победили!!!\n Ваш опыт:{self.player_experience} и оставшееся время:{self.remaining_time}',
                       'red', attrs=['underline'])
                self.trigger = False
            else:
                cprint(f'Конец игры\nВаш опыт:{self.player_experience} и оставшееся время:{self.remaining_time}', 'red')
                self.trigger = False

    def play_game(self):
        if int(self.remaining_time) < 0:
            self.trigger = False
            cprint(f'Время вышло\nВаш опыт:{self.player_experience} и время:{self.remaining_time}', 'red')
        while self.trigger:
            self.game()
        self.write_journal_file()


if __name__ == "__main__":
    game = Dungeon('rpg.json')
    game.open_game_file()
    game.play_game()

