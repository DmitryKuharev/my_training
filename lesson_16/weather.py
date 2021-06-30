# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погода
# Из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю. из БД

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database

from datetime import datetime, timedelta
from weatherMaker import WeatherMaker
from imageMaker import ImageMaker
from databaseUpdater import DatabaseUpdater


class Weather:
    def __init__(self):
        self.weather_data = None

    def check_user_input(self):
        choice = input()
        try:
            if int(choice) in range(1, 5):
                return int(choice)
            else:
                raise Exception
        except Exception:
            print('Некорректный ввод, повторите')
            return self.check_user_input()

    def check_date(self):
        date = input().split('-')
        try:
            for d in date:
                datetime.strptime(d.replace(' ', ''), '%d.%m.%Y')
                return date
        except Exception:
            print('Некорректный ввод, повторите')
            return self.check_date()

    def run(self):
        weather = WeatherMaker()
        self.weather_data = weather.get_weather()
        print('1. Добавление прогнозов за диапазон дат в базу данных\n'
              '2. Получение прогнозов за диапазон дат из базы\n'
              '3. Создание открыток из полученных прогнозов\n'
              '4. Выведение полученных прогнозов на консоль'
              )
        user_input = self.check_user_input()
        if user_input == 1:
            bd = DatabaseUpdater()
            bd.save_data(self.weather_data)
        elif user_input == 2:
            bd = DatabaseUpdater()
            bd.get_data()
        elif user_input == 3:
            print('Введиде дату или диапозон дат через дефиз(Например: 01.07.2021 или 01.07.2021-03.07.2021)')
            date = self.check_date()
            if len(date) == 1:
                img = ImageMaker()
                img.draw_postcard(self.weather_data[date[0]])
            elif len(date) == 2:
                start = datetime.strptime(date[0].replace(' ', ''), '%d.%m.%Y')
                end = datetime.strptime(date[1].replace(' ', ''), '%d.%m.%Y')
                date_list = [start + timedelta(days=x) for x in range(0, (end-start).days + 1)]
                for day in date_list:
                    img = ImageMaker()
                    img.draw_postcard(self.weather_data[day.strftime("%d.%m.%Y")])
        elif user_input == 4:
            pass

if __name__ == "__main__":
    w = Weather()
    w.run()