# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
import time
from pprint import pprint


class Parser:

    def __init__(self, file_name, report_file):
        self.file_name = file_name
        self.report = {}
        self.report_file = report_file

    def open_file_read(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                self.processing(line)

    def processing(self, line):
        if 'NOK' in line:
            if line[:17] + ']' in self.report:
                self.report[line[:17] + ']'] += 1
            else:
                self.report[line[:17] + ']'] = 1

    def write_file(self):
        with open(self.report_file, 'w') as f:
            for k, m in self.report.items():
                f.write(f'{k} {m}\n')



file = Parser('events.txt', 'report_file.txt')
file.open_file_read()

file.write_file()