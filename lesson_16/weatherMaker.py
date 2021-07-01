import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


class WeatherMaker:
    re_temperature = r'\+\d+'

    def __init__(self):
        self.weather_dict = {}

    def get_weather(self):
        site = requests.get('https://yandex.by/pogoda/mogilev')
        html_doc = BeautifulSoup(site.text, features='html.parser')
        list_day = html_doc.find_all('time', {'class': 'time forecast-briefly__date'})
        temperature_days = html_doc.find_all(
            'div',
            {"class": "temp forecast-briefly__temp forecast-briefly__temp_day"}
        )
        temperature_nights = html_doc.find_all(
            'div',
            {"class": "temp forecast-briefly__temp forecast-briefly__temp_night"}
        )
        state_weather = html_doc.find_all('div', {'class': "forecast-briefly__condition"})
        for date, t_day, t_night, state in zip(list_day, temperature_days, temperature_nights, state_weather):
            correct_date = datetime.strptime(date.get('datetime')[:10], '%Y-%m-%d').strftime('%d.%m.%Y')
            self.weather_dict[correct_date] = {
                'weather': state.text,
                't_day': re.search(self.re_temperature, t_day.text).group(),
                't_night': re.search(self.re_temperature, t_night.text).group(),
                'date': correct_date
            }
        return self.weather_dict
