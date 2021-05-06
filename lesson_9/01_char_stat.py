# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
import os
import zipfile as zf
from pprint import pprint


class SymbolCount:

    def __init__(self, file_name):
        self.file_name = file_name
        self.symbol = {}

    def unzip(self):
        file = zf.ZipFile(self.file_name)
        for filename in file.namelist():
            file.extract(filename)
        self.file_name = filename

    def open_file(self):
        '''cp1251 or utf8'''
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.read_by_line(line)

    def read_by_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.symbol:
                    self.symbol[char] += 1
                else:
                    self.symbol[char] = 1

    def report_output(self):
        print(f'+---------+----------+\n|{"буква":^9}|{"частота":^10}|\n+---------+----------+')
        total = 0
        for i in sorted(self.symbol):
            total += self.symbol[i]
            print(f"|{i:^9}|{self.symbol[i]:^10}|")
        print(f'+---------+----------+\n|{"итого":^9}|{total:^10}|\n+---------+----------+')

    def act(self):
        self.open_file()
        self.report_output()

# stat_file = SymbolCount(file_name='voyna-i-mir.txt')
# stat_file.open_file()
# stat_file.report_output()


class Vozrastanie(SymbolCount):
    """по частоте по возрастанию"""
    def __init__(self, file_name):
        super().__init__(file_name)

    def report_output(self):
        print(f'+---------+----------+\n|{"буква":^9}|{"частота":^10}|\n+---------+----------+')
        total = 0
        for i in sorted(self.symbol.items(), key=lambda x: x[1], reverse=True):
            total += i[1]
            print(f"|{i[0]:^9}|{i[1]:^10}|")
        print(f'+---------+----------+\n|{"итого":^9}|{total:^10}|\n+---------+----------+')


stat_file = Vozrastanie(file_name='voyna-i-mir.txt.zip')
stat_file.act()
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию