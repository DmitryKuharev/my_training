# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
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
import operator
import zipfile as zf
import os
import time
import multiprocessing


def unzip(file):
    """Распаковка архива при необходимости"""
    zip_file = zf.ZipFile(file)
    zip_file.extractall()


class Data(multiprocessing.Process):

    def __init__(self, path_to_files, collection, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_to_files = path_to_files
        self.collection = collection

    def run(self):
        with open(self.path_to_files) as f:
            file_name = os.path.splitext(os.path.basename(self.path_to_files))[0]
            price = []
            for line in f:
                simple_price = line.split(',')[2]
                if simple_price != 'PRICE':
                    price.append(float(simple_price))
            maxim, minim = max(price), min(price)
            average_price = (maxim + minim)/2
            volatility = ((maxim - minim) / average_price) * 100
            self.collection.put(dict(file_name=file_name, volatility=volatility))


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
    collection = multiprocessing.Queue()
    zero_tickers = {}
    tickers = {}
    file_name = get_path_file()
    voliativnost = [Data(path_to_files=file, collection=collection) for file in file_name]
    for fun in voliativnost:
        fun.start()
    for fun in voliativnost:
        fun.join()
    while not collection.empty():
        data = collection.get()
        if data['volatility'] == 0:
            zero_tickers[data['file_name']] = round(data['volatility'], 4)
        else:
            tickers[data['file_name']] = round(data['volatility'], 4)
    zero_sorted_tickers = sorted(zero_tickers.items(), key=operator.itemgetter(0))
    sorted_tickers = sorted(tickers.items(), key=operator.itemgetter(1))
    print('Максимальная волатильность:')
    for ticker in reversed(sorted_tickers[-3:]):
        print(f'{ticker[0]} - {ticker[1]}')
    print('Минимальная волатильность:')
    for ticker in reversed(sorted_tickers[:3]):
        print(f'{ticker[0]} - {ticker[1]}')
    print(f'Нулевая волатильность:')
    for ticker in zero_sorted_tickers:
        print(f'{ticker[0]}', end=', ')
