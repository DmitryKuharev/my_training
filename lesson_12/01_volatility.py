# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
import operator
import zipfile as zf
import os
import time


def unzip(file):
    """Распаковка архива при необходимости"""
    zip_file = zf.ZipFile(file)
    zip_file.extractall()


class Data:
    def __init__(self, path_to_files):
        self.path_to_files = path_to_files
        self.tickers = {}
        self.zero_tickers = {}

    def run(self):
        for file in self.path_to_files:
            with open(file) as f:
                file_name = os.path.splitext(os.path.basename(file))[0]
                price = []
                for line in f:
                    simple_price = line.split(',')[2]
                    if simple_price != 'PRICE':
                        price.append(float(simple_price))
                maxim, minim = max(price), min(price)
                average_price = (maxim + minim)/2
                volatility = ((maxim - minim) / average_price) * 100
                if volatility == 0:
                    self.zero_tickers[file_name] = round(volatility, 4)
                else:
                    self.tickers[file_name] = round(volatility, 2)


def get_path_file(path):
    """Получение списка путей к файлам"""
    path_to_files = []
    for path, folder, files in os.walk(path):
        for file in files:
            path_to_files.append(os.path.join(path, file))
    return path_to_files


def time_track(func, *args, **kwargs):
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'\nВремя работы функции {elapsed} секунд(ы)')
    return result


@time_track
def main():
    file_name = get_path_file()
    voliativnost = Data(file_name)
    voliativnost.run()
    zero_sorted_tickers = sorted(voliativnost.zero_tickers.items(), key=operator.itemgetter(0))
    sorted_tickers = sorted(voliativnost.tickers.items(), key=operator.itemgetter(1))
    print(len(zero_sorted_tickers), len(sorted_tickers))
    print('Максимальная волатильность:')
    for ticker in reversed(sorted_tickers[-3:]):
        print(f'{ticker[0]} - {ticker[1]}')
    print('Минимальная волатильность:')
    for ticker in reversed(sorted_tickers[:3]):
        print(f'{ticker[0]} - {ticker[1]}')
    print(f'Нулевая волатильность:')
    for ticker in zero_sorted_tickers:
        print(f'{ticker[0]}', end=', ')



