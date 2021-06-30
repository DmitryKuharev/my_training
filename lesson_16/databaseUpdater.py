# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)
import os
from models import database_proxy, DataWeather
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE') or 'sqlite:///weather.db')
database_proxy.initialize(db)
database_proxy.create_tables([DataWeather])


class DatabaseUpdater:

    def __init__(self):
        self.data = DataWeather

    def save_data(self, data_to_add: dict):
        for weather_date in data_to_add.keys():
            weather, created = self.data.get_or_create(date=weather_date, defaults=data_to_add[weather_date])
            if not created:
                self.data.update(data_to_add[weather_date]).where(DataWeather.id == weather.id).execute()

    def get_data(self, date: str):
        for data in self.data.select().where(self.data.date == date):
            return f'Погода {data.date} - {data.weather}\n'\
                   f'Температура днем:{data.t_day}\nТемпература ночью:{data.t_night}'
